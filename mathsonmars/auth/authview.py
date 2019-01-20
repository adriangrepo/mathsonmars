import datetime
from flask import current_app, g, flash, Markup, redirect, render_template, request, session, url_for , make_response
from flask.ext.login import LoginManager, current_user, login_user, login_required, logout_user
from werkzeug.exceptions import HTTPException
from sqlalchemy import desc, exc
from itsdangerous import URLSafeTimedSerializer

from mathsonmars.marslogger import logger
from mathsonmars.auth.authforms import LoginForm, SignupForm, ContactForm,\
    RegisterForm, PasswordResetRequestForm, ChangePasswordForm,\
    PasswordResetForm, ChangeEmailForm, NewUserForm

from mathsonmars.models import db, User, Role, Student,\
    ContactRequest, BlockedIPForUser, SignupType, UserAgent,\
    UserSessionTracker
from mathsonmars.constants.modelconstants import RoleTypes, DefaultUserName,\
    EmailTypes, LoginConstants, SignUpConstants
from mathsonmars.email import send_email
from mathsonmars.auth import auth_view
from sqlalchemy.sql.functions import now
from mathsonmars.utils.numberutils import NumberUtils
from mathsonmars.auth.authviewutils import AuthViewUtils
from mathsonmars.constants.userconstants import ProfileConstants

login_manager = LoginManager()
login_manager.login_view = "auth_view.login"
login_manager.login_message_category = "warning"

@auth_view.before_request
def before_request():
    g.user = current_user

@login_manager.user_loader
def load_user(userid):
    return db.session.query(User).get(userid)

@auth_view.route('/unconfirmed')
def unconfirmed():
    if current_user is not None:
        if current_user.is_anonymous or current_user.confirmed:
            return redirect(url_for('main_view.index'))
    return render_template('auth/unconfirmed.html')

@auth_view.route("/login", methods=["GET", "POST"])
def login():
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--login remote_ip:{0}".format(remote_ip))

    if current_user is not None and current_user.is_authenticated:
        flash("Already logged in.", 'info')
        return redirect(url_for('main_view.index'))
    try:
        form = LoginForm(request.form)
        error = None
        incorrect_login_msg = 'Incorrect email/username or password. Please try again.'
        if form.validate_on_submit():
            user_or_email = form.login_field.data.lower().strip()
            password = form.password.data.strip()
            #disable @ character in username so if has @ must be email
            if ('@' in user_or_email):
                logger.debug("--login trying email login")
                email_error, found_user = AuthViewUtils.emailLogin(user_or_email)
                if email_error:
                    form.login_field.errors.append(incorrect_login_msg)
                    return render_template('auth/login.html', form=form, error=error)
                else:
                    login_by_email = True
            else:
                #find user in db
                found_user = db.session.query(User).filter(User.user_name == user_or_email).first()
                login_by_email = False
            if found_user is not None:
                logger.debug("--login found_user not None")
                now = datetime.datetime.now()
                if AuthViewUtils.redirectIfBlocked(found_user, remote_ip, now):
                    logger.debug("--login redirectIfBlocked is true")
                    #within 24hrs, no login
                    flash(incorrect_login_msg, 'warn')
                    return render_template('auth/login.html', form=form, error=error)
                if AuthViewUtils.timeDeltaValid(db, found_user, LoginConstants.LOGIN_RATE_LIMIT_SECS, remote_ip):
                    authenticated = False
                    if login_by_email:
                        user, authenticated = \
                            User.authenticate_email(db.session.query, user_or_email, password)
                    else:
                        user, authenticated = \
                            User.authenticate_username(db.session.query, user_or_email, password)
                    if authenticated:
                        login_user(user)
                        createUserSessionTracker(user)
                        #user_session_tracker_id = createUserSessionTracker()
                        flash('Logged in successfully.', 'info')
                        role = db.session.query(Role).filter(Role.id == user.role_id).first()
                        logger.debug("--login() authenticated and logged in, role.role_name:{0}".format(role.role_name))
                        if role.role_name == RoleTypes.STUDENT:
                            logger.debug("--redirectIfAuthenticated() STUDENT")
                            student = db.session.query(Student).filter(Student.user_id == user.id).first()
                            #return redirect(url_for('appl_view.level', level_value=student.level))
                            return redirect(url_for('appl_view.student_home'))
                        elif role.role_name == RoleTypes.PARENT or role.role_name == RoleTypes.GUARDIAN or role.role_name == RoleTypes.TEACHER:
                            logger.debug("--login() role.role_name:{0} request.args.get('next'):{1}".format(role.role_name, request.args.get('next')))
                            return redirect(request.args.get('next') or url_for('report_view.report', user=user,role=role))
                        elif role.role_name == RoleTypes.ADMIN:
                            return redirect(url_for('report_view.report', user=user,role=role))
                    else:
                        AuthViewUtils.persistFailedLoginAttempt(user, remote_ip, now)
                        AuthViewUtils.nonAuthenticatedLoginAttempt(user, remote_ip, now)
                        flash(incorrect_login_msg, 'warn')
                else:
                    AuthViewUtils.persistFailedLoginAttempt(user, remote_ip, now)
                    flash(incorrect_login_msg, 'warn')
            else:
                flash(incorrect_login_msg, 'warn')
                logger.warn("--login no user found login:{0} remote_ip:{1}".format(user_or_email, remote_ip))
    except Exception as e:
        logger.error("--login() error: {0}".format(e))
    return render_template('auth/login.html', form=form, error=error)
  
