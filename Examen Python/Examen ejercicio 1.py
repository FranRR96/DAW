#ejercicio 1
cantidadnumeros= 3
numero1= int(input("Dime que numero mayor que 0"))
numero2= int(input("Dime que numero mayor que 0"))
numero3= int(input("Dime que numero mayor que 0"))
while (numero1 >0 and numero2>0) or (numero3>0 and numero2>0) or (numero3>0 and numero1>0):
    if numero1< numero2 and numero2 < numero3 and numero1 < numero3:
        print(f"{numero1}, {numero2}, {numero3}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))
    elif numero1< numero2 and numero2 > numero3 and numero2 > numero1:
        print(f"{numero1}, {numero3},{numero2}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))
    elif numero3< numero1 and numero1> numero2 and numero1 > numero3:
        print(f"{numero3, {numero2}, {numero1}}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))
    elif numero3< numero2 and numero2> numero1 and numero1 > numero3:
        print(f"{numero3, {numero1}, {numero2}}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))
    elif numero2 < numero1 and numero1 > numero3 and numero1> numero2:
        print(f"{numero2}, {numero3}, {numero1}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))
    elif numero2 < numero3 and numero3 > numero1 and numero3 > numero2:
        print(f"{numero2}, {numero1}, {numero3}")
        numero1= int(input("Dime que numero mayor que 0"))
        numero2= int(input("Dime que numero mayor que 0"))
        numero3= int(input("Dime que numero mayor que 0"))


