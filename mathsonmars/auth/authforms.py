from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, RadioField, TextAreaField, ValidationError
from wtforms.validators import Length, InputRequired, EqualTo, Optional, Length, Email
from wtforms.fields import HiddenField, SelectField

from mathsonmars.models import User, db
from wtforms.fields.simple import SubmitField
from wtforms.fields.core import StringField
from mathsonmars.constants.modelconstants import RoleTypes, ValueConstants

from mathsonmars.marslogger import logger
from mathsonmars.auth.authviewutils import AuthViewUtils

## Trap for spambots
# ensure field is empty, if anything passed here
# whole form is spam one
def emptypot(form, field):
    if field.data:
        raise ValidationError("spambot")
    
def emailCheck(form, field):
    email = field.data.strip()
    email_error = AuthViewUtils.email_firewall(email, True)
    if(email_error):
        raise ValidationError('Cannot deliver email to this address.')
    
def checkPasswordIsComplexEnough(form, field):
    if AuthViewUtils.passwordIsTooSimple(field.data):
        raise ValidationError('Password must contain at least one letter and one number.')

def checkPasswordIsNotCommon(form, field):
    if AuthViewUtils.passwordIsCommon(field.data):
        raise ValidationError('Password too easy to guess, please extend and or add special characters.')

class LoginForm(Form):
    login_field = TextField(u'Username/Email', validators=[InputRequired()])
    password = PasswordField(u'Password', validators=[InputRequired()])

    def validate(self):
        '''String length etc validation, no db hit/email domain validation'''
        logger.debug("--validate()")
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False
        #user can login with either username or email - test for which
        user_or_email = self.login_field.data.lower().strip()
        password = self.password.data.strip()
        #validate password length here as don't want to let public know the min/max
        if (len(password)< ValueConstants.MIN_PASSWORD_LENGTH) or (len(user_or_email) > ValueConstants.MAX_PASSWORD_LENGTH):
            self.login_field.errors.append('Incorrect email/username or password. Please try again.')
            return False
        if ('@' in user_or_email):
            #email to login
            if (len(user_or_email)< ValueConstants.MIN_EMAIL_LENGTH) or (len(user_or_email)> ValueConstants.MAX_EMAIL_LENGTH):
                self.login_field.errors.append('Incorrect email/username or password. Please try again.')
                return False
        else:
            #username
            if (len(user_or_email)< ValueConstants.MIN_USERNAME_LENGTH) or (len(user_or_email)> ValueConstants.MAX_USERNAME_LENGTH):
                self.login_field.errors.append('Incorrect email/username or password. Please try again.')
                return False
        return True


class RegisterForm(Form):
    first_name = TextField('First name', validators=[
            InputRequired(message=(u'Please provide a first name'))
            ])
    
    last_name = TextField('Last name', validators=[
            InputRequired(message=(u'Please provide a last (family) name'))
            ])
    
    student_first_name = TextField('Student first name', validators=[
            InputRequired(message=(u'Please provide a first name'))
            ])
    student_last_name = TextField('Student last name', validators=[
            InputRequired(message=(u'Please provide a last (family) name'))
            ])
    student_grade = SelectField(label = 'Student school grade', choices = [('1','Grade 1'), ('2','Grade 2'), ('3','Grade 3'), ('4','Grade 4'), ('5','Grade 5'), ('6','Grade 6')], default=('1','Grade 1'))
        
class ContactForm(Form):
    name = TextField('Name', validators=[
            InputRequired('Please provide a name'),
            Length(min=1, message=(u'Name is too short')),
            InputRequired(message=(u'That\'s not a valid name.'))
            ])
    email = TextField('Email address', validators=[
            InputRequired('Please provide an email address'),
            Length(min=ValueConstants.MIN_EMAIL_LENGTH, max=ValueConstants.MAX_EMAIL_LENGTH, message=(u'Email address length is invalid')),
            Email(message=(u'Email address is invalid.'))
            ])
    subject = TextField("Subject",  [InputRequired("Please enter a subject.")])
    message = TextAreaField("Message",  [InputRequired("Please enter a message.")])
    
class SignupForm(Form):
    
    email = TextField('Email address', validators=[
            InputRequired('Please provide an email address'),
            Length(min=ValueConstants.MIN_EMAIL_LENGTH, max=ValueConstants.MAX_EMAIL_LENGTH, message=(u'Email address length is invalid')),
            Email(message=(u'Email address is invalid.')), emailCheck])
    
class NewUserForm(Form):
    user_name = TextField('Create you user name', validators=[
            InputRequired(message=(u'Please create a new user name'))
            ])
    
    password = PasswordField('Password', validators=[
            InputRequired('Please provide a valid password'),
            Length(min=ValueConstants.MIN_PASSWORD_LENGTH, max=ValueConstants.MAX_PASSWORD_LENGTH, message=(u'Password must be a minimum of 6 characters'))
            , EqualTo('confirm_password', message='Passwords must match'), checkPasswordIsComplexEnough, checkPasswordIsNotCommon])
    
    confirm_password = PasswordField('Re-enter Password', validators=[
            InputRequired('Please provide a valid password'),
            Length(min=ValueConstants.MIN_PASSWORD_LENGTH, max=ValueConstants.MAX_PASSWORD_LENGTH, message=(u'Password must be a minimum of 6 characters'))
            ])
    
class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[InputRequired()])
    password = PasswordField('New password', validators=[
        InputRequired(), EqualTo('password2', message='Passwords must match'), Length(min=ValueConstants.MIN_PASSWORD_LENGTH, max=ValueConstants.MAX_PASSWORD_LENGTH, message=(u'Password must be a minimum of 6 characters'))
            ])
    password2 = PasswordField('Confirm new password', validators=[InputRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(min=ValueConstants.MIN_EMAIL_LENGTH, max=ValueConstants.MAX_EMAIL_LENGTH, message=(u'Email address length is invalid')),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(min=ValueConstants.MIN_EMAIL_LENGTH, max=ValueConstants.MAX_EMAIL_LENGTH, message=(u'Email address length is invalid')),
                                             Email()])
    password = PasswordField('New Password', validators=[
        InputRequired(), EqualTo('confirm_password', message='Passwords must match'), Length(min=ValueConstants.MIN_PASSWORD_LENGTH, max=ValueConstants.MAX_PASSWORD_LENGTH, message=(u'Password must be a minimum of 6 characters'))])
    confirm_password = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if db.session.query(User).filter(User.email == field.data).first() is None:
            raise ValidationError('Unknown email address.')


class ChangeEmailForm(Form):
    email = StringField('New Email', validators=[InputRequired(), Length(min=ValueConstants.MIN_EMAIL_LENGTH, max=ValueConstants.MAX_EMAIL_LENGTH, message=(u'Email address length is invalid')),
                                                 Email()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=ValueConstants.MIN_PASSWORD_LENGTH, max=ValueConstants.MAX_PASSWORD_LENGTH)])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if db.session.query(User).filter(User.email == field.data).first():
            raise ValidationError('Email already registered.')