@auth_view.route("/logout")
@login_required
def logout():
    try:
        db.session.query(UserSessionTracker).filter(UserSessionTracker.user_id == current_user.id).update({'logout': db.func.current_timestamp()}, synchronize_session=False)
        db.session.commit()
    except AttributeError as e:
        logger.debug(">>logout() error:{0}".format(e))
    logged_out = logout_user()

    #clear_messages("logout")
    flash("You have been logged out.", "success")
    return redirect(url_for("main_view.index"))

@auth_view.route("/restricted")
@login_required
def restricted():
    logger.debug(">>restricted")
    return "You can only see this if you are logged in!", 200
   
@auth_view.route('/contact', methods=['GET', 'POST'])
def contact():
    logger.debug(">>contact()")
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--contact remote_ip:{0}".format(remote_ip))
    form = ContactForm(request.form)
    if form.validate_on_submit():
        msg_sent = 'Thank you for contacting us. We will get back to you shortly.'
        if (request.headers['Content-Type'].startswith('application/x-www-form-urlencoded')):
            post_data = list(request.form.keys())
            if all(x in ['nameblank', 'nochange'] for x in post_data):
                nameblank_index = post_data.index("nameblank")
                nochange_index = post_data.index("nochange")
                test_string = post_data[nameblank_index]+post_data[nochange_index]
                if test_string is not "http://www.mathsonmars.com":
                    #spambot
                    logger.warn("--contact() spambot post remote_ip:{0}".format(remote_ip))
                    flash('Thank you for contacting us. We will get back to you shortly.')
                    return redirect(url_for('main_view.index'))
        else:
            logger.debug("--contact() request.headers['Content-Type']:{0}".format(request.headers['Content-Type']))
            #incorrect header type - hacker?
            flash(msg_sent)
            return render_template('auth/contact.html', form=form)
        #if got here is not dumb spambot
        #check for smart spambot url links in message
        message_text = form.message.data
        page_array = AuthViewUtils.getLinksInText(message_text)
        no_message_urls = AuthViewUtils.isEmpty(page_array)
        if no_message_urls:
            email = form.email.data.strip()
            email_error = AuthViewUtils.email_firewall(email, True)
            if email_error:
                flash('Email address error, please try again.')
                return render_template('auth/contact.html', form=form, error=email_error)
            #find user in db
            user = db.session.query(User).filter(User.email == email).first()
            time_requested_contact = datetime.datetime.now()
            if user is None:
                role = db.session.query(Role).filter(Role.role_name == RoleTypes.CONTACT).first() 
                user = User(email = email, 
                            contact_name=form.name.data, 
                            role_id = role.id)
                db.session.add(user)
                db.session.commit()
                logger.debug("--contact() user added: {0}".format(form.name.data))
            contact_request = ContactRequest(user_id = user.id, time_requested_contact = time_requested_contact, subject = form.subject.data, message = form.message.data)
            db.session.add(contact_request)
            db.session.commit()
            AuthViewUtils.sendContactFollowupEmail(user, contact_request)
            flash(msg_sent)
        else:
            flash('No URL links are permitted in messages, please remove the links and re-submit.')
            return render_template('auth/contact.html', form=form)
    return render_template('auth/contact.html', form=form)

