#from helpers.utils import login, login2
from helpers.utils import (login, login2,)
from pprint import pprint

user1 = {
	'username':'joy',
	'role':'admin',
	'password':'therealjoy', #trai;ing comma
	'info': {
		'address': 'Sillicon valley',
		'phone': '123456789',
		'ssn': '1234567980',
	}
}

user2 = {
	'username':'joyce',
	'role':'dba',
	'password':'therealjoy1', #trai;ing comma
	'info': {
		'address': 'Sillicon valley',
		'phone': '123456789',
		'ssn': '1234567980',
	}
}


pprint(user1['username'])
pprint(user1['role'])
is_admin1 = login2(user1)
print(is_admin1)

print('================')

pprint(user2['username'])
pprint(user2['role'])
is_admin2 = login2(user2)
print(is_admin2)