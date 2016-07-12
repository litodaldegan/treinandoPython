import math

 # Problema de numero triangular

# x = int (input ("Digite um numero para verificar se ele e triangular: "))

# x1 = 0
# x2 = 1
# x3 = 2

# while (x1 * x2 * x3) < x:
# 	x1 += 1
# 	x2 += 1
# 	x3 += 1

# if (x1 * x2 * x3) == x:
# 	print ("Numero triangular (%d %d %d)." % (x1,x2,x3))
# else:
# 	print ("Numero nao trinagular")

# # Problema do troco

# nota = [50,
# 		20,
# 		10,
# 		5,
# 		2,
# 		1]

# trocos = [0,
# 		0,
# 		0,
# 		0,
# 		0,
# 		0]

# troco = -1

# apg = int (input ("Insira um valor a ser pago: "))

# while troco < 0:
# 	pg = int (input ("Insira um valor pago: "))
# 	troco = pg - apg

# 	if troco < 0:
# 		print ("Valor insuficiente para fazer o pagamento.")

# i = 0

# print (troco)

# while troco > 1:
# 	print (troco)
# 	trocos[i] = troco / nota[i]
# 	troco %= nota[i]
# 	i += 1

# x = 0

# while x < 6:
# 	print ("Nota : %d quantidade: %d" %(nota[x],trocos[x]))
# 	x += 1

# Verificar se um numero primo

y = float (input ("Insira um numero para testar se ele e primo: "))

h = math.sqrt(y)

i = float (2)

while i < h:
	if (y % i) == 0:
		print ("Divisivel por %d" %i)
		i = h
	else:
		i += 1

if i != h:
	print ("Numero primo")