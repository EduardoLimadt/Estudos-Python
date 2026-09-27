'''
Novo exercicio de python
dessa vez um desconto progressivo ou por faixa de valor

'''

print('Loja de Sapatos lhorte')
print('Calculadora de descontos por faixa')
print('Uso restrito dos Funcionarios')


valor_venda = float(input('Digite o valor da sua venda: '))
desconto_cinco = round(valor_venda * 0.05, 2)
desconto_dez = round(valor_venda * 0.10, 2)
valor_final_cinco = round(valor_venda - desconto_cinco, 2)
valor_final_dez = round(valor_venda - desconto_dez, 2)

if valor_venda <= 100:
    print(f'Valor de Compra: {valor_venda}')
    print('Desconto: Sem desconto') 
    print(f'Valor a pagar: {valor_venda}')

elif valor_venda > 100 and valor_venda <= 500:
    print(f'Valor de Compra: {valor_venda}')
    print(f'Desconto: {desconto_cinco}')
    print(f'Valor a pagar: {valor_final_cinco}')

else:
    print(f'Valor de Compra: {valor_venda}')
    print(f'Desconto: {desconto_dez}')
    print(f'Valor a pagar: {valor_final_dez}')

print('Seguir para pagamento.')    