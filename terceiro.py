# Problema de nome e senha

nome = ""
senha = ""

while nome == senha:
	nome = str (input ("Digite seu usuario: "))
	senha = str (input ("Digite a senha: "))

	if nome == senha:
		print ("Senha igual ao nome.")

print ("Usuario cadastrado com sucesso")

# Problema das populacoes

a = 80000
b = 200000

txa = 1.03
txb = 1.015

years = 0

while a < b:
	a *= txa
	b *= txb
	years += 1

print ("Numero de anos necessario para A ficar maior que B: %d " %years)
print ("A - %d \nB - %d" %(a, b))

# Fibonacci

x = int (input ("Digite o numero de Fibonacci desejado: "))
i = 0
fst = 1
scd = 1

x -= 1

while i < x:
	aux = scd 
	scd += fst
	fst = aux
	i += 1

print ("%d Fibonacci: %d" %(x+1, scd))

# Calculo do mdc de dois numeros

x = int (input ("Entre com o primeiro numero: "))
y = int (input ("Entre com o segundo numero: "))

while y != 0:
	resto = x % y
	x = y
	y = resto

print ("MDC: %d" %x)