#funcion para ingresar la base del rectangulo
def ingresarBase():
    """
    Esta funcion nos ayuda a que el usuario ingrese la base del rectangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable base
    """
    #el usuario ingresa la base
    base = float(input("Ingrese la base del rectangulo: "))
    #la funcion retorna la variable base
    return base

#funcion para ingresar la altura del rectangulo
def ingresarAltura():
    """
    Esta funcion nos ayuda a que el usuario ingrese la altura del rectangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable altura
    """
    #el usuario ingresa la altura
    altura = float(input("Ingrese la altura del rectangulo: "))
    #la funcion retorna la variable altura
    return altura

#funcion para calcular el perimetro
def calcularPerimetro():
    """
    Esta funcion nos ayuda a que se calcule el Perimetro

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable perimetro
    """
    #a la variable perimetro se la asigna la formula del perimetro del rectangulo
    perimetro = (2 * baseDelRectangulo) + (2 * alturaDelRectangulo)
    #la funcion retorna la variable perimetro
    return perimetro

#funcion para calcular el area del rectangulo
def calcularArea():
    """
    Esta funcion nos ayuda a que se calcule el Area

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable area
    """
    #a la variable area se le asigna la formula para calcular el area del rectangulo
    area = baseDelRectangulo * alturaDelRectangulo
    #la funcion retorna la variable area
    return area

#funcion principal
if __name__ == '__main__':
    #a la variable baseDelRectangulo se le asigna lo que retorna la funcion ingresarBase()
    baseDelRectangulo = ingresarBase()
    #a la variable alturaDelRectangulo se le asigna lo que retorna la funcion ingresarAltura()
    alturaDelRectangulo = ingresarAltura()
    #a la variable perimetroRectangulo se le asigna lo que retorna la funcion calcularPerimetro()
    perimetroRectangulo = calcularPerimetro()
    #a la variable areaRectangulo se le asigna lo que retorna la funcion calcularArea()
    areaRectangulo = calcularArea()
    #se imprime los resultados
    print("La base del rectangulo es: ", baseDelRectangulo)
    print("La altura del rectangulo es: ", alturaDelRectangulo)
    print("El perimetro del rectangulo es: ",perimetroRectangulo)
    print("El area del rectangulo es: ", areaRectangulo)
