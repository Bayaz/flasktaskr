# project/models.py
# this will recreate the database that we used db_create.py in 
# first part of Flasktaskr app that used vanilla SQL

from views import db

class Task(db.Model):

	__tablename__ = 'tasks'

	





