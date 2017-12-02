from flask.ext.script import Manager, prompt_bool, Shell, Server
from termcolor import colored

from app import app, db, models


manager = Manager(app)


def make_shell_context():
	return dict(app=app)


@manager.command
def initdb():
	''' Create the SQL database. '''
	db.create_all()

	users = [{
			"first_name": "Lester",
			"last_name": "Verceles",
			"gender": "M",
			"profession": "Graphic Designer",
			"phone": "09093291283",
			"email": "lester@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.5513402,
			"geolng": 120.9871093
			}, 
			{
			"first_name": "Roddy",
			"last_name": "Dawidman",
			"gender": "M",
			"profession": "Mechanic",
			"phone": "09093291283",
			"email": "roddy@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.551211,
			"geolng": 120.991646
			}, {
			"first_name": "Odele",
			"last_name": "Martynikhin",
			"gender": "F",
			"profession": "Laundress",
			"phone": "09093291283",
			"email": "odele@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.5537202,
			"geolng": 120.9873491
			}, {
			"first_name": "Karyn",
			"last_name": "Emor",
			"gender": "F",
			"profession": "Housekeeper",
			"phone": "09093291283",
			"email": "karyn@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.550195, 
			"geolng": 120.990644
			}, {
			"first_name": "Wesley",
			"last_name": "Blondel",
			"gender": "M",
			"profession": "Carpenter",
			"phone": "09093291283",
			"email": "wesley@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.550266,
			"geolng": 120.991943
			}, {
			"first_name": "Yardley",
			"last_name": "Seymer",
			"gender": "M",
			"profession": "Mechanic",
			"phone": "09093291283",
			"email": "yardley@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.551674, 
			"geolng": 120.991495
			}, {
			"first_name": "Stanleigh",
			"last_name": "Kinrade",
			"gender": "M",
			"profession": "Welder",
			"phone": "09093291283",
			"email": "welder@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.553783,
			"geolng": 120.992063
			}, {
			"first_name": "Dorree",
			"last_name": "Pluck",
			"gender": "F",
			"profession": "Shoemaker",
			"phone": "09093291283",
			"email": "dorree@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.552051, 
			"geolng": 120.992116
			}, {
			"first_name": "Syd",
			"last_name": "Jehaes",
			"gender": "M",
			"profession": "Plumber",
			"phone": "09093291283",
			"email": "syd@gmail.com",
			"password": "123456",
			"confirmation": False,
			"geolat": 14.551825, 
			"geolng": 120.991383
			}]

	for user in users:
		user = models.User(
            first_name=user['first_name'],
            last_name=user['last_name'],
            profession=user['profession'],
            gender=user['gender'],
            phone=user['phone'],
            email=user['email'],
            confirmation=['user'],
            password=user['password'],
            geolat=user['geolat'],
            geolng=user['geolng'])
		db.session.add(user)

	db.session.commit()

	print(colored('The SQL database has been created', 'green'))

@manager.command
def dropdb():
	''' Delete the SQL database. '''
	if prompt_bool('Are you sure you want to lose all your SQL data?'):
		db.drop_all()
		print(colored('The SQL database has been deleted', 'green'))


manager.add_command('runserver', Server(host="0.0.0.0", port=5000))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
	manager.run()
