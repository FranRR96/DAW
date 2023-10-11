""""
sexo = "H"
edad = 27
lenguajeProgramacion = "java"
cantidadPersonas = 1250
mediaEdad = 0
mediaEdadTotal = mediaEdad / cantidadPersonas
while cantidadPersonas<=0:
    print("Vuelve a introducir los datos")
    sexo = (input("Dime el sexo: "))
    edad = int(input("Dime una edad: "))
    lenguajeProgramacion = (input("¿Que lenguaje de programacion utilizas? "))



"""





MENUPRINCIPAL= '''
########~######################
#Bienvenido al IES Jacarandá  #
    1. Alumnos que han entrado:
    2. Alumnos que han salido:
    3. Alumnos en el IES:
    4. Salir.
################################
'''
print(MENUPRINCIPAL)
total=4000
opcion = int(input("Dime que opción deseas elegir? "))
while opcion !=4:
    if opcion == 1:
        alumnosEntrar = int(input("Cuantos alumnos van a entrar?: "))
        total+=alumnosEntrar
        opcion = int(input("Dime que opción deseas elegir? "))
    if opcion == 2:
        alumnosSalir = int(input("Cuantos alumnos van a salir?: "))
        total-=alumnosSalir
        opcion = int(input("Dime que opción deseas elegir? "))
    if opcion ==3:
        print(f"Hay actualmente en el IES Jacaranda {total}")
        opcion = int(input("Dime que opción deseas elegir? "))



#excersise1
resultado = ""

player1= input("Dime que va a elegir Player 1: ")

#comprobacion de datos

while (player1 != "tijera" and player1 != "papel" and player1 != "lagarto" and player1 != "spock"):
    print("Esa respuesta no es valida")    
    player1= input("Dime que va a elegir Player 1: ")

player2= input("Dime que va a elegir Player 2: ")
while (player2 != "tijera" and player2 != "papel" and player2 != "lagarto" and player2 != "spock"):
    print("Esa respuesta no es valida")
    player2= input("Dime que va a elegir Player 2: ")

#Aqui comprobamos quien es el ganador 
if player1 == player2:
        print("Los jugadores han emptadao")
elif player1 == "spock":
    if player2 =="tijera" or player2 =="piedra":
        resultado = f"el player 1 {player1} ha ganado a player 2 {player2}"
    else:
         resultado = f"el player 2 {player2} ha ganado a player 1 {player1}"
elif player1 =="tijera":
    if player2 == "papel" or player2 =="lagarto":
        resultado = f"el player 1 {player1} ha ganado a player 2 {player2}"
    else:
        resultado = f"el player 2 {player2} ha ganado a player 1 {player1}"
elif player1== "papel":
    if player2 == "piedra" or player2 == "spock":
          resultado = f"el player 1 {player1} ha ganado a player 2 {player2}"
    else:
      resultado = f"el player 2 {player2} ha ganado a player 1 {player1}"

print(resultado)