#_config.py
import os

#grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# define the full path of the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)