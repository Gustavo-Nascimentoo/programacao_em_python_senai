# ***Sistema de Reservas de Hotel:***
# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*
# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

c1 = input('Digite o nome do Cliente e sua idade: ')
c2 = input('Digite o nome do Cliente e sua idade: ')
c3 = input('Digite o nome do Cliente e sua idade: ')
Clientes = [c1,c2,c3]
Carrinho = []
Quartos = ['', 'Simples','Duplo','Luxo']
Valores = [0, 100.00, 150.00, 250.00]
print(f'''
{Quartos[1]} R$ - {Valores[1]}
{Quartos[2]} R$ - {Valores[2]}
{Quartos[3]} R$ - {Valores[3]}
''')
Quarto1 = int(input("Digite o quarto: "))
Quarto2 = int(input("Digite o quarto: "))
Quarto3 = int(input("Digite o quarto: "))

Qtddia1 = int(input("Quantos dias vai ficar no hotel? "))
Qtddia2 = int(input("Quantos dias vai ficar no hotel? "))
Qtddia3 = int(input("Quantos dias vai ficar no hotel? "))

if Quarto1 == 1:
    Total1 = Qtddia1 * (Valores)[Quarto1]
elif Quarto1 == 2:
    Total1 = Qtddia1 * (Valores)[Quarto2]
else:
    Total1 = Qtddia1 * (Valores)[Quarto3]
if Quarto2 == 1:
    Total2 = Qtddia2 * (Valores)[Quarto1]
elif Quarto2 == 2:
    Total2 = Qtddia2 * (Valores)[Quarto2]
else:
    Total2 = Qtddia2 * (Valores)[Quarto3]
if Quarto3 == 1:
    Total3 = Qtddia3 * (Valores)[Quarto1]
elif Quarto3 == 2:
    Total3 = Qtddia3 * (Valores)[Quarto2]
else:
    Total3 = Qtddia3 * (Valores)[Quarto3]


print("--------------------------------------")
print(c1)
print("O total das diárias foi de R$", Total1)
print("--------------------------------------")

print("--------------------------------------")
print(c2)
print("O total das diárias foi de R$", Total2)
print("--------------------------------------")

print("--------------------------------------")
print(c3)
print("O total das diárias foi de R$", Total3)
print("--------------------------------------")

forma_pag = [" ","1 - PIX", "2 - CC", "3 - CD"]
pag = int(input("Escolha a forma de pagamento a partir do ID: "))
print ("Sua forma de pagamente é", forma_pag[pag], "Obrigado, volte sempre!")