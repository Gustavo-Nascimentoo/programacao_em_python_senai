# 1) CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar).

# def res1():

#     n1 = int(input("Digite um número: "))
#     n2 = int(input("Digite um número: "))
#     res1 = n1 % 2
#     if res1 == 0:
#         print (n1,"é par")
#     else:
#         print (n1, "é impar")
#     res1 = n2 % 2
#     if res1 == 0:
#         print (n2,"é par")
#     else:
#         print (n2, "é impar")

# res1()

# 2) CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

# def mult():

#     n1 = int(input("Digite um número: "))
#     n2 = int(input("Digite um número: "))
#     n3 = int(input("Digite um número: "))
#     mult = n1 * n2 * n3
#     print (mult)

# mult()

# 3) CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

# def aoqdd():

#     n1 = int(input("Digite um número: "))
#     aoqdd = n1 ** 2
#     print (aoqdd)

# aoqdd()

# 4) CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

# def ida():

#     ida = int(input("Digite sua idade: "))
#     if ida == 18:
#         print("Parabens por ser maior de idade 🎉🎉🎉")
# ida()

# 5) DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

# def idade():

#     anonasc = int(input("Em que ano você nasceu? "))
#     idade = 2025 - anonasc
#     print (idade)
# idade()

# 6) DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.

# def copa():
#     copa = [1958, 1962, 1970, 1994, 2002]
#     ano = 1999
#     if ano in copa:
#         print ("Brasil venceu a copa em", ano)
#     else:
#         print ("Brasil perdeu a copa em", ano)

# copa()

# 7) DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  

# def Restaurante(): 
#     Restaurante = {
#     'Salada': 12.90,
#     'Macarronada':25.90,
#     'Sanduiche': 9.90,
#     'Sorvete': 4.99,
#     }

#     print(f'''
#      {Restaurante}
#      ''')
#     carrinho= []
#     valores= []
#     produto1 = input('Digite o nome do produto que deseja: ')
#     carrinho.append([produto1])
#     print(carrinho)
#     valores.append(Restaurante[produto1])
#     print ('R$', valores)

# Restaurante()