
anoFabricacao = int(input("Digite o ano de fabricação do seu carro: "))
anoAtual = int(input("Digite o ano atual: "))
kmRodados = int(input("Quantos KM totais rodados possue o seu carro?: "))

mediaKm = kmRodados / (anoAtual-anoFabricacao)

print("A média de Km rodados anuais do seu carro é: ", mediaKm)