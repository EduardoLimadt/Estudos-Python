'''
CONVERSOR DE TEMPO
Exercicio solicitado pelo Claude: 
fazer a converção de segundos para horas minutos 
e segundos.
'''

print ('Conversor de Tempo')

segundos_solicitados = int(input('Quantos Segundos Você Quer Converter? '))

horas = segundos_solicitados // 3600
resto = segundos_solicitados % 3600

minutos = resto // 60
segundos_restante = resto % 60

print (f'É igual a {horas} horas, {minutos} minutos e {segundos_restante} segundos.')

'''
Fiz mas com ajuda, nao entendi bem, o modulo me da qual numero? o resto da divisao? 


'''