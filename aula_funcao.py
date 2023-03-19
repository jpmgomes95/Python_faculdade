def ler_numeros():

    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o Segundo número: "))
    n3 = float(input("Digite o terceiro núnmero: "))

    print(f"O primeiro número é: %2.f" %n1)
    print(f"O segundo número é:  %2.f" %n2)
    print(f"O terceiro número é:  %2.f" %n3)
    
    calcular_soma(n1, n2, n3)

def calcular_soma(n1,n2,n3):

    soma = n1 + n2 + n3
    print(f"A soma é: %2.f" %soma)
    calcular_media(soma)

def calcular_media(soma):
    
    media = soma/3
    print(f"A média é: %2.f" %media)   

if(__name__== "__main__"):
     
     n1 = 0
     n2 = 0
     n3 = 0
     ler_numeros()
