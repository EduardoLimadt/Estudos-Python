'''
Estou no Rj e quero praticar, pensei em criar algo simples
tipo um cadastro do hotel para chekin
'''
print('Bem Vindo ao Hotel Copacabana Palace')
nome_cliente_um = input('Insira seu nome completo: ')
condicao_um = input('Deseja adcionar mais algum hospede? ')

if condicao_um.lower() == 'sim':
    nome_cliente_dois = input('Insira o nome completo: ')
else:  
    print('Vamos seguir') 

print('Adcione o endereço completo: ')  
cep = input('Digite o Cep: ')
rua = input('Digite a Rua: ')
bairro = input ('Digite bairro: ')
cidade = input ('Digite a Cidade: ')

print('Vamos ao café da manhã: ')

cafe_manha = input('Escreva o que mais gosta de cafe da manha: ')


print(f'Seja bem vindo: {nome_cliente_um},')
if condicao_um.lower() == 'sim':
    print(f'Segundo hospede: {nome_cliente_dois}')
else: 
    print('Hospede unico')   
print(f'Seu endereço é: {cep}, {rua}, {bairro}, {cidade}.')
print(f'Sua opção de cafe da manhã é: {cafe_manha}')

confirmacao = input('Confirma as informaçoes? ')

if confirmacao.lower() == 'sim':
    print ('Perfeito, boa estadia')
else:
    print('Vamos recomeçar.')