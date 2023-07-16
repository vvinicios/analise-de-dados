valorSalario = float(input("Digite o valor do seu salário: "))
desconto1 = 0.075
desconto2 = 0.15
desconto3 = 0.225
desconto4 = 0.275

if valorSalario <= 1903.98:
    print("Você está isento de imposto de renda!")

elif valorSalario > 1903.98 and valorSalario <= 2826.65:
    deducao = 142.80
    valorDesconto = (valorSalario * desconto1)  - deducao
    print("O desconto do IRPF é:", valorDesconto)

elif valorSalario > 2826.65 and valorSalario <= 3751.05:
    deducao = 354.80
    valorDesconto = (valorSalario * desconto2) - deducao
    print("O desconto do IRPF é:", valorDesconto)

elif valorSalario > 3751.05 and valorSalario <= 4664.68:
    deducao = 636.13
    valorDesconto = (valorSalario * desconto3) - deducao
    print("O desconto do IRPF é:", valorDesconto)

elif valorSalario > 4664.68:
    deducao = 869.36
    valorDesconto = (valorSalario * desconto4) - deducao
    print("O desconto do IRPF é:", valorDesconto)

else: 
    print("Digite um valor correto!")