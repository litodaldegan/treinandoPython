# Problema de fazer a soma de dois numeros

a = int (input ("Digite o primeiro numero: "))
b = int (input ("Digite o segundo numero: "))

print ("Soma: %d" %(a+b))

# Problema de transformar dias, horas e minutos em segundos

c = int (input ("Digite dias: "))
d = int (input ("Digite horas: "))
e = int (input ("Digite minutos: "))

c *= 24 * 60 * 60
d *= 60 * 60
e *= 60

print ("Total em segundos: %d" %(c+d+e))

# Problema de calcular aumento de salario

f = float (input ("Digite o salario atual: "))
h = float (input ("Digite o percentual de aumento: "))

print ("Novo salario: %f" %(f* (1+ h/100)))

# Problema de calcular o tempo de viagem

km = int (input ("Digite a distancia total: "))
av = int (input ("Digite a velocidade media: "))

print ("Tempo total de viagem: %dhoras" %(km/av))

# Problema de dizer quantos digitos 2 elevado a um milhao tem

x = pow(2,1000000)

x2 = str(x)

x3 = len(x2)

print ("tamanho de 2 elevado a um milhao: %d" %x3)