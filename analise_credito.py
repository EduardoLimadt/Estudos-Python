'''
Vamos la, mais uma atividade de fixação
devo fazer uma especie de app bancario, nele vai ser uma 
analise de credito, para isso , vou fazer um organograma. 

app banco do brasil, cadastro do cliente, 

nome, cpf, estado, telefone, trabalho, tempo de serviço e renda mensal.

passado isso, pergunto qual o valor que o cliente iria querer emprestado,
em quantas parcelas ele quer dividir.

feito esse cadastro, se o cliente tiver menos de 12 meses trabalhados, ele nao pode 
fazer o emprestimo, mais de 12 meses, segue, em seguida 
devo fazer a conta do valor que vai ficar a parcela
quando souber a parcela, devo ver se ela passa do limite de 30% do salario  do cliente.

'''

print('Banco do Brasil.')
print('Analise de Crédito')

nome_cliente = input('Digite nome e sobrenome: ')
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu telefone com DDD: ')
trabalho = input('Em que você trabalha: ')
tempo_servico = int(input('Quantos meses nesse emprego?: '))

if tempo_servico < 12:
    print('Infelizmente não poderemos prosseguir com a solicitação, criterio minimo não atingido. Volte sempre.')
else:
    print('Otimo, criterio inicial atingido, abaixo informe sua renda')
    renda_mensal = float(input('Digite a media dos seus ultimos 3 salarios: '))
    valor_desejado = float(input('Qual valor você deseja solicitar?: '))
    parcelas_desejadas = int(input('Em quantas parcelas deseja pagar? '))
    
    import time
    time.sleep(1)
    print('Calculando ........')
    time.sleep(1)
    print('Calculando ........')
    time.sleep(0.5)
    print('Calculando ........')

#CONTAS

    valor_parcela = round((valor_desejado * 0.10 + valor_desejado) / parcelas_desejadas ,2)
    terco_salario = round(renda_mensal * 0.3 ,2)

    if valor_parcela <= terco_salario:
        status = 'APROVADO'
    else:
        status = 'REPROVADO'


    print('Proposta finalizada')
    print(f'Nome: {nome_cliente}')
    print(f'CPF: {cpf}')
    print(f'Telefone: {telefone}')
    print(f'Renda média: {renda_mensal}')
    print(f'Valor solicitado: {valor_desejado}')
    print(f'Valor da Parcela: R${valor_parcela}')
    print(f'Status: {status}')


