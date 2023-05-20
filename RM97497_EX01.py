# 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

# Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:

cliente = 0
basic = 0.3
silver = 0.2
gold = 0.1
platinum = 0.05

print('Bem vindo!')
print('1 - Cliente Basic')
print('2 - Cliente Silver')
print('3 - Cliente Gold')
print('4 - Cliente Platinum')
cliente = float(input('Qual o tipo de assinatura do Cliente? '))
faturamento = float(input('Qual o faturamento do Cliente nos últimos 12 meses em reais? '))

if cliente == 1:
    bonus = faturamento * basic
    print(f'O Cliente deverá pagar o valor de: R${bonus:.2f}')
elif cliente == 2:
    bonus = faturamento * silver
    print(f'O Cliente deverá pagar o valor de: R${bonus:.2f}')
elif cliente == 3:
    bonus = faturamento * gold
    print(f'O Cliente deverá pagar o valor de: R${bonus:.2f}')
elif cliente == 4:
    bonus = faturamento * platinum
    print(f'O Cliente deverá pagar o valor de: R${bonus:.2f}')
else:
    print('Cliente inválido! Por favor, digite novamente!')



