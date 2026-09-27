'''
=========================================================
SISTEMA DE FECHAMENTO DE CAIXA - LANCHONETE
=========================================================
Este programa calcula o faturamento do dia, a gorjeta
dos garcons e o controle de caixas de refrigerante.

ATENCAO: este codigo NAO esta pronto.
Ele tem problemas de varios tipos diferentes.
Alguns quebram o programa. Outros deixam ele rodar,
mas com resultado errado ou mal escrito.
=========================================================
'''

# ---------------- DADOS DA LOJA ----------------

nome_loja = 'Lanchonete Central'
dia = 15
mes = 'Setembro'
ano = 2026

print('=' * 45)
print('FECHAMENTO DE CAIXA')
print('Loja:', nome_loja)
print('Data: ', dia, '/', mes, '/', ano)
print('=' * 45)


# ---------------- VENDAS DO DIA ----------------

qtd_lanches = int(input('Quantos lanches foram vendidos? '))
preco_lanche = float(input('Preco de cada lanche: R$ '))

total_lanches = qtd_lanches * preco_lanche

qtd_refris = int(input('Quantos refrigerantes foram vendidos? '))
preco_refri = float(input('Preco de cada refrigerante: R$ '))

total_refris = round(qtd_refris * preco_refri,2)

faturamento = round(total_lanches + total_refris, 2)

print()
print('--- VENDAS ---')
print('Total em lanches:      R$', total_lanches)
print('Total em refrigerantes: R$', total_refris)
print('Faturamento bruto:     R$', faturamento)


# ---------------- GORJETAS ----------------
# A casa cobra 10% de gorjeta e divide entre 3 garcons.

qtd_garcons = 3
gorjeta_total = round(faturamento * 0.10,2)
gorjeta_cada = round(gorjeta_total / qtd_garcons, 2)

print()
print('--- GORJETAS ---')
print('Gorjeta total:    R$', gorjeta_total)
print('Cada garcom leva: R$', gorjeta_cada)


# ---------------- CUSTOS E LUCRO ----------------

custo_fixo = 250.00
lucro = round(faturamento - custo_fixo, 2)
lucro_conta = round((lucro / faturamento) * 100, 2) 


print()
print('--- RESULTADO ---')
print('Custo fixo do dia: R$', custo_fixo)
print('Lucro do dia:      R$', lucro)
print('Margem de lucro:', lucro_conta, '%')


# ---------------- CONTROLE DE ESTOQUE ----------------
# Cada caixa de refrigerante vem com 12 unidades.
# Preciso saber quantas caixas foram abertas e quantas
# latas sobraram soltas fora de caixa.

unidades_por_caixa = 12
caixas_abertas = (qtd_refris // unidades_por_caixa)
latas_soltas = qtd_refris % unidades_por_caixa

print()
print('--- ESTOQUE ---')
print('Caixas abertas:', caixas_abertas)
print('Latas soltas:  ', latas_soltas)


# ---------------- CONFERENCIA ----------------

loja_aberta = 'Sim'
meta_do_dia = 500
bateu_meta = faturamento >= meta_do_dia

print()
print('--- CONFERENCIA ---')
print('Loja abriu hoje?', loja_aberta)
print('Bateu a meta de R$', meta_do_dia, '?', bateu_meta)
print('Tipo do faturamento:', type(faturamento))
print('Tipo da qtd de lanches:', type(qtd_lanches))

print()
print('Fechamento concluido.\nVolte sempre!')
print("Assinado: \"Gerencia\"")
