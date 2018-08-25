class DBConnectionSQL:
	name = 'SQL General'
	host = 'localhost'
	port = 5432
	user = 'pepito'
	#name manglig
	__passwd = 'therealpepito' #encapsulacion

	def __init__(self,host, port, user, passwd):
		self.host = host
		self.port = port
		self.user = user
		self.__passwd = passwd 

		print(self.name)

	#def connect(self):
	#	print('Connected')
	#	return True

	def get_info(self):
		return {
			'host': self.host,
			'port': self.port,
			'user': self.user,
		}

	#def disconnect(self):
	#	print('Disconnected')
	#	return True

	def __del__(self):
		print('Disconnected')


class PostgreSQL(DBConnectionSQL):
	name = 'PostgreSQL'

	def get_info(self):
		d = super().get_info()
		d['engine'] = 'PostgreSQL'
		return d 

	def __str__(self):
		return self.name

	def __repr__(self):
		return 'Soy PostgreSQL'

#conn = DBConnection(host='localhost', port=5439, user='luis', passwd='1234')
conn = PostgreSQL(host='localhost', port=5439, user='luis', passwd='1234')
print(conn)

#conn.connect()
#print(conn.get_info())
del conn

#conn.disconnect()

#print(conn.passwd)
#print([attr for attr in dir(conn)])
#print(conn._DBConnection__passwd)