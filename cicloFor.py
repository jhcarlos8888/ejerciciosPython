
def run():
    numero = int(input("Ingresa el numero de la tabla de multiplicar: "))
    for contador in range (1,11):
        print (str(numero) + " x " + str(contador) + " = " + str(numero * contador))


if __name__ == "__main__":
    run()
    