@auth_view.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    logger.debug(">>register() current_user.email: {0}".format(current_user.email))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        logger.debug("--register() form data is OK")
        found_user = db.session.query(User).filter(User.id == current_user.id).first()
        logger.debug("--register() found_user.id:{0}, found_user.user_name:{1}, found_user.first_name:{2}".format(found_user.id, found_user.user_name, found_user.first_name))
        found_user.first_name=form.first_name.data
        found_user.last_name=form.last_name.data
        student_role = db.session.query(Role).filter(Role.role_name == RoleTypes.STUDENT).first()
        student_pass = AuthViewUtils.generateWeakPass(pass_length=6)
        current_time = datetime.datetime.now()
        student_user_name = AuthViewUtils.createUniqueUsername(student_role, form.student_first_name.data, form.student_last_name.data)
        student_user = User(role_id = student_role.id, user_name=student_user_name, first_name=form.student_first_name.data, \
                                last_name=form.student_last_name.data, time_registered=current_time, avatar=ProfileConstants.DEFAULT_AVATAR_NAME, \
                                password=student_pass)
        db.session.add(student_user)
        db.session.flush()
        #default
        grade = 1
        if (NumberUtils.representsInt(form.student_grade.data)):
            grade = NumberUtils.convertToInt(form.student_grade.data)
            db.session.commit()
        student = Student(user_id = student_user.id, parentid = current_user.id, grade=grade, pet=ProfileConstants.DEFAULT_PET_NAME)
        try:
            db.session.add(student)
            db.session.flush()
            db.session.commit()
            logger.debug("--register() sending sendRegistrationSuccessEmail")
            AuthViewUtils.sendRegistrationSuccessEmail(found_user, student_user.first_name, student_user.last_name, student_user_name, student_pass)
        except exc.SQLAlchemyError as e:
            logger.error("--register() error commiting data:{0}".format(e))
            return redirect(url_for('auth_view.contact', error = 'There has been an error processing your registration request. Please contact us to report this', signup_type = 'free'))
        logger.debug("--register() returning auth/register_success.html")
        return render_template('auth/register_success.html', form=form, email=current_user.email)
    return render_template('auth/register.html', form=form, email=current_user.email)

@auth_view.route('/signup/<string:signup_type>', methods=['GET', 'POST'])
def signup(signup_type):
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--signup remote_ip:{0}, signup_type:{1}".format(remote_ip, signup_type))
    form = SignupForm(request.form)
    if form.validate_on_submit():
        email = form.email.data.strip()
        #find user in db
        found_user = db.session.query(User).filter(User.email == email).first()
        if found_user is None:
            new_user = AuthViewUtils.addUserOnSingup(email, signup_type)
            user = new_user
            token = AuthViewUtils.generate_confirmation_token(email)
            AuthViewUtils.sendSignupEmail(user=user, signup_type=signup_type, token=token)
            flash('Thank you for signing up to Maths on Mars', 'success')
            return render_template('auth/signup_success.html', signup_type = signup_type)
        else:
            signup_type = db.session.query(SignupType).filter(SignupType.user_id == found_user.id).first()
            user = found_user
            token = AuthViewUtils.generate_confirmation_token(email)
            if signup_type.signup_type == SignUpConstants.CONTACT:
                #update role to signed up
                AuthViewUtils.modifyContactToSignedUp(found_user, signup_type)
                AuthViewUtils.sendSignupEmail(found_user, signup_type, token)
                flash('Thank you for signing up to Maths on Mars', 'success')
                return render_template('auth/signup_success.html', signup_type = signup_type)
            else:
                flash('You have already signed up to Maths on Mars', 'success')
                return redirect(url_for('auth_view.login'))
                
    if signup_type == SignUpConstants.STANDARD:
        flash('Thank you for showing interest in our annual subscription. At the moment we only have free access', 'success')
        return render_template('auth/signup_free.html', form=form) 
    elif signup_type == SignUpConstants.LIMITED_OFFER:
        flash('Thank you for showing interest in our limited time offer. At the moment we only have free access', 'success')
        return render_template('auth/signup_free.html', form=form) 
    else:
        return render_template('auth/signup_free.html', form=form)

