f = open('quotes.txt','r')
f2 = open('quotes2.txt','w')
f3 = open('quotes3','wb')

print(f.readlines)

for line in f.readlines():
	#print(line)
	#line = f.read(1024)
	#f2.write(line)
	f3.write(bytes(line,'iso-8859-1'))


f.close()
f2.close()
f3.close()