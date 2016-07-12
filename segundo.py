# Problema do ano bixesto

year = int (input ("Digite um ano para verificar se e bixest0: "))

if year % 4 == 0:
	if year / 100 > 0:
		if year / 400 > 0:
			print ("O ano e bixesto.")
else:
	print ("Ano nao bixesto")

# Problema do total de pescado

peso = int (input ("Digite o peso total do peixes: "))
multa = 0
acima = 0

if peso > 50:
	acima = peso - 50
	print ("Peso acima da regulamentacao: %f" %acima)
	print ("Multa: R$%d" %(acima / 4))
else:
	print ("Sem multa.")

# Problema das latas de tinta

a = int (input ("Digite a area total a ser pintada: "))
cobertura = 3 * 18

if a % cobertura == 0:
	total = a / cobertura
else:
	total = (a / cobertura) + 1 

print ("Total de latas de tintas neccessarias: %d" %total)





