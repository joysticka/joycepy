"""
User
	username
	passwd
	role

	set_username
	get_username => return
	set_passwd
	get_info => print
	login(username, passwd) => True or False
"""

class User:
	username = 'Joy'
	__passwd = '4567'
	role = 'dba'

	def __init__(self, username, passwd, role):
		self.username = username
		self.__passwd = passwd
		self.role = role
	
	def setUsername (self, username):
		self.username = username
		return True

	def getUsername (self):
		return self.username

	def setPasswd(self, passwd):
		self.__passwd = passwd
		return True

	def setRole (self, role):
		self.role = role
		return True

	def getRole (self):
		return self.role

	def getInfo(self):
		return {
			'username': self.username,
			'role': self.role,
		}

	def login(self, username, passwd):
		"""
		if (self.username == username) and (self.__passwd == passwd):
			print('Success')
			return True
		else:
			print('Error')
			return False
		"""
		return True if ((self.username == username) and (self.__passwd == passwd)) else False

	#solo se puede acceder con la clase
	@staticmethod
	def user_type():
		return ['admin','dba','dev']

	#@classmethod puedes acceder a objeto u clase, sin tener dependencia a la class
	#def user_type(cls):
	#	return ['admin','dba','dev']

	def __del__(self):
		print('Disconnected')

if __name__ == '__main__':
	user = User(username = 'pepito', passwd = 'therealpepito', role = 'dba')
	user.getInfo()
	user.setUsername(username = 'luis')
	print(user.getUsername())
	user.setRole(role = 'admin')
	print(user.getRole())
	user.setPasswd(passwd='1234')
	print(user.login(username='luis', passwd='1234'))

	print(User.user_type())









