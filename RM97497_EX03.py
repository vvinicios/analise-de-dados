#3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

#Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:
#VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
#POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

aluno_impar = 1
total_impar = 0

for aluno_impar in range(1,51,2):

    print('Você está digitando a nota dos alunos ímpares!')
    nota_impar = float(input(f'Digite a nota do aluno número {aluno_impar}: '))
    aluno_impar = aluno_impar + 2
    total_impar = total_impar + nota_impar


aluno_par = 2
total_par = 0

for aluno_par in range(2,51,2):

    print('Agora você está digitando a nota dos alunos pares!')
    nota_par = float(input(f'Digite a nota do aluno número {aluno_par}: '))
    aluno_par = aluno_par + 2
    total_par = total_par + nota_par

media_impar = total_impar / 25
media_par = total_par / 25

print(f'A média dos alunos de número ímpar foi de: {media_impar}')
print(f'A média dos alunos de número par foi de: {media_par}')

if media_impar > media_par:
    print('Os alunos de número ímpar, tiveram a maior média!')
else:
    print('Os alunos de número par, tiveram a maior média!')
