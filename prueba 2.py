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


player1= input("Dime que va a elegir Player 1: ")
player2= input("Dime que va a elegir Player 2: ")




while (player1 != "tijera" and player1 != "papel" and player1 != "lagarto" and player1 != "spock") and (player2 != "tijera" and player2 != "papel" and player2 != "lagarto" and player2 != "spock"):
    print("Esa respuesta no es valida")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if (player1 == "spock") and (player2 == "spock"):
    print("Fin")
if player1 == "tijera" and player2 == "papel":
    print("Tijera corta Papel")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "tijera" and player2 == "lagarto":
    print("Tijera corta Lagarto")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "spock" and player2 == "tijera":
    print("Spock rompe a Tijera")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "spock" and player2 == "piedra":
    print("Spock vaporiza a Piedra")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "papel" and player2 == "spock":
    print("Papel desautoriza a Spock")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "papel" and player2 == "piedra":
    print("Papel envuelve a Piedra")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")

if player1 == "lagarto" and player2 == "spock":
    print("Lagarto envenena a Spock.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")

if player1 == "lagarto" and player2 == "papel":
    print("Lagarto devora a Papel.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player1 == "piedra" and player2 == "lagarto":

    print("Piedra aplasta a Lagarto.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")

if player2 == "tijera" and player1 == "papel":
    print("Tijera corta a Papel")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "tijera" and player1 == "lagarto":
    print("Tijera corta a Lagarto")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "spock" and player1 == "tijera":
    print("Spock rompe a Tijera")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "spock" and player1 == "piedra":
    print("Spock vaporiza a Piedra")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "papel" and player1 == "spock":
    print("Papel desautoriza a Spock")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "papel" and player1 == "piedra":
    print("Papel envuelve a Piedra")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "lagarto" and player1 == "spock":
    print("Lagarto envenena a Spock.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "lagarto" and player1 == "papel":
    print("Lagarto devora a Papel.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")
if player2 == "piedra" and player1== "lagarto":
    print("Piedra aplasta a Lagarto.")
    player1= input("Dime que va a elegir Player 1: ")
    player2= input("Dime que va a elegir Player 2: ")