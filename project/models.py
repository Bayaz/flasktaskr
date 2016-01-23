# project/models.py
# this will recreate the database that we used only db_create.py in 
# first part of Flasktaskr app using vanilla SQL

from views import db

class Task(db.Model):

	__tablename__ = 'tasks'

	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	







