# 4 – Um grande cliente seu sofreu um ataque hacker: o servidor foi sequestrado por um software malicioso, que criptografou todos os discos e pede a digitação de uma senha para a liberação da máquina. E é claro que os criminosos exigem um pagamento para informar a senha.
#Ao analisar o código do programa deles, porém, você descobre que a senha é composta da palavra “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120). Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio. ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial. Ele deve obrigatoriamente utilizar loop.

minutos = int(input("Digite os minutos marcados agora: "))
fatorial = 1
numero = minutos

while numero > 0:
    fatorial = fatorial * numero
    numero -= 1
print(f'O fatorial de {minutos} é = {fatorial}')

print(f'A senha é a palavra LIBERDADE + {fatorial}')
senha = input('Digite a senha correta: ')

if senha == f'LIBERDADE{fatorial}':
    print('Acesso liberado!')
else:
    print('Senha incorreta, tente novamente!')
