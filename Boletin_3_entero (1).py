"""Boletin 3"""
"""1. Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par)."""

numero = int(input("dime un numero: "))

if numero % 2 ==0 :
    print("este numero es par")
else:
    print("este numero es impar")


"""2. Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo."""

numero_1 = int(input("dime un numero: "))
numero_2 = int(input("dime un numero: "))

if numero_1 == numero_2:
    print("son iguales")
elif numero_1 > numero_2:
    print("el numero 1 es mayor que el numero dos")
else:
    print("el numero 1 es menor que el numero 2")


"""3. Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje."""

numero = int(input("numero aleatorio: "))

if ((numero % 2) == 0 and (numero % 3 ==0)):
    print("El numero es múltiplo de 2 y de 3")

elif numero % 3 == 0:
    print("El número es múltiplo de 3")

elif numero % 2 == 0:
    print("el numero es múltiplo de 2")


"""4. Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto"""

edad = int(input("mi edad es: "))
edad < 100

if (edad >=0) and (edad <=12):
    print("es un niño")
elif (edad>=13) and (edad<=17):
    print("es un adolescente")
elif (edad>=18) and (edad<=29):
    print("es un joven")
else:
    print("es un adulto")


"""5. Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media."""

numero_1 = float(input("Dime un numero: "))
numero_2 = float(input("Dime un numero: "))
numero_3 = float(input("Dime un numero: "))
numero_4 = float(input("Dime un numero: "))
notaMedia = (numero_1 + numero_2 + numero_3 + numero_4) / 4

if numero_1 >= notaMedia:
   notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
   print(numero_1)
if numero_2 >= notaMedia:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
    print(numero_2)
if numero_3 >= notaMedia:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
    print(numero_3)
if numero_4 >= notaMedia:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
    print(numero_4)
elif notaMedia <= numero_1:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
    print(notaMedia)
elif notaMedia <= numero_2:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4) 
    print(notaMedia)
elif notaMedia <= numero_3:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4)
    print(notaMedia)
elif notaMedia <= numero_4:
    notaMedia = ((numero_1 + numero_2 + numero_3 + numero_4) / 4)
    print(notaMedia)

""""6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc."""

letra = str("dime una letra: ")

if letra == "A":
    print("Esta la primera vocal(A)")
elif letra == "E":
    print("Esta la segunda vocal (E)")
elif letra == "I":
    print("Esta la tercera vocal (I)")
elif letra == "O":
    print("Esta la cuarta vocal (O)")
elif letra == "U":
    print("Esta es la quinta vocal (U)")
else:
    print("esta letra no es una vocal")


"""7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%"""
estadoCivil = str((input("dime cual es su estado: ")))
edad= int(input("dime su edad: "))

if estadoCivil == ("soltero" or estadoCivil == "divorciado") and (edad < 35):
    print("12%")
elif (edad > 50):
    print("8.5%")
elif estadoCivil == ("viudo" or estadoCivil == "casado") and (edad < 35):
    print("11.3%")
else:
    print("10.5%")


"""8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor"""

hora_1 = int(input("dime una hora: "))
min_1 = int(input("dime un minuto: "))
seg_1 = int(input("dime un segundo: "))
hora_2 = int(input("dime una hora: "))
min_2 = int(input("dime un minuto: "))
seg_2 = int(input("dime un segundo: ")) 
horaEntera_1 = hora_1 * 3600 + min_1 * 60 + seg_1
horaEntera_2 = hora_2 * 3600 + min_2 * 60 + seg_2

if (hora_1 >= 0 and hora_1<= 23 ) and(min_1 >= 0 and min_1 <=59) and (seg_1 >= 0 and seg_1<=59) and (hora_2 >= 0 and hora_2<= 23 ) and(min_2 >= 0 and min_2 <=59) and (seg_2 >= 0 and seg_2<=59):
     horaEntera_1 = hora_1 * 3600 + min_1 * 60 + seg_1
     horaEntera_2 = hora_2 * 3600 + min_2 * 60 + seg_2
     if horaEntera_1 > horaEntera_2:
      print("La primera hora es mayor")
     else:
      print("La segunda hora es mayor")

else:
    print("Uno o más de los valores ingresados no son válidos")


"""9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error"""

productoPedido = str(input("Dime qué producto es: "))
precioPedido = float(input("¿Qué precio tiene? "))

if productoPedido == ("A"):
    precioDescuento = precioPedido - (precioPedido * 0.07)
    print (precioDescuento)
elif productoPedido == ("C") or productoPedido == ("B") and (precioPedido > 500):
    precioDescuento = precioPedido - (precioPedido * 0.12)
    print (precioDescuento)
elif productoPedido == ("B"):
    precioDescuento = precioPedido - (precioPedido * 0.09)
    print (precioDescuento)
else:
     print("Error: 404")

"""10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error."""

caracter = input("Ingresa un operador aritmético (+, -, /, **, %): ")
valid_operators = ['+', '-', '/', '**', '%']

if caracter not in valid_operators:
    print("Error: Operador inválido")
else:
    numeroEnt = int(input("Ingresa el primer número entero: "))
    numeroEnt_2 = int(input("Ingresa el segundo número entero: "))

    if caracter == '+':
        resultadoOperacion = numeroEnt + numeroEnt_2
    elif caracter == '-':
        resultadoOperacion = numeroEnt - numeroEnt_2
    elif caracter == '/':
        if numeroEnt_2 != 0:
            resultadoOperacion = numeroEnt / numeroEnt_2
        else:
            print("Error: No se permite la división por cero")
    elif caracter == '**':
        resultadoOperacion = numeroEnt ** numeroEnt_2
    elif caracter == '%':
        resultadoOperacion = numeroEnt % numeroEnt_2
    print("El resultado es: ", resultadoOperacion)