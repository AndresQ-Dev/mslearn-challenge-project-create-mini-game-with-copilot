# hagamos un minijuego de Piedra papel o tijera
# ten en cuenta que roca rompe la tijera, tijera envuelve al papel y papel envuelve a la roca
# el jugador debe elegir una de las tres opciones y notificar si la opción escogida es inválida.
# cada rondo debe sumar puntaje para el jugador y la máquina dependiendo quien gane
# son 3 rodas por jugador, al final se debe mostrar el scrorer final
# la máquina debe escoger una opción aleatoria al elegir el jugador tambien
# al final de cada partida se debe ofrecer la opción de seguir jugando o salir. Y despues de tres rondas se debe mostrar el score final.
# debe verificarse que la opción ingresada por el jugador sea válida pasando todo a minusculas
# si el jugador decide salir se debe mostrar el score final y un mensaje de despedida
import random
import os
import time
def juego():
    print("Bienvenido a Piedra, Papel o Tijera")
    print("Selecciona una opción: Piedra, Papel o Tijera")
    jugador = input("Escribe tu opción: ")
    jugador = jugador.lower()
    opciones = ["piedra", "papel", "tijera"]
    maquina = random.choice(opciones)
    print("La máquina escogió: ", maquina)
    if jugador not in opciones:
        print("Opción inválida")
    elif jugador == maquina:
        print("Empate")
    elif jugador == "piedra" and maquina == "tijera":
        print("Ganaste")
    elif jugador == "tijera" and maquina == "papel":
        print("Ganaste")
    elif jugador == "papel" and maquina == "piedra":
        print("Ganaste")
    else:
        print("Perdiste")
    return jugador, maquina

def main():
    score_jugador = 0
    score_maquina = 0
    for i in range(3):
        jugador, maquina = juego()
        if jugador == maquina:
            pass
        elif jugador == "piedra" and maquina == "tijera":
            score_jugador += 1
        elif jugador == "tijera" and maquina == "papel":
            score_jugador += 1
        elif jugador == "papel" and maquina == "piedra":
            score_jugador += 1
        else:
            score_maquina += 1
    print("Score final: Jugador: ", score_jugador, "Máquina: ", score_maquina)
    seguir = input("Quieres seguir jugando? (s/n): ")
    if seguir == "s":
        main()
    else:
        print("Gracias por jugar")
        time.sleep(2)
        os.system("clear")
main()

