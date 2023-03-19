nome = ""
altura = 0
peso = 0
imc = 0
N

def le_dados():
    global nome
    global peso
    global altura

    nome= input("Digite o seu nome:")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

def calcula_imc():
    global peso
    global altura

    imc = peso/pow(altura,2)
    return round (imc,2)

def avalia_imc():
    imc = calcula_imc()
    
    if imc < 18.5:
     return "abaixo do peso ideal"
    
    elif imc >= 18.5 and imc < 25:
       return "peso ideal"
    
    else:
       return "sobrepeso"
    

le_dados()   
imc = calcula_imc()
msg =avalia_imc()

print("%s tem IMC de: %.2f e está %s" % (nome, imc, msg))
