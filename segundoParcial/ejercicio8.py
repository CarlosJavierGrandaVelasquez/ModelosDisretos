#funcion para ingresar la longitud del rectangulo
def ingresarLongitud():
    """
    Esta funcion nos ayuda a que el usuario ingrese la longitud del rectangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable longitud
    """
    #el usuario ingresa la longitud del rectangulo
    longitud = float(input("Ingrese la longitud del rectangulo: "))
    #la funcion retorna la variable longitud
    return longitud

#funcion para ingresar el ancho del rectangulo
def ingresarAncho():
    """
    Esta funcion nos ayuda a que el usuario ingrese el ancho del rectangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable ancho
    """
    #el usuario ingresa el ancho del rectangulo
    ancho = float(input("Ingrese el ancho del rectangulo: "))
    #la funcion retorna la variable ancho
    return ancho

#funcion para calcular el perimetro
def calcularPerimetro():
    """
    Esta funcion nos ayuda a que se calcule el perimetro del rectangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable perimetro
    """
    #a la variable perimetro se le asigna la formula para calcular el perimetro del rectangulo
    perimetro = (2 * longitudDelRectangulo) + (2 * anchoDelRectangulo)
    #la funcion retorna la variable perimetro
    return perimetro

#funcion principal
if __name__ == '__main__':
    #a la variable longitudDelRectangulo se le asigna lo que retorna la funcion ingresarLongitud()
    longitudDelRectangulo = ingresarLongitud()
    #a la variable anchoDelRectangulo se le asigna lo que retorna la funcion ingresarAncho()
    anchoDelRectangulo = ingresarAncho()
    #a la variable perimetroRectangulo se le asigna lo que retorna la funcion calcularPerimetro()
    perimetroRectangulo = calcularPerimetro()
    #se imprime los resutados
    print("La longitud del rectangulo es: ", longitudDelRectangulo)
    print("La ancho del rectangulo es: ", anchoDelRectangulo)
    print("El perimetro del rectangulo es: ",perimetroRectangulo)
