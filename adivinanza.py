import random

def adivinanza():
    # Generamos un número aleatorio entre 1 y 100
    numero_aleatorio = random.randint(1, 100)
    
    print("¡Bienvenido al juego de Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("Intenta adivinar el número. Escribe 'salir' para rendirte.")
    
    intentos = 0
    
    while True:
        # Pedimos al jugador que ingrese un número
        entrada = input("¿Cuál es tu adivinanza? ")
        
        # Si el jugador quiere salir, terminamos el juego
        if entrada.lower() == 'salir':
            print(f"El número era {numero_aleatorio}. ¡Hasta la próxima!")
            break
        
        # Intentamos convertir la entrada en un número
        try:
            adivinanza = int(entrada)
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        intentos += 1
        
        # Comprobamos si la adivinanza es correcta
        if adivinanza < numero_aleatorio:
            print("¡Demasiado bajo! Intenta nuevamente.")
        elif adivinanza > numero_aleatorio:
            print("¡Demasiado alto! Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
            break

# Ejecutamos el juego
adivinanza()
