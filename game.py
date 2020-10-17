#guessing games
#import random

#random cifra
cifra = 7


#rounds
for i in range(0,9):
    vnos = input("Vnesi stevilko:")
    vnos = int(vnos)
    if vnos == cifra:
        print("bravo")
        break
    else: 
        print("try again")
        

