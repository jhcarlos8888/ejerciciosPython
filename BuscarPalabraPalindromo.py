def palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else: 
        return False
    

def run():
    palabra = input("Escribe una palabra: ")
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print("Es una palabra palindromo")
    else:
        print("No es un palindromo")


if __name__ == "__main__":
    run()

