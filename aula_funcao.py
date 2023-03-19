def ler_numeros():

    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o Segundo número: "))
    numero_3 =  float(input("Digite o terceiro núnmero: "))
    
    print("Os números lidos são: "+numero_1, +", "+ numero_2+" e "+numero_3)

    calcular_soma(numero_1, numero_2, numero_3)

def calcular_soma(n1,n2,n3):

    soma = n1 + n2 + n3
    print("A soma é: "  + soma)
    calcular_media(soma)

def calcular_media(soma):
    
    media = soma/3
    print("A média é: " + media)   

if(__name__== "__main__"):
    ler_numeros()
