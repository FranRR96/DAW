#Ejercicio 2.


numero = int(input("Dime un nº "))
anterior=0
while numero!=0:
    if numero>anterior:
        print("Es Creciente")
        anterior=numero
        numero=int(input("Dime un Nº: "))
    elif numero> anterior:
        print("Es creciente")
        anterior=numero
        numero=int(input("Dime un Nº: "))
    elif numero == anterior:
        print("Hay iguales.")
        anterior=numero
        numero=int(input("Dime un Nº: "))
    else:
        print("Desordenado")
        anterior=numero
        numero=int(input("Dime un Nº: "))
    print(numero)