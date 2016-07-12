
notas = [10,
		15,
		20,
		40]

x = 0
soma = 0

while x < 4:
	soma += notas[x]
	x += 1

print ("Media: %d" %(soma/x))
