"""Solve the next problems with flowchart and pseudocode
1. Diseñe un programa para mostrar todos los números entre 1 y 100. Si el número es un
múltiplo de 7 deberías mostrar el mensaje "El número xx es múltiplo de 7". Si el
número es múltiplo de 13 debería mostrar el mensaje "El número xx es un
múltiplo de 13". Si el número es múltiplo de 7 y 13, debes mostrar ambos
mensajes."""

numero = int(input("Dime un nº: "))

for numero in range (numero, 101):
    print(numero)
    while numero % 7 == 0 and numero % 13== 0:
            print(f"el numero {numero} es multiplo de 7")
            print(f"el numero {numero} es multiplo de 13")
            numero+=1
    if numero % 7 == 0:
        print(f"el numero {numero} es multiplo de 7")
    if numero % 13 == 0:
        print(f"el numero {numero} es multiplo de 13")

"""2. Diseñar un programa para leer un número entero entre 0 y 10 y mostrar la tabla de multiplicar.
Para solicitar el número deberá mostrar el siguiente mensaje "Ingrese un número
entre 0 y 10”. Si el número está fuera de los límites, el programa debería mostrar
el mensaje "El número está fuera de los límites". Si el número es válido, debería
muestra la tabla de tiempos siguiendo el siguiente formato:
7*1=7
...
7*10=70"""
i=0
i+=1
numero = int(input("Ingrese un número entre 0 y 10: "))
while numero >10 or numero< 0:
    print("El número está fuera de los límites")
    numero = int(input("Ingresa el nº correcto: "))
for i in range(0,11):
    print(f"{numero} multiplicado por {i} es = {numero * i} ")
    i+=1

"""3. Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”"""


cantidadNumeros = int(input("Cuantos numeros quieres ingresar ?: "))

while cantidadNumeros <= 0:
    print("El número no es válido, debe ser mayor que 0")
    cantidadNumeros = int(input("Cuantos numeros quieres ingresar ?: "))

for i in range(cantidadNumeros):
    numero= int(input("Dime que numero quieres saber si es impar: "))
    while numero <= 0:
        print("El número no es válido, debe ser mayor que 0")
        numero = int(input("Cuantos numeros quieres ingresar ?: "))
    if numero %2==0:
        print(f"El nº {numero} es par")
    else:
        print(f"El nº {numero} es impar")


"""4. Design a program that reads a positive number N greater than 0 and show the result
of the sum of the N numbers between 1 and N. If the number N is not valid, the
program should ask for it again. The messages are the following:
“Enter one number greater than 0:”
“The number is not right, try again.”
“The sum of the N first numbers is XX."""


numero = int(input("Dime un numero: "))
i = int(input("Hasta cual es: "))
while numero<=0:
    print("he number is not right, try again.")
    numero = int(input("Dime un numero: "))

    for numero in range(i):
        numero+=1
   
print(f"The sum of the {numero} + {i}  is {numero+i}")   


 

"""5. Design a program that asks for numbers until the user inputs a negative one. When
this happens, the program will show how many positive numbers have been
introduced by the user. The messages are the following:
“Enter a number (negative to finish):” 
“You have entered XX positive numbers.”"""

numero = int(input("Dime un nº: "))
suma=0
while numero!=0 or numero<0:
    print("Enter a number")
    suma+=numero
    numero = int(input("Dime un nº: "))
if numero>0:
    ("Finish")
print(f"The sum is {numero + suma} positive numbers")


"""6. Design a program that reads two integer numbers, for example numberA and
numberB, and calculates the product of both numbers without use multiplication, but
using the sum. The messages are the following:
“Enter one number:”
“The product is XX”"""

numeroA = int(input("Dime un nº: "))
numeroB = int(input("Dime un nº: "))



"""7. Design a program that asks how many numbers the user wants to write. After the
user enters all numbers, the program should say the medium of the numbers. If the
user inputs a wrong number, the program should ask for it again. The messages are
the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The medium is XX.XX” to show the result."""

cantidadNumeros = int(input("Cuantos numeros quieres ingresar ?: "))
total= 0
while cantidadNumeros <= 0:
    print("El número no es válido, debe ser mayor que 0")
    cantidadNumeros = int(input("Cuantos numeros quieres ingresar ?: "))
for i in range(cantidadNumeros):
    numero= int(input("Dime que numero quieres introducir: "))
    total +=numero
    while numero <= 0:
        total+=numero
        print("El número no es válido, debe ser mayor que 0")
        numero = int(input("Dime que nº quieres introducir?: "))
if total!=0:
    print(f"The medium is {total / 2} to show the result")

"""8. Diseña un programa que pida un conjunto de números. Después de introducir cada número, el programa debe preguntar "
¿Desea introducir más números (S/N)?". Si la respuesta es "S" el programa pide otros números. Cuando el usuario termina de introducir todos los números, 
el programa debe decir cuál es el más pequeño.
 Los mensajes son los siguientes
"Introduzca un número:"
"¿Desea introducir más número (Y/N)?"
"El número más pequeño es XX”"""

cantidadNumeros = int(input("Cuantos numeros quieres ingresar ?: "))
total= 0
respuesta= "Y"
while cantidadNumeros<0:
    numeroIngresar = int(input("Introduzca un numero: "))
    total+=numeroIngresar
    print(str(input("¿Desea introducir más número (Y/N)? ")))
    if respuesta == "Y":
        numeroIngresar = int(input("Introduzca un numero: "))
    else:
        print(total)



"""9. Design a program that reads an integer positive number greater than 0 and says if
it’s a “perfect number”. A number is perfect if it is equal to the sum of all its divisors.
The messages are the following:
“Enter an integer positive number greater than 0:”
“The number is not valid, try again.”
“The number is perfect.”
“The number is not perfect.”"""


number = int(input("Enter an integer positive number greater than 0: "))

while number <0:
    print("The number is not valid, try again.")
    number = int(input("Enter an integer positive number greater than 0: "))
if number >0 or number / 1==1 and number / 2==1 and number / 6 ==1:
        print("The number is perfect.")
else:
    print("The number is not perfect.")



"""10. Design a program that reads an integer positive number and says the “factorial” of
the number. To calculate the factorial you should know that
FACT(0)= 1
FACT(1) =1
FACT(N)= N*(N-1)*(N-2)*....1
The messages are the following:
“Enter an integer positive number:”
“The number is not valid, try"""



