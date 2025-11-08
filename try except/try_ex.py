try:
    N1 = int(input("Digite um número: "))
    N2 = int(input("Digite outro número: "))
    print ("O resultado dessa multiplicação é:", N2*N1)
except ValueError:
    print ("Isso não é um número")

try:
    N3 = int(input("Digite um número: "))
    N4 = int(input("Digite outro número: "))
    print (N3/N4)
except ZeroDivisionError:
    print ("Ocorreu um erro na divisão")

try:
    lista = ["",1,2,3]
    indice = int(input("Digite o índice da lista: "))
    print (lista[indice])
except ValueError:
    print ("Esse índice não existe")