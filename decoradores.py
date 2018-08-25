def decorador(f):
	def envoltura():
		print(':)')
		f()
		print('adios')
	return envoltura

@decorador	
def saludo():
	print('hola')
