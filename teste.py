lista = [4, 3, 1, 9, 8, 7, 2, 5]

for passo in range(len(lista)-1,0,-1):

  for i in range(passo):
    if lista[i]>lista[i+1]:

     lista[i],lista[i+1]=lista[i+1],lista[i] 

     print(lista)

print(18/4, 18//4, 18%4)