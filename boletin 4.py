"""1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""

import math
cateto_1 = float(input("dime cuanto mide el lado: "))
cateto_2 = float(input("dime cuanto mide el lado: "))
hipotenusa = math.sqrt((cateto_1**2) + (cateto_2**2))
print(hipotenusa)

"""2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""


gradoCelsius = float(input("dime un numero: "))
gradosFarenheit = (gradoCelsius *(9 /5) +32 )
print(gradosFarenheit)


"""3. Calcular la media de tres números pedidos por teclado"""


numero_1 = float(input("dime un numero: "))
numero_2 = float(input("dime un numero: "))
numero_3 = float(input("dime un numero: "))
numeroMedia = ((numero_1 + numero_2 + numero_3)/3)
print(numeroMedia)

"""4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra."""


precioProducto = float(input("dime un numero: "))
descuento = 0.15
precioDescuento = precioProducto * descuento
precioFinal = precioProducto - precioDescuento

print(precioFinal)

"""5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo)."""

numero_1= float(input("dime un numero: "))
numero_2= float(input("dime un numero: "))
resultadoOperacion = (numero_1 - numero_2)
valorAbsoluto = abs(resultadoOperacion)
if resultadoOperacion > 0:
    print(valorAbsoluto)
else:
    print("esta distancia es negativa")


"""6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos"""

import math

numero = float(input("Dime un nº: "))

raiz_cuadrada = math.sqrt(numero)

raiz_cubica = numero ** (1/3)

print("La raiz cuadrada:", raiz_cuadrada)
print("La raiz cubica: ", raiz_cubica)



"""7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular"""

import math

numero = float(input("Dime un nº: "))

raiz_cuadrada = math.sqrt(numero)

raiz_cubica = numero ** (1/3)

print(raiz_cuadrada)
print(raiz_cubica)

"""8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos)"""

euros_2 = int(input("Cuantos euros son: "))
euros_1 =  int(input("Cuantos euros son: "))
centimos_50 = int(input("Cuantos euros son: "))
centimos_20 = int(input("Cuantos euros son: "))
centimos_10 = int(input("Cuantos euros son: "))

totalEuros = euros_2 *2 + euros_1

centimos_totales = (centimos_10 * 10) + (centimos_20 * 20) + (centimos_50 * 50)

print(f"Tienes {totalEuros} euros y {centimos_totales} centimos")


