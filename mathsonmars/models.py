from datetime import datetime, timedelta

from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Boolean, DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship, synonym
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

from werkzeug import check_password_hash, generate_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from mathsonmars.utils.numberutils import NumberUtils
from mathsonmars.marslogger import logger
from mathsonmars.extensions import bcrypt

db = SQLAlchemy()
Base = declarative_base()
db.Model = Base



class User(Base):
    """A user login, with credentials and authentication.
    @param created: auto to default
    @param created: auto to default
    @param user_name: str
    @param first_name: str
    @param last_name: str
    @param email: str
    @param active: bool

    @param _password: str
    """
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer,
                     ForeignKey('role.id'), nullable=False)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    #used in initial contact messaging interest
    contact_name = Column(String(255), nullable=True)
    user_name = Column(String(255), unique=True, nullable=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    #students don't require email
    email = Column(String, unique=True, nullable=True)
    time_signedup = Column(DateTime)
    time_registered = Column(DateTime)
    unsuccessfull_logins_since_success = Column(Integer)
    active = Column(Boolean, default=True)
    confirmed = Column(Boolean, default=False)
    time_confirmed = Column(DateTime)
    avatar = Column(String(), nullable=True)
    #see https://exploreflask.com/users.html
    _password = Column(String(255))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        app = current_app._get_current_object()
        plaintext.encode('utf-8')
        #we want to store as a string not bytes so can always convert back (eg postgresql vs sqlite)
        bytearray = bcrypt.generate_password_hash(plaintext, app.config['BCRYPT_LOG_ROUNDS'])
        self._password = bytearray.decode('utf-8')
        
    def is_correct_password(self, plaintext):
        plaintext.encode('utf-8')
        valid = False
        try:
            bytearray = self._password.encode('utf-8')
            valid = bcrypt.check_password_hash(bytearray, plaintext)
        except ValueError as e:
            logger.error("--is_correct_password Exception:{0}".format(e))
        return valid

    @classmethod
    def authenticate_email(cls, query, email, password):
        email = email.strip().lower()
        user = query(cls).filter(cls.email==email).first()
        if user is None:
            return None, False
        if not user.active:
            return user, False
        return user, user.is_correct_password(password)
    
    @classmethod
    def authenticate_username(cls, query, user_name, password):
        logger.debug(">>authenticate_username()")
        user_name = user_name.strip().lower()
        user = query(cls).filter(cls.user_name==user_name).first()
        if user is None:
            return None, False
        if not user.active:
            return user, False
        return user, user.is_correct_password(password)
    
    '''
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})
    '''
    
    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})
    
    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True

    def generate_email_change_token(self, new_email, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'change_email': self.id, 'new_email': new_email})

    # Hooks for Flask-Login.
    #
    # As methods, these are only valid for User instances, so the
    # authentication will have already happened in the view functions.
    #
    # If you prefer, you can use Flask-Login's UserMixin to get these methods.

    def get_id(self):
        return str(self.id)

    @property
    def is_active(self):
        return self.active

    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True
    
    '''
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True
    '''

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    
class Student(Base):
    '''
    @param parentid: id 
    @param teacherid: id 
    @param age: int
    @param grade: int
    @param level: int
    @param school: str
    @param goal_session_time: int
    @param goal_session_frequency: int
    @param points: int
    '''
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,
                     ForeignKey('user.id'), nullable=False)
    user = relationship(User, lazy='joined', join_depth=1)
    parentid = Column(Integer, nullable=True)
    teacherid = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    #for students only
    grade = Column(Integer, nullable=True)
    #grouping of levels eg Foundation1
    level = Column(Integer)
    school =  Column(String(255), nullable=True)
    country = Column(String(), nullable=True)
    #minutes
    goal_session_time = Column(Integer, nullable=True)
    #once every n days default is 2?
    goal_session_frequency = Column(Integer, nullable=True)
    points = Column(Integer, nullable=True)
    pet = Column(String(), nullable=True)
    
class ContactRequest(Base):
    """contactrequest"""
    __tablename__ = 'contact_request'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,
                     ForeignKey('user.id'), nullable=False)
    time_requested_contact = Column(DateTime)
    subject = Column(String)
    message = Column(String)

class Activity(Base):
    __tablename__ = 'activity'
    id = Column(Integer, primary_key=True)
    #eg NA (ie Numbers and Algebra - look up from other table)
    topic_id = Column(Integer,
                     ForeignKey('topic.id'), nullable=False)
    #order in which this appears in topic - combine with
    topic_progress = Column(Integer)
    #look up from CategoryConstants
    category_id = Column(Integer,
                     ForeignKey('category.id'), nullable=False)
    #eg Fun chunks single single
    strategy_id = Column(Integer,
                     ForeignKey('strategy.id'), nullable=False)
    #eg level2
    level = Column(Integer)
    name = Column(String)
    description = Column(String)
    #stage within this particular topic
    stage = Column(Integer)

    url_name = Column(String)
    time_limit = Column(Integer) 
    total_questions = Column(Integer) 
    num_variables = Column(Integer)
    #eg positive integer
    answer_format = Column(String)
    
