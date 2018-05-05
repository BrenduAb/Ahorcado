def asignarJugadores():
    """
    Autor = Chiara
    Le pide al usuario que ingrese la cantidad de jugadores para el juego. A continuacion le pide los nombres y los \
    almacena en un diccionario, asignando 0 puntos, 0 aciertos y 0 desaciertos en un principio
    [ "Nombre del jugador"  --- [Puntaje, Aciertos, Desaciertos] ]

    """
    cantidadJugadores = int(input('Ingresar la cantidad de jugadores que van a jugar: '))
    dic = {}
    for i in range(0, cantidadJugadores):
        jugador = input('Ingrese el nombre del jugador: ')
        dic[jugador] = [0, 0, 0]
    return dic


def organizarJugadores(dic):
    """
    Autor = Chiara
    Ordena los jugadores por puntaje, y devuelve una lista con una lista que tiene el nombre y el puntaje

    """
    ordenarDic = sorted(dic.items(), key = lambda x:x[1][2], reverse = True)
    listaJuagadorPuntaje = []
    for tupla in ordenarDic:
        jugador = tupla[0]
        puntaje = tupla[1][2]
        listaIndividual = [jugador,puntaje]
        listaJuagadorPuntaje.append(listaIndividual)
    return listaJuagadorPuntaje

def actualizarDatos(dic,lista):
    """
    Autor = Chiara
    Actualiza los datos del diccionario con la lista ingresada

    """
    listaJugadores = []
    clavesValores = dic.items()
    for tupla in clavesValores:
        listaJugadores.append(tupla[0])
    listaValoresFinal = []
    for jugador in listaJugadores:
        listaResultadosParciales = dic[jugador]
        for i in lista:
            participantePartida = i[0]
            if participantePartida == jugador:
                puntajeParcial = listaResultadosParciales[0]
                aciertosParciales = listaResultadosParciales[1]
                desaciertosParciales = listaResultadosParciales[2]
                puntajePartida = i[5]
                aciertosPartida = i[4]
                desaciertosRestantesPartida = i[3]
                desaciertosPartida = (7 - desaciertosRestantesPartida)
                puntajeTotal = puntajeParcial + puntajePartida
                aciertosTotales = aciertosParciales + aciertosPartida
                desaciertosTotales = desaciertosParciales + desaciertosPartida
                listaValoresFinal = [puntajeTotal, aciertosTotales, desaciertosTotales]
        dic[jugador] = listaValoresFinal
    return dic



def imprimirDatosGenerales(dicDatosGenerales):
    """
    Autor = Ezequiel
    Imprime los datos del diccionario

    [ "Nombre del jugador"  --- [Puntaje, Aciertos, Desaciertos] ]
    """

    for jugador in dicDatosGenerales:
        print("Jugador: ", jugador, "\nPuntaje: ", dicDatosGenerales[jugador][0])
        print("Aciertos: ", dicDatosGenerales[jugador][1], "\nDesaciertos: ", dicDatosGenerales[jugador][2])