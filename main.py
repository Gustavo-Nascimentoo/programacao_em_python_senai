# arquivo main.py

import modulo as mdl

empresa1 = [1000,6000,1200,8000,1400]

print(mdl.imc(65,1.70))
print(mdl.calcular_soma(10,30))
print(mdl.verificar_idade(25))
print('media',mdl.media(empresa1))
print('mediana',mdl.mediana(empresa1))
print('desvio',mdl.desvio(empresa1))
print('variancia',mdl.variancia(empresa1))
print('amplitude', mdl.amplitude(empresa1))
