#funcion para ingresar la distancia
def ingresarDistancia():
    """
    Esta funcion nos ayuda a que el usuario ingrese la distancia

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable distancia
    """
    #el usuario ingresa la distancia
    distancia = float(input("Ingrese el valor de la distancia en metros: "))
    #la funcion retorna la variable distancia
    return distancia

#funcion para ingresar el tiempo
def ingresarTiempo():
    """
    Esta funcion nos ayuda a que el usuario ingrese el tiempo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable tiempo
    """
    #el usuario ingresa el tiempo
    tiempo = float(input("Ingrese el valor de el tiempo en segundos: "))
    #la funcion retorna la variable tiempo
    return tiempo

#funcion para calcular la velocidad
def calcularVelocidad():
    """
    Esta funcion nos ayuda a que se calcule la velocidad

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable velocidad
    """
    # a la variable velocidad se le asigna la formula para calcular la velocidad
    velocidad = distanciaRecorrida / tiempoRecorrido
    #la funcion retorna la variable velocidad
    return velocidad

#funcion principal
if __name__ == '__main__':
    #a la variable distanciaRecorrida se le asigna lo que retorna la funcion ingresarDistancia()
    distanciaRecorrida = ingresarDistancia()
    #a la variable tiempoRecorrido se le asigna lo que retorna la funcion ingresarTiempo()
    tiempoRecorrido = ingresarTiempo()
    #a la variable velocidadFinal se le asigna lo que retorna la funcion calcularVelocidad()
    velocidadFinal = calcularVelocidad()
    #se imprime los resultados
    print("Su distancia es: ", distanciaRecorrida, "m")
    print("Su tiempo recrrido es: ", tiempoRecorrido, "s")
    print("La velocidad suya es de: ", velocidadFinal, "m/s")
