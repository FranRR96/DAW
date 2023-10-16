
menuPrincipal= '''##################################
####################################################
    A) Añadir cliente.
    B) Mostrar los porcentajes de los clientes premium y normales.
    C) Visualizar calculos de clientes premium
    G) Salir. 
####################################################
'''
print(menuPrincipal)
opcion= input("Dime una opción: ")


contadoPrecioProducto= 0
precioGastadoCliente=0
clientePremium= 0
clienteNormal=0
contadorTotal =0
totalPrecio=0
articuloMasCaro=0
importeMaximo =0

while opcion != "G":
    if opcion!="A" and opcion!= "B" and opcion!="C" and opcion!="D":
        print("esa no es la opción correcta")
        opcion= input("Dime una opción: ")
    if opcion == "A":
        cliente = (input("Dime si es Premium o no(Y/N) "))
        clienteCorreoElectronico= input("Dime el email del cliente?: ")
        codigoArticulo= int(input("Dime el codigo hasta llegar a cero: "))
        unidad= int(input("Cuantas unidades han entrado: "))
        precioUnitario= int(input("Dime cual ha sido el precio por unidad"))
        if cliente =="Y":
            clientePremium+=1
            contadorTotal+=1
            opcion=input("Dime que opcion quieres?: ")
        elif cliente=="N":
            clienteNormal+=1
            contadorTotal+=1
            opcion=input("Dime que opcion quieres?: ")
    elif opcion =="B":
            clientePremiumPorcentaje= (clientePremium / contadorTotal)*100
            print(f"El numero total de clientes premium es {clientePremiumPorcentaje}%")
            clienteNormalPorcentaje = (clienteNormal/contadorTotal*100)
            print(f"El numero total de clientes premium es {clienteNormalPorcentaje}%")
            opcion= input("Dime una opción: ")
    elif opcion == "C":
        clientePremiumPorcentaje= (clientePremium / contadorTotal)*100
        print(f"El numero total de clientes premium es {clientePremiumPorcentaje}%")
        importeCliente= precioUnitario* unidad
        if importeCliente>importeMaximo:
            importeMaximo = importeCliente
            print(f"El importe más grande es {importeMaximo} y su codigo es {codigoArticulo}")
            opcion=input("Dime que opcion quieres?: ")
        elif precioUnitario>articuloMasCaro:
            articuloMasCaro = precioUnitario
            print(f"El articulo más caro entre los premiums es {articuloMasCaro}")
            opcion=input("Dime que opcion quieres?: ")
    elif opcion == "D":
        clienteNoPremiumPorcentaje= (clienteNormal / contadorTotal)*100
        print(f"El numero total de clientes NoPremium es {clienteNoPremiumPorcentaje}%")
        importeClienteNoPremium= precioUnitario* unidad
        if importeClienteNoPremium>importeMaximo:
            importeMaximo = importeClienteNoPremium
            print(f"El importe más grande es {importeMaximo} y su codigo es {codigoArticulo}")
            opcion=input("Dime que opcion quieres?: ")
        elif precioUnitario>articuloMasCaro:
            articuloMasCaro = precioUnitario
            print(f"El articulo más caro entre los premiums es {articuloMasCaro}")
            opcion=input("Dime que opcion quieres?: ")
    elif opcion=="E":
        precioGastadoCliente=unidad* precioUnitario
        if precioGastadoCliente>contadoPrecioProducto:
            contadoPrecioProducto= precioGastadoCliente
            print(f"El usuario que mas ha gastado ha sido {clienteCorreoElectronico} con una cantidad de {precioGastadoCliente} €")
