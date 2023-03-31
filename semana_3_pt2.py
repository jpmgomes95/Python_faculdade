valorReal = 0
valorBitCoin = 0
opcao = 0
valorConvertido= 0

print("Conversão de criptomoedas")
print("1 -  Converter Bitcoins em reais")
print("2 -  Converter Reais em BitcoinS")
print("3 -            Sair")
opcao = int(input("Escolha uma opção: "))

while opcao != 3:

    if opcao == 1:
        valorBitCoin = float(input("Insira o valor em BitCoins: "))
        #como o bitcoin vale aproximadamente 300 mil reais, apenas multiplico o valor de cada bitcoin por 300 mil
        valorConvertido = valorBitCoin * 300000
        print("O valor convertido de %.2f bitcoins para reais é de %.2f reais " %(valorBitCoin, valorConvertido))

    elif opcao == 2:
        valorReal = float(input("Insira o valor em Reais: "))
        #como uma bitcoin vale aproximadamente 300 mil reais, apenas divido o valor em reais por 300 mil
        valorConvertido =  valorReal/300000
        print("O valor convertido de %.2f reais é de %.2f bitcoins" %(valorReal, valorConvertido))


    print("Conversão de criptomoedas")
    print("1 -  Converter Bitcoins em reais")
    print("2 -  Converter Reais em BitcoinS")
    print("3 -            Sair")
    opcao = int(input("Escolha uma opção: "))



    