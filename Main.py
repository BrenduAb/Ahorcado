

import text
import Text_Manager
import Game
import Player_Manager


# En cada input se debe verificar que cada valor ingresado sea valido.
# No descomenten el main hasta que esten todas las funciones, sino va a tirar error.
# Si necesitan cambiar algo, haganlo y aclaren abajo o en el chat


listaDePalabrasSinProcesar = text.obtener_texto()
listaDePalabrasProcesadas = Text_Manager.procesarTexto(listaDePalabrasSinProcesar)
diccionarioDePalabras = Text_Manager.generarDiccionario(listaDePalabrasProcesadas)

# diccionarioDePalabras es el definitivo

datosGenerales = Player_Manager.asignarJugadores()


# Seguir jugando = True o false si quiere seguir jugando
seguirJugando = True
numerodePartida = 0

while (seguirJugando):
    numerodePartida+=1

    print ("Partida numero:", numerodePartida)

    listaPartida, datosGenerales = Game.iniciarPartida(datosGenerales, diccionarioDePalabras.keys())
    seguirJugando = Game.finalizarPartida(listaPartida, datosGenerales)
