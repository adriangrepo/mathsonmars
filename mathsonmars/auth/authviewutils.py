import datetime
import re
import logging

from flask import current_app
from email_validator import validate_email, EmailNotValidError
from mathsonmars.models import FailedLoginAttempt, db, User, Role, \
    BlockedIPForUser, SignupType, UserAgent, Student
from mathsonmars.constants.modelconstants import LoginConstants
from mathsonmars.auth.authconstants import InvalidPasswords
from mathsonmars.utils.stringutils import StringUtils
from random import shuffle
import random
import string
from flask import flash, request
#from flask.ext.login import LoginManager, current_user, login_user, login_required, logout_user
from sqlalchemy import exc
from itsdangerous import URLSafeTimedSerializer

from mathsonmars.constants.modelconstants import RoleTypes, DefaultUserName,\
    EmailTypes, SignUpConstants
from mathsonmars.email import send_email
from mathsonmars.constants.userconstants import ProfileConstants

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AuthViewUtils(object):
    special_char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
             'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
            }

    basic_char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
             'nums': '0123456789',
             'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            }
    
    @classmethod
    def timeDeltaValid(cls, db, user, rate_limit, remote_ip):
        '''limit time between log attempts from remote_ip to rate_limit seconds
        Could be improved as an attacks from multiple ip's sequentially on same user will be allowed
        @param db: db
        @param user: user
        @param rate_limit: secs
        @param remote_ip: ipv4 address
        '''
        valid_time = False
        now = datetime.datetime.now()
        failed_login = db.session.query(FailedLoginAttempt).filter(FailedLoginAttempt.user_id == user.id).first()
        if failed_login is not None:
            if failed_login.ip4_address == remote_ip:
                time_difference = now - failed_login.created
                time_difference_in_secs = time_difference / datetime.timedelta(seconds=1)
                logger.debug("timeDeltaValid last fail:{0} secs ago, from:{1} ".format(time_difference_in_secs, remote_ip))
                if time_difference_in_secs >= rate_limit:
                    valid_time = True
                else:
                    valid_time = False
            else:
                valid_time = True
        #make valid for first ever login attempt
        else:
            valid_time = True
        return valid_time
    
    @classmethod
    def addFailedLoginAttempt(cls, db, user, remote_ip, now):
        '''
        @param db: db
        @param user: user
        @param remote_ip: ipv4 address
        @param now: datetime
        '''
    
        logger.debug("--addFailedLoginAttempt() from ip:{0}".format(remote_ip))
        failed_login = FailedLoginAttempt(created = now, user_id = user.id, ip4_address=remote_ip)
        db.session.add(failed_login)
        db.session.commit()
        
    @classmethod
    def checkLoginsWithinTimePeriod(cls, db, user, num_hours, remote_ip, now):
        '''
        @param db: db
        @param user: user
        @param num_hours: eg 24hrs
        @param remote_ip: ipv4 address
        @param now: datetime
        '''
        logger.debug(">>checkLoginsWithinTimePeriod()")
        valid_login_attempt = False
        last_failed_logins = db.session.query(FailedLoginAttempt).filter(FailedLoginAttempt.user_id == user.id).filter(FailedLoginAttempt.ip4_address == remote_ip).order_by(FailedLoginAttempt.created.desc()).limit(LoginConstants.MAX_LOGIN_ATTEMPTS).all()
        if last_failed_logins is not None and len(last_failed_logins) >= LoginConstants.MAX_LOGIN_ATTEMPTS:
            first_login = last_failed_logins[0]
            time_difference = now - first_login.created
            time_difference_in_hrs = time_difference / datetime.timedelta(hours=1)
            logger.debug("--checkLoginsWithinTimePeriod time difference:{0} count:{1}".format(time_difference_in_hrs, len(last_failed_logins)))
            if time_difference_in_hrs > num_hours:
                valid_login_attempt = True
        else:
            logger.debug("--checkLoginsWithinTimePeriod( ether no prev failed or < 10 login attempts)")
            valid_login_attempt = True
        return valid_login_attempt
    

    
    @classmethod
    def getRemoteAddress(cls, request):
        #see http://stackoverflow.com/questions/22868900/how-do-i-safely-get-the-users-real-ip-address-in-flask-using-mod-wsgi
        trusted_proxies = {'127.0.0.1'}  # define your own set
        route = request.access_route + [request.remote_addr]
        
        remote_addr = next((addr for addr in reversed(route) 
                            if addr not in trusted_proxies), request.remote_addr)
        return remote_addr
    
    @classmethod
    def anyUrlRegex(cls):
        regex = r"""(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))"""
        return regex
    
    @classmethod
    def getLinksInText(cls, page_text):
        urls = re.findall(AuthViewUtils.anyUrlRegex(), page_text)
        return urls
    
    @classmethod
    def isEmpty(cls, any_structure):
        if any_structure:
            return False
        else:
            return True
    
    @classmethod    
    def email_firewall(cls, email, check_deliverability):
        '''
        @email: string, email address
        @check_deliverability: boolean
        @return: empty string or error string
        '''
        try:
            v = validate_email(email, check_deliverability) # validate and get info
            email = v["email"] # replace with normalized form
        except EmailNotValidError as e:
            # email is not valid
            return e
        return ""
            
    @classmethod
    def passwordIsTooSimple(cls, paramPassword):
        too_simple = False
        if StringUtils.hasNumbers(paramPassword) and StringUtils.hasAlphabetics(paramPassword):
            too_simple = False
        else:
            too_simple = True
        return too_simple
    
    @classmethod
    def passwordIsCommon(cls, paramPassword):
        common_password = False
        if paramPassword in InvalidPasswords.BAD_PASSWORDS:
            common_password = True           
        else:
            for item in InvalidPasswords.BAD_PASSWORDS:
                for i in range(9):
                    if (paramPassword == str(i)+item) or (paramPassword == item+str(i)):
                        common_password = True
        return common_password
    
    @classmethod
    def generateUsername(cls, postfix_length, param_initials):
        """Function to generate a semi-random username"""
        assert isinstance(postfix_length, int), "Integer"
        assert (len(param_initials)==2), "2 digits"
        numbers = []
        for index in range(postfix_length):
            number_postfix = random.randint(0,9)
            numbers.append(str(number_postfix))
        str_postfix = "".join(numbers)
        username = param_initials.lower() + str_postfix
        return username
    
    @classmethod
    def generatePass(cls, pass_length):
        """Function to generate a password"""
        chars=string.ascii_letters + string.digits + string.punctuation
        password = []
        for _ in range(pass_length):
            password.append(random.choice(chars))
        return ''.join(password)
    
    @classmethod
    def generatePassLimitedPuctuation(cls, pass_length):
        """Function to generate a password with limited punctuation chars"""
        limited_punct = '#$*&!@:<>?%'
        chars=string.ascii_letters + string.digits + limited_punct
        password = []
        for _ in range(pass_length):
            password.append(random.choice(chars))
        return ''.join(password)
    
    @classmethod
    def generateWeakPass(cls, pass_length):
        """Function to generate a weak password"""
        digits = string.digits
        chars = string.ascii_letters
        password = []
        for _ in range(pass_length-2):
            password.append(random.choice(digits))
        for _ in range(2):
            password.append(random.choice(chars).lower())
        shuffle(password)
        return ''.join(password)
        
    @classmethod
    def checkPrevChar(cls, password, current_char_set):
        """Function to ensure that there are no consecutive 
        UPPERCASE/lowercase/numbers/special-characters."""
        index = len(password)
        if index == 0:
            return False
        else:
            prev_char = password[index - 1]
            if prev_char in current_char_set:
                return True
            else:
                return False
            
    @classmethod
    def createUniqueUsername(cls, student_role, first_name, last_name):
        '''try 100 times to create a unique name, then if still non unique make different'''
        retries = 0
        max_retries = 100
        initials = first_name[:1]+last_name[:1]
        student_user_name = AuthViewUtils.generateUsername(postfix_length=5, param_initials=initials.lower()) 
        existing_username = db.session.query(User).filter(User.role_id == student_role.id).filter(User.user_name == student_user_name).first()
        if existing_username:
            while retries < max_retries and (existing_username==True):
                #how many times do we need to check this?
                student_user_name = AuthViewUtils.generateUsername(postfix_length=6, param_initials=initials.lower()) 
                existing_username = db.session.query(User).filter(User.role_id == student_role.id).filter(User.user_name == student_user_name).first()
                retries += 1
        if existing_username:
            student_user_name = AuthViewUtils.generateUsername(postfix_length=6, param_initials=initials.upper()) 
        return student_user_name
    
    @classmethod
    def redirectIfBlocked(cls, user, remote_ip, now):
        logger.debug(">>redirectIfBlocked()")
        redirect = False
        isIpForUserBlocked = db.session.query(BlockedIPForUser).filter(BlockedIPForUser.user_id==user.id, BlockedIPForUser.ip4_address==remote_ip).first()
        if isIpForUserBlocked is not None:
            time_difference = now - isIpForUserBlocked.created
            time_difference_in_hrs = time_difference / datetime.timedelta(hours=1)
            if time_difference_in_hrs < LoginConstants.LOGIN_RATE_LIMIT_HR_PERIOD:
                redirect = True
        return redirect
 
    @classmethod
    def nonAuthenticatedLoginAttempt(cls, user, remote_ip, now):
        logger.debug(">>nonAuthenticatedLoginAttempt()")
        valid_login_attempt = AuthViewUtils.checkLoginsWithinTimePeriod(db, user, LoginConstants.LOGIN_RATE_LIMIT_HR_PERIOD, remote_ip, now)
        if not valid_login_attempt:
            blockedIpForUser = BlockedIPForUser(created = now, user_id=user.id, ip4_address=remote_ip)
            db.session.add(blockedIpForUser)
            db.session.commit()
    
    @classmethod      
    def persistFailedLoginAttempt(cls, user, remote_ip, now):
        logger.debug(">>persistFailedLoginAttempt()")
        if user.unsuccessfull_logins_since_success is not None:
            user.unsuccessfull_logins_since_success += 1
        else:
            user.unsuccessfull_logins_since_success = 1
        db.session.commit()
        AuthViewUtils.addFailedLoginAttempt(db, user, remote_ip, now)
    
    @classmethod
    def emailLogin(cls, user_or_email):
        logger.debug(">>emailLogin()")
        email_error = AuthViewUtils.email_firewall(email=user_or_email, check_deliverability=False)
        found_user = None
        if not email_error:
            found_user = db.session.query(User).filter(User.email == user_or_email).first()
        return email_error, found_user
    
    @classmethod  
    def trackSessionOnLogin(cls):
        browser = request.user_agent.browser
        version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
        platform = request.user_agent.platform
        language = request.user_agent.language
        uas = request.user_agent.string
        user_agent = db.session.query(UserAgent).filter(UserAgent.uas == uas).first()
        if user_agent is None:
            user_agent = UserAgent(browser = browser, version = version, platform = platform, language = language, uas = uas)
            db.session.add(user_agent)
            db.session.commit()
        return user_agent.id
    
    @classmethod
    def signUpUser(cls, signup_type, user):
        logger.debug(">>signup() user.id:{0}".format(user.id))
        if signup_type == SignUpConstants.STANDARD:
            logger.debug("--signup() standard signup")
            signup_ammount = 40.00
            flash('We are not quite ready to accept payments.', 'info')
        if signup_type == SignUpConstants.LIMITED_OFFER:
            logger.debug("--signup() limited offer signup")
            signup_ammount = 10.00
            flash('We are not quite ready to accept payments.', 'info')
        else:
            logger.debug("--signup() free signup")
            signup_type = SignUpConstants.FREE
            signup_ammount = 0.00
        time_now = datetime.datetime.now()
        try:
            signup = SignupType(user_id=user.id, signup_type = signup_type, signup_ammount = signup_ammount,
                            signup_date=time_now)
            db.session.add(signup)
            db.session.commit()
            return True
        except exc.SQLAlchemyError as e:
            logger.error("--signUpUser() error commiting data:{0}".format(e))
            return False
        
    @classmethod
    def sendContactFollowupEmail(cls, user, contact_request):
        app = current_app._get_current_object()
        admin_email = app.config['ADMIN_EMAIL']
        email_type = EmailTypes.EMAIL_INTERNAL_CONATCT_REQUEST_PREFIX
        send_email(email_type=email_type, to = admin_email, subject = '', template='auth/email/internal/contact_request_followup', user=user, contact_request=contact_request)

    @classmethod
    def sendSignupEmail(cls, user, signup_type, token):
        subject = 'Thank you for signing up to Maths on Mars'
        email_type = EmailTypes.EMAIL_GENERAL_PREFIX
        send_email(email_type=email_type, to=user.email, subject='Thank you for signing up to Maths on Mars',
                           template='auth/email/signup', user=user, signup_type=signup_type, token=token)
        #note to developers, remove when too active
        email_type = EmailTypes.EMAIL_INTERNAL_SIGNUP
        if signup_type == SignUpConstants.LIMITED_OFFER:
            subject = "Signup: "+SignUpConstants.LIMITED_OFFER
        else:
            subject = "Signup: "+SignUpConstants.FREE
        app = current_app._get_current_object()
        admin_email = app.config['ADMIN_EMAIL']
        send_email(email_type=email_type, to=admin_email, subject=subject,
                           template='auth/email/internal/signup_internal_note', user=user, signup_type=signup_type, token=token)
       
    @classmethod 
    def sendRegistrationSuccessEmail(cls, user, student_first_name, student_last_name, student_user_name, student_pass, token):
        subject = 'Thank you for registering a student with Maths on Mars'
        email_type = EmailTypes.EMAIL_GENERAL_PREFIX
        if user.email is not None:
            send_email(email_type=email_type, to=user.email, subject=subject,
                               template='auth/email/registration_success', user=user, student_first_name=student_first_name, student_last_name=student_last_name, \
                                student_user_name=student_user_name, student_pass=student_pass)
        else:
            logger.warn("--sendRegistrationSuccessEmail() no email address to send to for user.id:{0}".format(user.ud))
    
    @classmethod
    def modifyContactToSignedUp(cls, user, signup_type):
        signuptype = db.session.query(SignupType).filter(SignupType.user_id == user.id).first()
        time_signedup = datetime.datetime.now()
        signuptype.signup_type = signup_type
        user.time_signedup = time_signedup
        signuptype.signup_date = time_signedup
        db.session.add(signuptype)
        db.session.commit()
        
    @classmethod
    def addUserOnSingup(cls, email, signup_type):
        logger.debug(">>addUserOnSingup()")
        time_signedup = datetime.datetime.now()
        role = db.session.query(Role).filter(Role.role_name == RoleTypes.STUDENT).first()
        contact_name = DefaultUserName.PARENT_GUARDIAN_TEACHER
        avatar=ProfileConstants.DEFAULT_AVATAR_NAME
        user = User(contact_name=contact_name, email=email, time_signedup = time_signedup, role_id = role.id, avatar=avatar)
        db.session.add(user)
        db.session.flush()
        pet=ProfileConstants.DEFAULT_PET_NAME
        student = Student(user_id = user.id, level = 2,
                    goal_session_time = 10,
                    goal_session_frequency = 5, pet=pet)
        db.session.add(student)
        signuptype = SignupType(user_id = user.id, signup_type = signup_type, signup_date = time_signedup)
        db.session.add(signuptype)
        db.session.commit()
        return user
    
    @classmethod
    def addCasualUser(cls, email, signup_type):
        logger.debug(">>addCasualUser()")
        time_signedup = datetime.datetime.now()
        role = db.session.query(Role).filter(Role.role_name == RoleTypes.PARENT).first()
        contact_name = DefaultUserName.PARENT_GUARDIAN_TEACHER
        user = User(contact_name=contact_name, email=email, role_id = role.id)
        signuptype = SignupType(user_id = user.id, signup_type = signup_type, signup_date = time_signedup)
        db.session.add(user)
        db.session.add(signuptype)
        db.session.commit()
        return user
    
    @classmethod
    def updatePasswordOnSignupUpgrade(cls, user, form):
        time_signedup = datetime.datetime.now()
        user.password = form.password.data
        user.time_signedup = time_signedup
        db.session.commit()
    
    @classmethod
    def generate_confirmation_token(cls, email):
        timedSerializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        token = timedSerializer.dumps(email, salt=current_app.config['EMAIL_TOKEN_SALT'])
        return token
        
    @classmethod
    def confirm_token(cls, token, expiration=86400):
        #24hr expiration default
        timedSerializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            email = timedSerializer.loads(
                token,
                salt=current_app.config['EMAIL_TOKEN_SALT'],
                max_age=expiration
            )
        except:
            return False
        return email
    
    
    '''
    TODO update to use session tracker
    def checkIfIPUsedBefore(user, request):
        logged_in_before_on_ip = False
        remote_ip = getRemoteAddress(request)
        if remote_ip in user.login_ips:
            logged_in_before_on_ip = True
        return logged_in_before_on_ip
    '''
    
    '''
    @classmethod
    def log_in_user(cls, user_or_email, password ):
        #disable @ character in username so if has @ must be email
        if ('@' in user_or_email):
            found_user = db.session.query(User).filter(User.email == user_or_email).first()
            login_by_email = True
        else:
            #find user in db
            found_user = db.session.query(User).filter(User.user_name == user_or_email).first()
            login_by_email = False
    '''