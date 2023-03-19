
temperatura = float(input("Qual é a temperatura: "))

if temperatura < 7:
    print("Congelando")

elif temperatura >=7 and temperatura <10:
    print("Frio")
elif temperatura >= 10 and temperatura < 26:
    print("Ótimo")
else:
    print("Muito Quente!")        