import Text_Manager
import Player_Manager

def iniciarPartida(dic, listadepalabras):
    """
    Autor = Mauro
    Inicia la partida, da la bienvenida e imprime instrucciones \
    Organiza los jugadores y llama a pedido de longitud y dar turno.

    return lista, diccionario
    """
    input("Bienvenidos a esta nueva partida. Para comenzar, presione enter.")
    listaJugadores = Player_Manager.organizarJugadores(dic)
    listaGame = solicitarLongitudDePalabra(listaJugadores, listadepalabras)
    listaFinal = darTurno(listaGame)
    datosGenerales = Player_Manager.actualizarDatos(dic, listaFinal)
    return listaFinal, datosGenerales

def solicitarLongitudDePalabra(listaJugadores, listaPalabrasGenerales):
    """
    Autor = Ezequiel
    Pide la longitud de la palabra. Luego pide las palabras al texto y se las asigna a cada jugador en la lista de listas
    Creando una nueva lista de listas, que contenga para cada jugador:

    [ Nombre del jugador,  Palabra a Adivinar,  Progreso de Palabra,  Desaciertos restantes,  Aciertos,  Puntaje, Letras Ingresadas]

    DesaciertosRestantes inicia en 7
    Aciertos en 0
    El puntaje estará en la lista, igual que el nombre

    Formato de progreso de palabra:
    Ej: PERRO
    Formato: -----
    con letras: -E--O

    Devuelve lista
    """

    valido = False
    cantidadJugadores = len(listaJugadores)
    while not valido:
        longitud = input ("Ingrese longitud de palabra: ")
        if longitud.isdigit() and int(longitud) > 5:
            valido = True
            listaPalabrasJuego = Text_Manager.buscarPalabras(int(longitud), cantidadJugadores, listaPalabrasGenerales)

            palabraProceso = ""
            for i in range(int(longitud)):
                palabraProceso += "-"

            listaDeJugadoresCompleta = []

            for i in range(cantidadJugadores):
                auxList = [listaJugadores[i][0], listaPalabrasJuego[i], palabraProceso, 7, 0, listaJugadores[i][1], ""]
                listaDeJugadoresCompleta.append(auxList)

            return listaDeJugadoresCompleta

        else:
            print("Valor ingresado no valido.")


def darTurno(lista):
    """
    Autor = Brenda
    Verifica el jugador que le toca intentar acertar. En cuanto hay un ganador, devuelve la lista
    """

    contador = 0
    cantidadJugadores = len(lista)
    while not verificarGanador(lista):
        if lista[contador][3] > 0:
            lista = turno(lista, contador)
        else:
            print ("Jugador: ", lista[contador][0], "No quedan mas desaciertos restantes")
        contador += 1

        if contador == cantidadJugadores:
            contador = 0

    return lista


def turno(lista, contador):
    """
    Autor = Brenda
    Pide el ingreso de un caracter, verifica si esta en la palabra. Imprime el turno. \
    Si esta, cambia el progreso de la palabra, \
    te permite ingresar un nuevo caracter, disminuye el numero de desaciertos restante, asigna el puntaje y \
    devuelve la lista cambiada """

    print ("Ahora es el turno de: ", lista[contador][0])
    print ("Palabra:     ", lista[contador][2])
    print ("Letras ingresadas: ", lista[contador][6])

    termino = False
    valido = False
    while not termino:
        while not valido:
            # C = Caracter ingresado
            c = input("Ingrese un caracter: ")
            if (len(c) > 1) and not c.isalpha():
                print("Por favor ingrese un caracter valido")
            else:
                valido = True
                c = c.upper()

        if c in lista[contador][6]:
            print ("Este caracter ya fue ingresado. Reintente.")
        else:

            if c in lista[contador][1]:
                aux = cambiarCaracter(c, lista[contador][1], lista[contador][2])
                lista[contador][2] = aux

                print("Palabra: ", aux)
                # Puntaje
                lista[contador][5] += 1
                # Aciertos
                lista[contador][4] += 1
                print("Muy bien! ")
				print ("Palabra:     ", lista[contador][2])
    			print ("Letras ingresadas: ", lista[contador][6])
                
				valido = False

            else:
                print("Esa letra no se encuentra")
                lista[contador][6] += c + " "

                # Desaciertos restantes
                lista[contador][3] -= 1
                # Puntaje
                lista[contador][5] -= 2
                termino = True

        if lista[contador][2] == lista[contador][1]:
            termino = True

		if not termino:
			print("Tienes otra posibilidad")
    return lista


def cambiarCaracter(c, palabra, progreso):
    """Autor = Brenda.
        Verifica si se encuentra el caracter en la palabra, si es asi lo reemplaza.
    """
    cantidad = len(palabra)
    aux = ""

    for i in range(cantidad):
        if palabra[i] == c:
            aux += palabra[i]
        else:
            aux += progreso[i]

    return aux


def verificarGanador(lista):
    """
    Autor = Brenda
    Verifica si algun jugador ya completo la palabra. Si no es asi, verifica si ya todos los jugadores se quedaron \
    sin desaciertos. En ese caso, gana el programa. Suma puntos en caso de que haya ganador"""

    ganador = False
    cantDesaciertosCompletos = 0
    cantidadJugadores = len(lista)
    contador = 0


    while not ganador and contador < cantidadJugadores:
        if lista[contador][1] == lista[contador][2]:
            print("GANADOR: ", lista[contador][0])
            ganador = True
            lista[contador][5] += 30
        else:
            if (lista[contador][3] == 0):
                cantDesaciertosCompletos +=1

        contador +=1

    if cantDesaciertosCompletos == cantidadJugadores:
        print ("GANO EL PROGRAMA!")
        ganador = True

    return ganador


def finalizarPartida(listaPartida, datosGenerales):
    """
    Autor = Mauro
    Llama a funcion que imprime los datos de la partida (hay que hacerla). \
    Pregunta si quieren seguir jugando. Return True o False """
    Player_Manager.imprimirDatosGenerales(datosGenerales)
    seguir = input("Si se desea iniciar una nueva partida, ingrese 1. Sino, presione enter para terminar.")
    if seguir == "1":
        return True
    else:
        return False
