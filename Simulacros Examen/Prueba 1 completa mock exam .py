#exercise3
cantidadJavaHombre =0
cantidadJavaMujer =0
cantidadPythonHombre =0
cantidadPythonMujer =0
porcentajePython=0
contadorHombres = 0
contadorMujer = 0
contadorJava = 0
contadorPython =0
contadorLenguaje = 0
cantidadPersonas = int(input("Cuantas personas trabajan en la empresa? "))
contadorEdad = 0
while cantidadPersonas<=0:
    print("Vuelve a introducir los datos")
    cantidadPersonas = int(input("Cuantas personas trabajan en la empresa? "))

for i in range(cantidadPersonas):
    edad = int(input("Dime una edad: "))
    while edad < 18 or edad > 65:
        print("Vuelve a introducir los datos")
        edad = int(input("Dime una edad correcta: "))
    contadorEdad+=edad

    sexo = (input("Dime si es H o M: "))
    if sexo == "H":
        contadorHombres+=1
    elif sexo == "M":
        contadorMujer+=1
    while sexo != "H" and sexo != "M":
        print("Dime el sexo correcto: ")
        sexo = (input("Dime si es H o M: "))
        if sexo == "H":
            contadorHombres+=1
        elif sexo == "M":
            contadorMujer+=1

    lenguajeProgramacion = (input("Dime que lenguaje utilizan? "))
    if lenguajeProgramacion == "java":
            contadorJava+=1
    elif lenguajeProgramacion == "python":
            contadorPython+=1
    while lenguajeProgramacion != "java" and lenguajeProgramacion != "python":
        print("No es el lenguaje correcto")
        lenguajeProgramacion = (input("Dime que lenguaje es correcto? "))
        if lenguajeProgramacion == "java":
            contadorJava+=1
        elif lenguajeProgramacion == "python":
            contadorPython+=1

    if sexo == "H" and lenguajeProgramacion == "java":
        cantidadJavaHombre+=1
    elif sexo == "H" and lenguajeProgramacion == "python":
        cantidadPythonHombre+=1
    elif sexo== "M" and lenguajeProgramacion == "java":
        cantidadJavaMujer+=1
    elif sexo== "M" and lenguajeProgramacion == "python":
        cantidadPythonMujer


porcentajeJava = (contadorJava/ cantidadPersonas)*100

porcentajePython = (contadorPython/ cantidadPersonas)*100

print(f"El {porcentajePython}% utiliza Python de los que {cantidadPythonHombre} hombres y {cantidadPythonMujer} mujeres y su edad media {contadorEdad/cantidadPersonas}")
print(f"El {porcentajeJava}% utiliza Python de los que {cantidadJavaHombre} hombres y {cantidadJavaMujer} mujeres y su edad media {contadorEdad/cantidadPersonas}")





#excersise2

MENUPRINCIPAL= '''
########~######################
#Bienvenido al IES Jacarandá: #
    1. Alumnos que han entrado:
    2. Alumnos que han salido:
    3. Alumnos en el IES:
    4. Salir.
################################
'''
print(MENUPRINCIPAL)
total=4000
opcion = int(input("Dime que opción deseas elegir? "))
while opcion <=4 and opcion !=4:
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

while (player1 != "tijera" and player1 != "papel" and player1 != "lagarto" and player1 != "spock" and player1!= "piedra"):
    print("Esa respuesta no es valida")    
    player1= input("Dime que va a elegir Player 1: ")

player2= input("Dime que va a elegir Player 2: ")
while (player2 != "tijera" and player2 != "papel" and player2 != "lagarto" and player2 != "spock" and player2!= "piedra"):
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
elif player1 == "piedra":
    if player2 == "tijera" or player2 == "lagarto":
        resultado = f"el player 1 {player1} ha ganado a player 2 {player2}"
    else:
      resultado = f"el player 2 {player2} ha ganado a player 1 {player1}"
elif player1 == "lagarto":
    if player2 == "papel" or player2 =="Spock":
        resultado = f"el player 1 {player1} ha ganado a player 2 {player2}"
    else:
      resultado = f"el player 2 {player2} ha ganado a player 1 {player1}"
print(resultado)
