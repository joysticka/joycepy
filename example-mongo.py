#! /usr/bin/env python3

from pprint import pprint

user = {
	'username':'joy',
	'role':'dba',
	'password':'therealjoy', #trai;ing comma
	'info': {
		'address': 'Sillicon valley',
		'phone': '123456789',
		'ssn': '1234567980',
	}
}

pprint (user)

if (user['username']=='joy') and (user['password']=='therealjoy') and (user['role']=='dba'):
	print('welcome {}'.format(user['username']))

else:
	print('denied')