@auth_view.route('/confirm/<token>')
def confirm(token):
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--confirm remote_ip:{0}".format(remote_ip))
    try:
        email = AuthViewUtils.confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    user = db.session.query(User).filter(User.email == email).first()
    if user is not None:
        if user.confirmed:
            flash('Account already confirmed. Please login.', 'success')
        else:
            user.confirmed = True
            user.time_confirmed = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            #should we login user here?
            login_user(user)
            createUserSessionTracker(user)
            return redirect(url_for('auth_view.confirmed_create_login'))
    else:
        flash('Invalid confirmation link, please contact us.', 'danger')
    return redirect(url_for('main_view.index'))

@auth_view.route('/confirmed_create_login/', methods=['GET', 'POST'])
@login_required
def confirmed_create_login():
    logger.debug(">>confirmed_create_login() current_user.email: {0}".format(current_user.email))
    form = NewUserForm(request.form)
    if form.validate_on_submit():
        logger.debug("--confirmed_create_login() form data is OK")
        existing_user = db.session.query(User).filter(User.user_name == form.user_name.data).first()
        if existing_user:
            flash('A user with that name already exists, please try another name', 'warn')
            return redirect(url_for('auth_view.confirmed_create_login'))
        else:
            current_user.user_name = form.user_name.data
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
        return render_template('auth/register_success.html', form=form, email=current_user.email)
    return render_template('auth/confirmed_create_login.html', form=form)

@auth_view.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    logger.debug(">>change_password()")
    form = ChangePasswordForm()
    if form.validate_on_submit(request.form):
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            flash('Your password has been updated.')
            return redirect(url_for('main_view.index'))
        else:
            flash('Invalid password.')
    return render_template("auth/change_password.html", form=form)

@auth_view.route('/password_reset_request', methods=['GET', 'POST'])
def password_reset_request():
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--password_reset_request remote_ip:{0}".format(remote_ip))
    if not current_user.is_anonymous:
        return redirect(url_for('main_view.index'))
    form = PasswordResetRequestForm(request.form)
    if form.validate_on_submit():
        email=form.email.data
        email_error = AuthViewUtils.email_firewall(email, True)
        invalid_email = "Email is not valid, please try again."
        if email_error:
            logger.warn("--password_reset_request() email_error email:{0}, remote_ip:{1}".format(email, remote_ip))
            flash(invalid_email)
            return render_template('auth/reset_password_request.html', form=form, error=invalid_email)
        user = db.session.query(User).filter(User.email == email).first()
        if user:
            token = user.generate_reset_token()
            email_type = EmailTypes.EMAIL_RESET_PASSWORD
            #email_type, to, subject, template
            send_email(email_type=email_type, to=user.email, subject='Reset Your Password',
                       template='auth/email/reset_password', user=user, token=token,
                       next=request.args.get('next'))
            flash('An email with instructions to reset your password has been '
              'sent to you.')
        else:
            logger.warn("--password_reset_request() valid email but no user email:{0}, remote_ip:{1}".format(email, remote_ip))
            flash(invalid_email)
    return render_template('auth/reset_password_request.html', form=form)


