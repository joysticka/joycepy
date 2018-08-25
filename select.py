
#! /usr/bin/env python3

"""
shebang
sharpbang
hashbang
"""


#role = 'dba'

#if role == 'admin':
#	print('welcome admin')

#elif role == 'user':
#	print('welcome user')

#elif role == 'dba':
#	print('welcome dba')

#else:
#	print('denied')


users = ['joy','joyce']
roles = ['dba','admin']

compressed = zip(users, roles)

for role in compressed:
	if role[1]  == 'admin':
		print ('role:' + role[1])
		print('welcome admin')
	else:
		print ('role:' + role[1])
		print('access denied')

