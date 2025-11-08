# arquivo modulo.py
import  statistics

#medida de tendencia central:
# moda -  media - mediana  -  desvio  
# variancia  -  amplitude 

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

def estatistica(empresa1):
    dados2 =  set(empresa1)
    ''' moda é o que mais aparece'''
    if len(empresa1) != len(dados2):
        moda = statistics.mode(empresa1)
        print('moda', moda)

    else:    
        print('Não tem moda')

def media(empresa1):
    ''' soma dos indices /  quantidade'''
    media  =  statistics.mean(empresa1)
    return 'media', media

def mediana(empresa1):
    ''' esta no meio da frequencia'''
    med  =  statistics.median(empresa1)
    return med

def desvio(empresa1):
    ''' a raiz quadrada da variancia '''
    d =  statistics.stdev(empresa1)
    return d

def variancia(empresa1):
    ''' a distancia entre a media quadratica a os indices '''
    variancia   =  statistics.variance(empresa1)
    return variancia


def amplitude(empresa1):
    ampl = max(empresa1) -  min(empresa1)
    return ampl












def imc(peso, altura):
    return peso/altura**2

def calcular_soma(x,y):
    return x + y

def verificar_idade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'Menor de idade'