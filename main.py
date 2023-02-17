# Fernando José Pereira Salvador

import random

# Iniciamos las variables para contar las partidas jugadas, las ganadas y el maximo y minimo de intentos. Ademas de una
# variable booleana para saber si queremos seguir jugando
continuar = "si"
partidas_jugadas = 0
partidas_ganadas = 0
max_intentos = 0
min_intentos = 0
suma_intentos = 0

# Iniciamos las variables que usaremos para decir el rango
rango_alto = 100
rango_bajo = 1

# Mientras queramos seguir jugando ejecutamos el bucle
while continuar == "si" or continuar == "Si":

    # Creamos el número aleatorio y preguntamos el número de intentos y sumamos el contador de partidas jugadas.
    n_aleatorio = random.randint(1, 100)

    partidas_jugadas += 1

    n_intentos = int(input("Introduce el número de intentos: "))

    # Ahora preguntamos con el número de intentos solicitados anteriormente
    for i in range(1, n_intentos + 1):

        # Preguntamos el numero
        n = int(input(f"Introduce el número ({i} intento): "))

        # Si hemos acertado imprimimos el mensaje que hemos ganado y aumentamos en uno las partidas jugadas y
        # ganadas, ademas de calcular el max y minimo de intentos y sumar los intentos en una variable. Por ultimo
        # detenemos el bucle
        if n == n_aleatorio:
            print(f"Muy bien!!! Has acertado en {i} intentos")
            partidas_ganadas += 1
            suma_intentos += i

            # Calculamos el maximo y el mínimo de intentos
            if i > max_intentos:
                max_intentos = i

            if i < min_intentos or min_intentos == 0:
                min_intentos = i

            break
        # Si no, si n es mayor que el numero aleatorio calculamos el valor de rango_alto y decimos que era menor.
        elif n_aleatorio < n <= rango_alto:
            rango_alto = n - 1
            print("Es menor")

        # Si no, si n es menor que el numero aleatorio calculamos el valor del rango_bajo y decimos que era mayor.
        elif n_aleatorio > n >= rango_bajo:
            rango_bajo = n
            print("Es mayor")

        # Si ha introducido un numero fuera del rango imprimimos un mensaje diciendoselo y no calculamos nada
        else:
            print(f"No has introducido un numero dentro del rango")

        # Imprimimos el rango
        print(f"El rango es {rango_bajo} a {rango_alto}")


    # Si no superamos los intentos imprimimos el mensaje de que hemos fallado con el numero correcto y aumentamos
    # las partidas_jugadas en 1
    else:
        print(f"Has superado el número de intentos y no has acertado. El numero era: {n_aleatorio}")
        partidas_jugadas += 1

    # Preguntamos si queremos jugar otra partida
    continuar = input("¿Quiere jugar otra partida?: ")

# Imprimimos el numero de partidas que hemos jugado
print(f"Has jugado {partidas_jugadas} partidas")

# Si hemos ganado alguna partida mostramos PREMI por cada partida ganada, el max y minimo de intentos y la media
if partidas_ganadas != 0:

    print("Has ganado: ")
    for i in range(partidas_ganadas):
        print("PREMI")

    print(f"El minimo de intentos en el que se ha ganado una partida es: {min_intentos}")
    print(f"El maximo de intentos en el que se ha ganado una partida: {max_intentos}")
    print(f"Media de intentos es: {suma_intentos / partidas_ganadas}")
