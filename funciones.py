"""
def saludar():
	print("holiii")

saludar()

def suma(a,b):
	return a + b

num1 = 5
num2 = 6
print(suma(num1, num2))



def foo(*args, **kwargs):
	print(args) #tupla
	print(kwargs) #diccionario	

foo ('dba',1, name = 'joy', age=32)



f = lambda x: print(x)
f('hola')
print(f)
"""

def myfunc(n):
	return lambda a : a * n  

