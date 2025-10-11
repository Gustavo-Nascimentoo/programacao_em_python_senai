lista_alunos = []
nome1= input('nome 1: ')
nome2= input('nome 2: ')
nome3= input('nome 3: ')

lista_alunos.append(nome1)
lista_alunos.append(nome2)
lista_alunos.append(nome3)

notas_aluno1 = [float(input(f'nota 1:{nome1} ')), float(input(f'nota 2:{nome1} '))]
notas_aluno2 = [float(input(f'nota 1:{nome2} ')), float(input(f'nota 2:{nome2} '))]
notas_aluno3 = [float(input(f'nota 1:{nome3} ')), float(input(f'nota 2:{nome3} '))]

media_aluno1 =  sum(notas_aluno1)/len(notas_aluno1)
media_aluno2 =  sum(notas_aluno2)/len(notas_aluno2)
media_aluno3 =  sum(notas_aluno3)/len(notas_aluno3)

print('Média Alunos')

print(f''''

Médias:
aluno{nome1} - {media_aluno1}
aluno{nome2} - {media_aluno2}
aluno{nome3} - {media_aluno3}
''')

aprovado_1 = media_aluno1 >= 7
aprovado_2 = media_aluno2 >= 7
aprovado_3 = media_aluno3 >= 7

print(f'''
{nome1} - APROVADO - {aprovado_1}
{nome2} - APROVADO - {aprovado_2}
{nome3} - APROVADO - {aprovado_3}
''')

lista  =  [1,2,3,4,5,6]


l =  list(range(1,2000))
print(l)
