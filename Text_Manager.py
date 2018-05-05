

def procesarTexto(list):
    """
    Autor = Santiago
    Esta funcion recibe la lista de la funcion provista obtener_texto, y devuelve otra con las palabras validas.
    Que tengan mas de 5 caracteres, quitando los simbolos, y numeros, las enies, los tildes, pasando a mayuscula \
    y ordenado alfabeticamente. y la devuelve """
    # PRE: Recibe una lista de frases
    # POST: Devuelve cada una de las palabras en las frases sin repeteir ordenadas alfabeticamente en una lista


    final_list=[]
    signosARemplazar = [["\"", ""], ["(", ""], [")", ""], [",", ""], [".", ""], [":", ""], [";", ""], ["-", ""] \
        ,["Ñ", "N"], ["Á", "A"], ["É", "E"], ["Í", "I"], ["Ó", "O"], ["Ú", "U"]]
    for frase in list:
        palabras = frase.split(" ")
        cantidadDeCaracteres=len(palabras)

        for i in range(0,cantidadDeCaracteres -1):
            palabra = palabras[i].upper()
            if verificarPalabra(palabra):
                for remplazado, remplazo in signosARemplazar:
                    palabra= palabra.replace(remplazado,remplazo)
                if len(palabra) > 5:
                    final_list.append(palabra)

    ordered_list = sorted(final_list)
    return ordered_list

def verificarPalabra(palabra):
    # PRE: Recibe una palabra
    # POST: Devuelve True si no tiene numeros, False si tiene
    for i in range (0,10):
        if str(i) in palabra:
            return False
    return True


def generarDiccionario(list):
    """
    Autor = Santiago
    Crea un diccionario con las palabras de la lista, quitando las repetidas, y asignando la cantidad de veces que \
    aparece esa palabra en el valor"""
    # PRE: Recibe una lista de palabras
    # POST: Devuelve un diccionario con la palabra, cuantas veces aparece y llama a la funcion ImprimirDiccionario
    diccionarioDePalabras={}
    for i in list:
        if not i in diccionarioDePalabras:
            cantidadDeRepeticiones = list.count(i)
            diccionarioDePalabras[i]=(cantidadDeRepeticiones)

    imprimirDiccionario(diccionarioDePalabras)
    
    return diccionarioDePalabras


def imprimirDiccionario(dic):
    """
    Autor = Santiago
    Imprime una lista con las claves del diccionario sin palabras repetidas, informando tambien cuantas palabras \
    hay en total. """
    # PRE: Recibe una lista de palabras
    # POST: Imprime la lista y el total de palabras en ella
    for palabra in dic:
        print("la palabra ", palabra, " esta repetida ", dic[palabra], " veces")
    totalDePalabras= len(dic)
    print("el total de palabras es: ", totalDePalabras)


def buscarPalabras(longitud, cantidad, listaDePalabras):
    """
    Autor = Mauro
    Busca palabras de una longitud particular y las devuelve en una lista"""

    listaPalabrasLongitudDeterminada = []
    buscarPalabras = True
    while buscarPalabras:
        listaPalabrasLongitudDeterminada.clear()
        for palabra in listaDePalabras:
            if len(palabra) == (longitud):
                listaPalabrasLongitudDeterminada.append(palabra)
                if len(listaPalabrasLongitudDeterminada) == (cantidad):
                    return listaPalabrasLongitudDeterminada
        longitud = input("Insuficientes palabras de la longitud pedida. Ingresar una nueva longitud de palabras: ")

