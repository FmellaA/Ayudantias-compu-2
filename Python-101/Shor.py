#extrapolación del algoritmo de Shor
#muestra el producto de numeros primos para un numero natural cualquiera
num_primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
N = int(input("Ingrese un número entre 1 y 60: ")) #resultado A 

producto = []
for a in num_primos: 
    for b in num_primos:
            for c in num_primos: 
                  for d in num_primos: 
                        for e in num_primos:   
                            if a*b*c*d*e ==N:                                  
                                producto = [a,b, c, d, e]  #lista con numeros de productos
#se deja una unica lista, para la primera lista de elementos que lo cumple, porque va a ser una combinación única. 

P = []
for i in producto: # elimina los unos extras
    if not i==1: 
        P.append(i)
P = P + [1]

# stg = ''
# for i in range(len(P)-1): 
#      stg = f'{P[i]}'+ '*' + stg
# stg = stg + f'{P[-1]}'
# print(f'{stg} = {N}')

#Armamos los dos factores B y C a partir de lo que esta en la lista P

if len(P) == 6: 
    print(f"{P[0]*P[1]*P[2]}*{P[3]*P[4]*P[5]}") 
elif len(P) == 5: 
    print(f"{P[0]*P[1]*P[2]}*{P[3]*P[4]}")
elif len(P) ==4: 
    print(f"{P[0]*P[1]}*{P[3]*P[2]}")
elif len(P) ==3: 
    print(f"{P[0]*P[1]}*{P[2]}")
elif len(P) ==2: 
    print(f"{P[0]}*{P[1]}")
