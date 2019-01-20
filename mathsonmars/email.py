from threading import Thread
from flask import current_app, render_template
from mathsonmars.marslogger import logger
from flask.ext.mail import Mail, Message
#import sendgrid
#import mailchimp

from mathsonmars.settings import Config as config

mail = Mail()

def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e), e.args)
            logger.error("--send_async_email() {0}".format(message))

def send_email(email_type, to, subject, template, **kwargs):
    if to is not None:
        logger.debug(">>send_email to:{0}, subject:{1}".format(to, subject))
        app = current_app._get_current_object()
        msg = Message(email_type + ' ' + subject,
                      sender=app.config['MAIL_SENDER'], recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        msg.html = render_template(template + '.html', **kwargs)
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()
        return thr
    