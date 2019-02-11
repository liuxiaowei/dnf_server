from flask_mail import Message, Mail
from app.libs.log import APP_LOGGER
import app

mail = None


def init_mail(app):
    global mail
    mail = Mail(app)


def send_mail(subject, content, recipients, filename=None, content_type=None, attach=None):
    if not isinstance(recipients, list):
        recipients = [recipients]

    msg = Message(subject, sender='no-reply@utomarket.com', recipients=recipients)
    msg.body = content
    if filename:
        msg.attach(filename, content_type, attach)
    try:
        mail.send(msg)
    except Exception as e:
        APP_LOGGER.error('发送邮件失败, exception: {}'.format(str(e)))
        return False

    return True
