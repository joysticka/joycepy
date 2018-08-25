"""
def login(user):
	if (user['role']=='admin'):
		return True

	else:
		return False

"""

def login(user):
	return True if user['role'] == 'admin' else False


login2 = lambda user: True if user['role'] == 'admin' else False