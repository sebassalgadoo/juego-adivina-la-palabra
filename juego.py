import random

palabras = ["hola", "avión", "cocodrilo", "coches", "nvidia", "pan"]
palabra = random.choice(palabras)
adivinalapalabra = ["_"] * len(palabra)
attempts = 10

while attempts > 0:
    print('\nPalabra actual: ' + ' '.join(adivinalapalabra))
    
    adivina_letra = input("Di una letra: ").lower()
    
    if adivina_letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == adivina_letra:
                adivinalapalabra[i] = adivina_letra
        print("¡Bien hecho!")
    else:
        attempts -= 1
        print("No hay esa letra. Te quedan:", attempts)

    if "_" not in adivinalapalabra:
        print("¡Tú ganas! La palabra era:", palabra)
        break

if attempts == 0 and "_" in adivinalapalabra:
    print("Te has quedado sin intentos. La palabra era:", palabra)
