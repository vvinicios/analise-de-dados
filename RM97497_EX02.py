# 2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.

segunda = int(input('Qual a quantidade de votos que a Segunda-Feira recebeu? '))
terca = int(input('Qual a quantidade de votos que a Terça-Feira recebeu? '))
quarta = int(input('Qual a quantidade de votos que a Quarta-Feira recebeu? '))
quinta = int(input('Qual a quantidade de votos que a Quinta-Feira recebeu? '))
sexta = int(input('Qual a quantidade de votos que a Sexta-Feira recebeu? '))

if segunda > terca:
    print('O dia ganhador foi: Segunda-Feira')
elif segunda > quarta:
    print('O dia ganhador foi: Segunda-Feira')
elif segunda > quinta:
    print('O dia ganhador foi: Segunda-Feira')
elif segunda > sexta:
    print('O dia ganhador foi: Segunda-Feira')
else:
    if terca > quarta:
        print('O dia ganhador foi: Terça-Feira')
    elif terca > quinta:
        print('O dia ganhador foi: Terça-Feira')
    elif terca > sexta:
        print('O dia ganhador foi: Terça-Feira')
    else:
        if quarta > quinta:
            print('O dia ganhador foi: Quarta-Feira')
        elif quarta > sexta:
            print('O dia ganhador foi: Quarta-Feira')
        else:
            if quinta > sexta:
                print('O dia ganhador foi: Quinta-Feira')
            else:
                print('O dia ganhador foi: Sexta-Feira')
                