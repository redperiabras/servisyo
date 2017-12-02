import logging

from app.config_common import *


# DEBUG has to be to False in a production environment for security reasons
DEBUG = False

# Secret key for generating tokens
SECRET_KEY = 'servisyo_mnl'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'pa$$word')

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Configuration of a Gmail account for sending mails
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'servisyo.mnl'
MAIL_PASSWORD = 'p@$$word'
ADMINS = ['servisyo.mnl@gmail.com']

# Number of times a password is hashed
BCRYPT_LOG_ROUNDS = 12

LOG_LEVEL = logging.INFO
LOG_FILENAME = 'activity.log'
