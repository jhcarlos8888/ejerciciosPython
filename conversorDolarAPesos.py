dolaresIngresados = input("Ingrese el valor de dolares a convertir en pesos: ")
dolaresIngresados = float(dolaresIngresados)
valorActualEnPesos = 5100

cantidadPesos = dolaresIngresados * valorActualEnPesos
cantidadPesos = int(cantidadPesos)
cantidadPesos = str(cantidadPesos)

print("Su conversion de dolares a pesos es: $ " + cantidadPesos + " pesos")