class FunChunks(Base):
    __tablename__ = 'funchunks'
    #question section common to all activity implementation 
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    question = Column(String)
    stage1_question = Column(String)
    answer = Column(String)
    #end question section
    #eg line_positions
    line_positions = Column(String)
    #eg jump_values
    jump_values = Column(String)
    #eg flip
    flip = Column(Boolean)
    
class FriendlyAndFix(Base):
    __tablename__ = 'friendlyandfix'
    #question section common to all activity implementation 
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    question = Column(String)
    stage1_question = Column(String)
    answer = Column(String)
    #end question section
    #eg line_positions
    line_positions = Column(String)
    #eg jump_values
    jump_values = Column(String)
    #eg flip
    flip = Column(Boolean)
    
class Memorize(Base):
    __tablename__ = 'memorize'
    #question section common to all activity implementation 
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    variables = Column(Integer)
    #store as string as could be float or int
    var1 = Column(String)
    var2 = Column(String)
    var3 = Column(String)
    operator1 = Column(String)
    operator2 = Column(String)
    
class BoxModelMADS(Base):
    """boxmodelmads"""
    __tablename__ = 'boxmodelmads'

    #question section common to all activity implementation 
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    question = Column(String)
    hint = Column(String)
    answer = Column(String)
    num_variables = Column(Integer)
    total_value = Column(String)
    part_values = Column(String)
    #c=constant, u=unknown,g=group representation
    part_value_types = Column(String)
    part_names = Column(String)
    #csv specifically for mult/divide bob has twice as many balls as ann
    #would be 1, 2 (ie name position 1 have 1 part, position 2 (bob) has 2 parts
    part_name_association = Column(String)
    
class BoxMethod(Base):
    """boxmethod"""
    __tablename__ = 'boxmethod'

    #question section common to all activity implementation 
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    question = Column(String)
    stage1_question = Column(String)
    answer = Column(String)
    num_variables = Column(Integer)
    #end question section
    
    variable_constraint_type = Column(String)
    constant_positions = Column(String)
    variable_values = Column(String)
    object_values = Column(String)
    owner_values = Column(String)
    text_values = Column(String)
    model_format = Column(String)
    
class NumberBonds(Base):
    """numberbonds"""
    __tablename__ = 'numberbonds'
    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    #counters, part-part, whole-part
    numberbond_type = String()
    whole = Column(String)
    part1 = Column(String)
    part2 = Column(String)
    
class SignupType(Base):
    """signuptype"""
    __tablename__ = 'signuptype'
    '''Includes contact requests'''
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,
                     ForeignKey('user.id'), nullable=False)
    signup_type = Column(String)
    signup_ammount = Column(String)
    signup_date = Column(DateTime)

    
class Topic(Base):
    """topic"""
    __tablename__ = 'topic'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    order = Column(Integer)
    
class Category(Base):
    """category"""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey('topic.id'), nullable=False)
    name = Column(String)
    order = Column(Integer)

class Strategy(Base):
    """strategy"""
    __tablename__ = 'strategy'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    qualifier = Column(String)
    description = Column(String)
    #csv list of examples
    examples = Column(String)
    
class Completed(Base):
    """record of activity completion"""
    __tablename__ = 'completed'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #dont use foreign key as too hard to drop activities
    activity_id = Column(Integer)
    time_completed = Column(DateTime)
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)

class Results(Base):
    """record of results of activities"""
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    session_tracker_id = Column(Integer, ForeignKey('user_session_tracker.id'))
    #seconds
    time_spent = Column(Float)
    #dont use activity foreign key as too hard to drop activity
    activity_id = Column(Integer)
    table_name = Column(String)
    #id of question within table above
    question_id = Column(Integer)
    correct = Column(Boolean)
    hint = Column(Boolean)
    help = Column(Boolean)
    time_completed = Column(DateTime)
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
   
class Role(Base):
    '''
    @param role: str eg student/parent/teacher
    '''
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    'eg admin, parent, teacher, student, contact'
    role_name = Column(String, unique=True)
 
