import random

#  Maior menor de 10 sorteados

numerosSorteados = []

i = 0

while i < 10:
	numerosSorteados.append (int(random.random() * 100))
	i+=1

maior = 0
menor = 100

i = 0

while i < 10:
	if numerosSorteados[i] > maior:
		maior = numerosSorteados[i]
	elif numerosSorteados[i] < menor:
		menor = numerosSorteados[i]
	i += 1

print numerosSorteados
print ("Maior: %d Menor: %d" %(maior,menor))

#  Separar impar e par em sorteados

impares = []
pares = []

i = 0

while i < 10:
	numerosSorteados.append (int(random.random() * 100))
	i+=1

i = 0

while i < 20:
	if numerosSorteados[i] % 2 == 0:
		pares.append (numerosSorteados[i])
	else:
		impares.append (numerosSorteados[i])
	i += 1

print numerosSorteados
print ("Impares: %s" %impares)
print ("Pares: %s" %pares)

# Lista de palavras
s = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."

ss = s.split()
ssPytohn = []
lengthSS = len(ss)

i = 0

while i < lengthSS:
	if 'pythonPYTHON'.find(ss[i][0]) > 0:
		 ssPytohn.append(ss[i])
	elif 'pythonPYTHON'.find(ss[i][-1]) > 0:
		ssPytohn.append(ss[i])
	i += 1 

print (ssPytohn)





