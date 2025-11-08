# peso = 65.00 # global 


# 1º cria a função 
def imc():
    ''' Calcula o IMC '''
    
    peso = float(input('Peso:')) # locais
    altura = float(input('Altura:')) # locais
    imc  =  peso / (altura ** 2)
    print(imc)




imc() # 2º chama para funcionar 