@auth_view.route('/password_reset/<token>', methods=['GET', 'POST'])
def password_reset(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main_view.index'))
    form = PasswordResetForm(request.form)
    if form.validate_on_submit():
        email=form.email.data
        email_error = AuthViewUtils.email_firewall(email, True)
        if email_error:
            return render_template('auth/reset_password.html', form=form, error="Email is not valid, please try again.")
        user = db.session.query(User).filter(User.email == email).first()
        if user is None:
            return redirect(url_for('main_view.index'))
        if user.reset_password(token, form.password.data):
            flash('Your password has been updated.')
            return redirect(url_for('auth_view.login'))
        else:
            return redirect(url_for('main_view.index'))
    return render_template('auth/reset_password.html', form=form)


@auth_view.route('/change_email', methods=['GET', 'POST'])
@login_required
def change_email_request():
    logger.debug(">>change_email_request()")
    form = ChangeEmailForm(request.form)
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            new_email = form.email.data
            email_error = AuthViewUtils.email_firewall(new_email, True)
            if email_error:
                return render_template('auth/change_email.html', form=form, error="New email address is not valid, please try again.")
        
            token = current_user.generate_email_change_token(new_email)
            send_email(new_email, 'Confirm your email address',
                       'auth/email/change_email',
                       user=current_user, token=token)
            flash('An email with instructions to confirm your new email '
                  'address has been sent to you.')
            return redirect(url_for('main_view.index'))
        else:
            flash('Invalid email or password.')
    return render_template("auth/change_email.html", form=form)

@auth_view.route('/change_email/<token>')
@login_required
def change_email(token):
    logger.debug(">>change_email()")
    if current_user.change_email(token):
        flash('Your email address has been updated.')
    else:
        flash('Invalid request.')
    return redirect(url_for('main_view.index'))

def error_handler(error):
    msg = "Request resulted in {}".format(error)
    logger.warning(msg, exc_info=error)

    if isinstance(error, HTTPException):
        description = error.get_description(request.environ)
        code = error.code
        name = error.name
    else:
        description = ("We encountered an error "
                       "while trying to fulfill your request")
        code = 500
        name = 'Internal Server Error'

    # Flask supports looking up multiple templates and rendering the first
    # one it finds.  This will let us create specific error pages
    # for errors where we can provide the user some additional help.
    # (Like a 404, for example).
    templates_to_try = ['errors/{}.html'.format(code), 'errors/generic.html']
    return render_template(templates_to_try,
                           code=code,
                           name=Markup(name),
                           description=Markup(description),
                           error=error)


@auth_view.route('/settings')
@login_required
def settings():
    '''User settings - eg student points, avatar'''
    flash('User settings have not yet been implemented', 'info')
    return redirect(url_for('main_view.index'))

# a route for generating sitemap.xml
@auth_view.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Generate sitemap.xml. Makes a list of urls and date modified."""
    pages=[]
    ten_days_ago=datetime.datetime.now() - datetime.timedelta(days=10)
    # static pages
    for rule in current_app.url_map.iter_rules():
        if "GET" in rule.methods and len(rule.arguments)==0:
            pages.append(
                         [rule.rule,ten_days_ago]
                         )
    sitemap_xml = render_template('frontend/sitemap_template.xml', pages=pages)
    response= make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"    
    return response

def createUserSessionTracker(user):
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    user_agent_id = AuthViewUtils.trackSessionOnLogin()
    user_session_tracker = UserSessionTracker(ip = remote_ip, user_agent_id = user_agent_id, user_id = user.id, login = db.func.current_timestamp())
    db.session.add(user_session_tracker)
    db.session.commit()
    return user_session_tracker.id

'''
#signup with password - revised
@auth_view.route('/signup/<string:signup_type>', methods=['GET', 'POST'])
def signup(signup_type):
    logger.debug(">>signup()")
    remote_ip = AuthViewUtils.getRemoteAddress(request)
    logger.debug("--signup remote_ip:{0}, signup_type:{1}".format(remote_ip, signup_type))
    form = SignupForm(request.form)
    if form.validate_on_submit():
        email = form.email.data.strip()
        #find user in db
        found_user = db.session.query(User).filter(User.email == email).first()
        if found_user is None:
            new_user = addUserOnSingup(email, form.password.data)
            user = new_user
            token = generate_confirmation_token(email)
            sendSignupEmail(user=user, signup_type=signup_type, token=token)
            flash('Thank you for signing up to Maths on Mars', 'success')

            if signup_type == SignUpConstants.LIMITED_OFFER:
                return render_template('auth/signup_limited_success.html')
            elif signup_type == SignUpConstants.STANDARD:
                return render_template('auth/signup_standard_success.html')
            else:
                #free for all other cases
                return render_template('auth/signup_free_success.html')
        else:
            signup_type = db.session.query(SignupType).filter(SignupType.user_id == found_user.id).first()
            user = found_user
            token = user.generate_confirmation_token()
            if signup_type.signup_type == LeadTypes.CONTACT:
                #update role to signed up
                modifyContactToSignedUp(found_user)
                sendSignupEmail(found_user, signup_type, token)
                flash('Thank you for signing up to Maths on Mars', 'success')
                return render_template('auth/signup_free_success.html')
            elif signup_type.signup_type == LeadTypes.SIGNUP:
                #user already signed up, check signup_type
                signedup_type = db.session.query(SignupType).filter(SignupType.user_id == found_user.id).all()
                already_used_offer = False
                already_signed_up_standard = False
                already_signed_up_free = True
                if signedup_type is not None:
                    for signup in signedup_type:
                        if signup.signup_type == SignUpConstants.LIMITED_OFFER:
                            already_used_offer = True
                        elif signup.signup_type == SignUpConstants.STANDARD:
                            already_signed_up_standard = True
                        elif signup.signup_type == SignUpConstants.FREE:
                            already_signed_up_free = True
                    if already_used_offer:
                        #signing up for offer again, dont write to DB
                        logger.debug("--signup() already_used_offer")
                        flash('You have already signed-up to the limited time offer with Maths on Mars', 'info')
                        return render_template('auth/signup_limited_success.html')
                    elif already_signed_up_standard:
                        #signing up for offer again, dont write to DB
                        logger.debug("--signup() already_signed_up")
                        flash('You have already signed-up to Maths on Mars', 'info')
                        return render_template('auth/signup_standard_success.html')
                    elif already_signed_up_free:
                        if signup_type != SignUpConstants.LIMITED_OFFER:
                            #upgrading
                            logger.debug("--signup() upgrading from free to paid")
                            updatePasswordOnSignupUpgrade(user, form)
                            #user upgraded their signup from free to paid
                            sendSignupEmail(found_user, signup_type, token)
                            return render_template('auth/signup_limited_success.html')
                        elif signup_type != SignUpConstants.STANDARD:
                            updatePasswordOnSignupUpgrade(user, form)
                            sendSignupEmail(found_user, signup_type, token)
                            return render_template('auth/signup_standard_success.html')
                        else:
                            logger.debug("--signup() already signed up for free")
                            flash('You have already signed-up to Maths on Mars', 'info')
                            return render_template('auth/signup_free_success.html')
    if signup_type == SignUpConstants.STANDARD:
        return render_template('auth/signup_standard.html', form=form) 
    elif signup_type == SignUpConstants.LIMITED_OFFER:
        return render_template('auth/signup_limited.html', form=form) 
    else:
        return render_template('auth/signup_free.html', form=form)
'''

'''
TODO
@auth_view.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.', 'info')
    return redirect(url_for('main_view.index'))
'''

'''
@auth_view.route('/confirm/<token>')
@login_required
def confirm(token):
    logger.debug(">>confirm()")
    if current_user.confirmed:
        return redirect(url_for('main_view.index'))
    if current_user.confirm(token):
        return redirect(url_for('auth_view.register'))
        flash('Please register a student for Maths on Mars', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'warning')
    return redirect(url_for('main_view.index'))
'''

'''     
@auth_view.route('/register', methods=['GET', 'POST'])
def register():
    remote_ip = getRemoteAddress(request)
    logger.debug("--register remote_ip:{0}".format(remote_ip))
    form = RegisterForm(request.form)
    confirmation_sent = "A confirmation request has been sent to your email address."
    if form.validate_on_submit():
        logger.debug("--register() validate_on_submit")
        
        email = form.email.data
        email_error = email_firewall(email, True)
        if email_error:
            logger.debug("--register() email_error")
            return render_template('auth/register.html', form=form, error=email_error)
        
        #find user in db
        user = db.session.query(User).filter(User.email == email).first()
        logger.debug("--register() found_user:".format(user))
        if user is None:
            role = db.session.query(Role).filter(Role.role_name == form.role.data).first() 
            user = User(role_id = role.id, first_name = form.first_name.data, last_name = form.last_name.data, email=email,
                        password=form.password.data)
            db.session.add(user)
            db.session.commit()
        token = user.generate_confirmation_token()
        #send an email that have registered OK
        sendRegistrationEmail(user, form.student_number)
        flash(confirmation_sent)
        return redirect(url_for('auth_view.login'))
    else:
        logger.debug("--register() invalid form")
    return render_template('auth/register.html', form=form)

    
def sendRegistrationEmail(user, time_created, learning_difficulty, dyslexia, software, feature, why_interested, grades):

    send_email(user.email, 'Thank you for registering {0} students with Maths on Mars'.format(n_students),               
                       'auth/email/signup', user=user, token=token)
'''  

'''
def clear_messages(current_page):
    #clear messages if comming from another page
    referering_page = request.referrer
    logger.debug("--clear_messages() referer:{0}, current:{1}".format(referering_page, current_page))
    
    if referering_page is not None:
        if not referering_page.endswith(current_page):
            session.pop('_flashes', None)
    else:
        session.pop('_flashes', None)
'''