


def run():
    LIMITE = 100

    contador = 0

    potencia2 = 2**contador

    while contador <= LIMITE:
        print("El resultado de 2 elevado a " + str(contador) + " daria : " + str(potencia2))
        contador = contador + 1 
        potencia2 = 2**contador

    

if __name__ == "__main__":
    run()