"""9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

numero = float(input("Dime un nº: ",))
exponente = float(input("Dime un nº: ",))
if exponente > 0:
    print(pow(numero, exponente))
elif exponente == 0:
    print(pow(numero, exponente))
elif exponente < 0:
    resultado = 1 / pow(numero, abs(exponente))
    print(resultado)

"""10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno"""

tipoA = float(input("¿Cuanto mide?: "))
tipoB = float(input("¿Cuanto mide?: "))
tipoC = float(input("¿Cuanto mide?: "))

if (tipoA ** 2 == tipoB ** 2 + tipoC ** 2):
    print("Es un triángulo rectángulo") 
elif tipoA != tipoB != tipoC:
    print("Es un triágulo escaleno")
elif tipoA == tipoB == tipoC:
    print("Es un triángulo equilatero.")
else:
    print("Es un triágulo isóceles")


"""11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400."""

año = int(input("Dime que año quieres comprobar:"))

if año% 4 ==0 and año%100!=0 or año% 400==0:
    print("Es bisiesto")
else:
    print("Este año no es bisiesto")



"""12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. 
Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: 
si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2.
Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida."""


precioKilo = float(input("Cuanto vale el kilo?: "))
ganancia = 0

tipoUva = (input("Dime que tipo de uva es: "))
while tipoUva != "a" and tipoUva != "b":
    print("Te has equivocado")
    tipoUva = (input("Dime que tipo de uva es: "))

tamañoUva =int(input("Dime el tamañao de la uva: "))

while tamañoUva != 1 and tamañoUva != 2:
    print("Te has equivocado")
    tamañoUva =int(input("Dime el tamañao de la uva: "))

if tipoUva == "a":
    if tamañoUva ==1:
        ganancia+=0.20
        print(f"La ganancia o perdida sería de {ganancia}")
        print(f"El precio total sería de {precioKilo +ganancia}")
    else:
        ganancia+=0.30
        print(f"La ganancia o perdida sería de {ganancia}")        
        print(f"El precio total sería de {precioKilo +ganancia}")
if tipoUva == "b":
    if tamañoUva== 1:
        ganancia-=0.30
        print(f"La ganancia o perdida sería de {ganancia}")        
        print(f"El precio total sería de {precioKilo -ganancia}")
    else:
        ganancia-=0.50
        print(f"La ganancia o perdida sería de {ganancia}")        
        print(f"El precio total sería de {precioKilo -ganancia}")

"""13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje."""
numeroAlumnos = int(input("Cuantos alumnos van a ir al viaje?"))

if numeroAlumnos > 100:
    rentaAutobus = numeroAlumnos*65
    print(f"El coste por alumno es de 70 euros y el coste del autobus es {rentaAutobus}")
elif numeroAlumnos >=50 and numeroAlumnos <100:
    rentaAutobus = numeroAlumnos*70
    print(f"El coste por alumno es de 70 euros y el coste del autobus es {rentaAutobus}")
elif numeroAlumnos >=30 and numeroAlumnos <50:
    rentaAutobus = numeroAlumnos*95
    print(f"El coste por alumno es de 95 euros y el coste del autobus es {rentaAutobus}")
else:
    rentaAutobus= 4000
    pagoAlumno = rentaAutobus / numeroAlumnos
    print(f"El coste por alumno es de {pagoAlumno} euros y el coste del autobus es {rentaAutobus}")


"""14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada"""

sumaDinero= 0
minutos = int(input("Cuantos minutos ha hablado: "))
dia = input("Dime que dia es cuando habla: ")
tramoHorario = input("Dime que hora del dia es cuando habla: ")

if minutos >1 and minutos <= 5:
    sumaDinero+=1
    if dia == "domingo":
        sumaDinero+=sumaDinero*0.03
        print(sumaDinero)
    elif tramoHorario== "tarde":
        sumaDinero+=sumaDinero*0.10
        print(sumaDinero)
    elif tramoHorario == "mañana":
        sumaDinero+=sumaDinero*0.15
        print(sumaDinero)

elif minutos >5 and minutos <= 8:
    sumaDinero+=1.80
    if dia == "domingo":
        sumaDinero+=sumaDinero*0.03
        print(sumaDinero)
    elif tramoHorario== "tarde":
        sumaDinero+=sumaDinero*0.10
        print(sumaDinero)
    elif tramoHorario == "mañana":
        sumaDinero+=sumaDinero*0.15
        print(sumaDinero)

elif minutos >8 and minutos <= 10:
    sumaDinero+=2.50
    if dia == "domingo":
        sumaDinero+=sumaDinero*0.03
        print(sumaDinero)
    elif tramoHorario== "tarde":
        sumaDinero+=sumaDinero*0.10
        print(sumaDinero)
    elif tramoHorario == "mañana":
        sumaDinero+=sumaDinero*0.15
        print(sumaDinero)
else:
    sumaDinero+=3
    if dia == "domingo":
        sumaDinero+=sumaDinero*0.03
        print(sumaDinero)
    elif tramoHorario== "tarde":
        sumaDinero+=sumaDinero*0.10
        print(sumaDinero)
    elif tramoHorario == "mañana":
        sumaDinero+=sumaDinero*0.15
        print(sumaDinero)


"""15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error"""


numeroDiaSemana = int(input("Dime un nº del 1 al 7: "))

if numeroDiaSemana == 1:
    print("El dia elegido es Lunes.")
elif numeroDiaSemana == 2:
    print("El numero elegido es Martes.")
elif numeroDiaSemana == 3:
    print("El numero elegido es Miercoles.")
elif numeroDiaSemana == 4:
    print("El numero elegido es Jueves.")
elif numeroDiaSemana == 5:
    print("El numero elegido es Viernes.")
elif numeroDiaSemana == 6:
    print("El numero elegido es Sábado.")
elif numeroDiaSemana == 7:
    print("El numero elegido es Domingo.")
else:
    print("Error")

"""16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente"""

mes = int(input("Dime un numero del mes."))

if mes == 1:
    print("El mes tiene 31 días")
elif mes == 2:
    print("El mes tiene 28 dias.")
elif mes == 3:
    print("El mes tiene 31 dias.")
elif mes == 4:
    print("El mes tiene 30 dias.")
elif mes == 5:
    print("El mes tiene 31 dias.")
elif mes == 6:
    print("El mes tiene 30 dias.")
elif mes == 7:
    print("El mes tiene 31 dias.")
elif mes == 8:
    print("El mes tiene 31 dias.")
elif mes == 9:
    print("El mes tiene 30 dias.")
elif mes == 10:
    print("El mes tiene 31 dias.")
elif mes == 11:
    print("El mes tiene 30 dias.")
elif mes == 12:
    print("El mes tiene 31 dias.")
else:
    print("Error")



"""17. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario"""



numero_1 = int(input("Dime un numero: "))
numero_2 = int(input("Dime un numero: "))

for i in range(numero_1, numero_2+1):
    if i %2==0:
        print(f"Este numero {i} es par.")
    else:
        print(f"Este numero {i} es impar.")


"""18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo."""


limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
limite_superior = int(input("Introduce el límite superior del intervalo: "))

while limite_inferior > limite_superior:
    print("El límite inferior no puede ser mayor que el límite superior.")
    limite_inferior = int(input("Introduce el límite inferior del intervalo: "))
    limite_superior = int(input("Introduce el límite superior del intervalo: "))
numero = int(input("Introduce un nº: "))
suma_intervalo = 0
fuera = 0
coincide = 0
while numero != 0:
    if limite_inferior< numero< limite_superior:
        suma_intervalo+= numero
        numero = int(input("Introduce un nº: "))
    elif numero == limite_inferior or numero ==limite_superior:
        coincide+=1
    else:
        fuera+=1
print(f"La suma de los números dentro del intervalo es: {suma_intervalo}")
print(f"Los numeros fuera del intervalo son: {fuera}")
print(f"Hay {coincide} que coincide o coinciden.")

"""19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia."""
import math
numero = int(input("Dime un numero: "))
exponente = int(input("Dime el exponente: "))

while exponente < 0:
    print("No se puede utilizar el operador de potencia.")
    exponente = int(input("Introduce el exponente correcto: "))
if exponente > 0:
    print(pow(numero, exponente))


"""20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses"""

pagoInicial = 10
pagoMensual = pagoInicial
meses = 20
pagoTotal = pagoMensual
for i in range(1,20):
  print(f"El pago del mes {i} es: {pagoMensual} €")
  i+=1
  pagoMensual *= 2
  if i >=20:
    print(f"el pago total sera {pagoMensual* meses}")


"""21. Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad de
números primos que queremos mostrar"""


#Esta actividad no he podido resolverla Jose Manuel.

numero = int(input("Dime que numero vas a utilizar: "))

for i in range(2,numero):
    if numero % i ==0:
        print(f"el nº {i} es primo")
    else:
        print(f"el nº {i} no es primo.")



