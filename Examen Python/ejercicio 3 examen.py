#ejercicio 3

opcion = input("Dime si quieres añadir algun incidente: ")
contadorLeve = 0
contadorModerado= 0
contadorGrave=0
total =0
contadorEso= 0
contadorPostObligatoria= 0
while opcion=="S" and opcion !="N":
    partes = input("Dime que tipo de infraccion ha sido: ")
    nivelEstudios= input("Dime en que nivel está: ")
    if partes == "L":
        if nivelEstudios =="E":
            contadorLeve+=1
            contadorEso+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")
        elif nivelEstudios=="P":
            contadorLeve+=1
            contadorPostObligatoria+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")
    elif partes == "M":
        if nivelEstudios == "E":
            contadorModerado+=1
            contadorEso+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")
        elif nivelEstudios == "P":
            contadorModerado+=1
            contadorPostObligatoria+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")
    elif partes == "G":
        if nivelEstudios =="E":
            contadorGrave+=1
            contadorEso+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")
        elif nivelEstudios =="P":
            contadorGrave+=1
            contadorPostObligatoria+=1
            total+=1
            opcion = input("Dime si quieres añadir algun incidente más: ")
            partes = input("Dime que tipo de infraccion ha sido: ")
            nivelEstudios= input("Dime en que nivel está: ")

porcentajeEso= contadorEso*100/total
porcentajePostObligatoria = contadorPostObligatoria*100/total
print(f"Se han producido {total} incidentes en el centro: {contadorLeve} de ellos Leves, {contadorModerado} Moderados y {contadorGrave} Graves, siendo el {porcentajeEso}% en Eso y el {porcentajePostObligatoria}% en Post-Obligatoria")
