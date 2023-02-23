def conversor (tipoPesos, valorDolar):

    pesosIngresados = input("Ingrese el valor de pesos " + tipoPesos +  " a convertir en dolares: ")
    pesosIngresados = float(pesosIngresados)
    cantidadDolares = pesosIngresados / valorDolar
    cantidadDolares = round(cantidadDolares, 2)
    cantidadDolares = str(cantidadDolares)

    print("Su conversion de pesos a dolares es: $ " + cantidadDolares + " dolares")



menu = """
Bienvenido al conversor de monedas 

1- Pesos colombianos
2- Pesos argentinos
3- Pesos mexicanos

Elige una opcion: 
"""
opcion = input(menu)

if opcion == "1":
    conversor("Colombianos", 3875)

elif opcion == "2":
    conversor("Argentinos", 65)

elif opcion == "3":
    conversor("Mexicanos", 24)

else:
    print("ingresa una opcion correcta")



