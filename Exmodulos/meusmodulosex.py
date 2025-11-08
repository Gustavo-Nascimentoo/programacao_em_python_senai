# # 1 criar suas funções 
import random

# 1) Crie um número aleatório de 5,10

def atividade_1():
    n   =  random.randint(5,10)
    return n

# # 2) Crie 3 números aleatórios

def atividade_2():
    a   =  random.randint(1,101)
    k   =  random.randint(1,101)
    l   =  random.randint(1,101)
    return a, k, l


# # 3) Crie um número aleatório entre 10 a 30 utilize o range()

def atividade_3():
    b   =  random.randrange (10,31)
    return b

# # 4) Contagem regressiva simples Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)

def atividade_4():
    for n in range (10, 0, -1):
        print (n)
    print ("Fogo")

# # 5) Peça ao usuário que insira um
# #  número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.
# # Peça ao usuário que insira um número inteiro 
# # faça o loop com range e for ate´o numero
# # positivo e, em seguida, calcule a soma de 
# # todos os números pares de 2 até o número inserido.
# # (use módulo, if, for)

# 6) Tabuada de multiplicação
# Utilize print() na saída
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (while ou for )

def atividade_6():
    num = int(input("digite um número: "))
    for tab in range(1,11):
        print (num * tab)

# 7) Números ímpares reversos
# Exiba uma contagem regressiva de números ímpares de 99 a 1.
# (for)