class FailedLoginAttempt(Base):
    __tablename__ = 'failed_login_attempt'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    ip4_address = Column(String(45))
    
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    
class BlockedIPForUser(Base):
    __tablename__ = 'blocked_ip_for_user'
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    ip4_address = Column(String(45))

    
#use google analytics for general tracking, here for logins only
class UserSessionTracker(Base):
    """web tracking."""
    __tablename__ = 'user_session_tracker'

    id = Column(Integer, primary_key=True)
    #max IPV6 is 39 but IPV4 mapped to IPV6 is 45 bytes
    ip = Column(String(45)) 
    user_agent_id = Column(Integer,
                     ForeignKey('user_agent.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #login
    login = Column(DateTime, nullable=False)
    #logout or close
    logout = Column(DateTime, nullable=True)
    #closed due to inactivity, logged out, closed browser
    logout_type = Column(String)
    
    @property
    def duration(self):
        duration = 0.0
        if self.completed is not None:
            delta = self.logout - self.login
            duration = delta.days * 24 * 60 * 60 + delta.seconds
        return duration

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    

    
class UserAgent(Base):
    """Search for matches before inserting new one, limited to 256 chars"""
    __tablename__ = 'user_agent'

    id = Column(Integer, primary_key=True)
    browser = Column(String(255))
    version = Column(String(255))
    platform = Column(String(255))
    language = Column(String(255))
    uas = Column(String(255))
    
class Payment(Base):
    """Payments."""
    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    #student user ids
    student_ids_csv = Column(String) 
    payment_date = Column(DateTime, nullable=False)
    expiry_date = Column(DateTime, nullable=True)
    #AUD
    ammount = Column(Float)
    #marketing offer
    discount_code = Column(String, nullable=True)

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    
'''
class LegacyActivity(Base):
    """A maths activity eg Addition activity - Two numbers 1 to 3.
    @param id:
    @param topic: str
    @param category: str
    @param strategy_id: int
    @param name: str
    @param level: int
    @param activity_action_id: int
    @param time_limit: int
    @param total_questions: int
    """
    __tablename__ = 'legacyactivity'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    strategy_id = Column(Integer, ForeignKey('strategy.id'), nullable=False)
    level = Column(Integer) 
    level_progress = Column(Integer)
    #used so that can query
    activity_stage = Column(Integer) 
    name = Column(String)
    url_name = Column(String)
    time_limit = Column(Integer) 
    total_questions = Column(Integer) 
    answer_format = Column(String)
    #deprecated
    activity_action_id = Column(Integer)
    #deprecated
    activity_action_type = Column(String)
    
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)  
'''

'''
class MadsActivity(Base):
    """madsactivity
    @param num_values: int
    @param value_mins: str
    @param value_maxs: str
    @param multiple_ofs: str
    @param constraint_type: str
    @param constraint_value: str
    @param constraint_value_type: str
    """
    __tablename__ = 'madsactivity'


    id = Column(Integer, primary_key=True)
    #number of variables
    num_variables = Column(Integer) 
    #csv of min value for each number
    value_mins = Column(String) 
    #csv of max value for each number
    value_maxs = Column(String)
    #csv of multiple of for each number
    multiple_ofs = Column(String)
    #eg AddToMaxOf (numbers add to a maxium of)
    constraint_type = Column(String)
    #eg 100
    constraint_value = Column(String)
    #eg int, float
    constraint_value_type = Column(String)
    #eg for 12 + 3 = 15 if value = 0 = first, if 2 then to answer
    value_positions_to_apply_contraint_on = Column(String) 
    
    def getMinValuesStr(self):
        return [x.strip() for x in self.value_mins.split(',')]
    
    def getMinValues(self):
        numberStrList = self.getMinValuesStr()
        return self.getValuesFromStringList(numberStrList)
        
    def getMaxValuesStr(self):
        return [x.strip() for x in self.value_maxs.split(',')]
    
    def getMaxValues(self):
        numberStrList = self.getMaxValuesStr()
        return self.getValuesFromStringList(numberStrList)
    
    def getValuesFromStringList(self, numberStrList):
        numbers = []
        for val in numberStrList:
            if NumberUtils.isInt(val):
                result = int(val)
                numbers.append(result)
            elif NumberUtils.isFloat(val):
                result = float(val)
                numbers.append(result)
            else:
                'TODO log this, it should never happen'
                numbers.append(0)
                
    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    


class Question(Base):
    """question"""
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    answer_id = Column(Integer, ForeignKey('answer.id'), nullable=False)
    value_ids = Column(String)
    operator_ids = Column(String)
    
class Operator(Base):
    """operator"""
    __tablename__ = 'operator'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    name = Column(String)
    operator_position = Column(Integer)
    
class Value(Base):
    """value"""
    __tablename__ = 'value'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    #int, float, or fraction as a string
    value_type = Column(String)
    value = Column(String)
    value_position = Column(Integer)
    
class Answer(Base):
    """answer"""
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    #false = floats
    values_integer = Column(Boolean)
    #number of values
    values_number = Column(Boolean)
    value_ids = Column(String)
    value_ids = Column(String)
    operator_ids = Column(String)

    def __repr__(self):
        return u'<{self.__class__.__name__}: {self.id}>'.format(self=self)
    
class Power(Base):
    """power"""
    __tablename__ = 'power'

    id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activity.id'), nullable=False)
    #int, float, or fraction as a string
    power_type = Column(String)
    power = Column(String)
    #position of value operating on
    value_position = Column(Integer)
'''