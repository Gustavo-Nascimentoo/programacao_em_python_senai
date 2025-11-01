# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.

numero = int(input("Digite um número: "))
if numero == 0:
    print ('O número é zero')
elif numero >= 1:
    print ('O número é positivo')
else:
    print ('O número é negativo')

# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.

idade = int(input('Digite sua idade: '))
if idade >= 16:
    print ('Você ja pode votar')
else:
    idadevoto = 16 - idade
    print ("Você ainda não pode votar, espere mais", idadevoto, "anos")
# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.

parouimpar = int(input('Digite um número: '))
if parouimpar % 2 == 0:
    print ("O número é par")
else:
    print ("O número é impar")

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 == n2 and n2 == n3:
    print ("O triângulo é equilátero")
elif n1 != n2 and n2 != n3 and n1 != n3:
    print ('O triângulo é escaleno')
else:
    print ("O triângulo é isósceles")

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.

# 5*

# Determine se um número é múltiplo de 5 e 7.

divisivel = int(input('Digite um número: '))
if divisivel % 5 == 0 and divisivel % 7 == 0:
    print ("O número é divisível por 5 e 7")
else:
    print ("O número não é divisível por 5 e 7")

# 6*

# Verifique se um número é positivo e maior que 10

numero2 = int(input('Digite um número: '))
if numero2 > 0 and numero2 > 10:
    print ("O", numero2, "é positivo e maior que dez")
elif numero2 > 0 and numero2 < 10:
    print ("O", numero2, "é positivo e menor que dez")
elif numero2 < 0:
    print ("O", numero2, "é negativo e não é maior que dez")
elif numero2 == 0:
    print ("O", numero2, "é zero e não é maior que dez")

# 7*

# Verifique se um número é divisível por 3 ou 5.

numero3 = int(input('Digite um número: '))
if numero3 % 5 == 0 and numero3 % 3 == 0:
    print ('O número é divisível por 3 e 5')
elif numero3 % 3 == 0:
    print ('O número é divisível por 3')
elif numero3 % 5 == 0:
    print ("O número é divisível por 5")
else:
    print ('O número não é divisível por 3 e 5')

