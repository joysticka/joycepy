#def getNumbers(n):
#	return [x for x in range(n)]

#print (getNumbers(10))



#def getNumbers(n):
#	for x in range(n):
#		return x

#print (getNumbers(10))


def getNumbers(n):
	for x in range(n):
		yield x 

g = getNumbers(10)
print(g.__next__())
print(g.__next__())

#for y in getNumbers(10):
#	print(y)

#un generador te extrega los valores conforme las vayas necesitando para no agotar la memoria con colecciones de base de datos