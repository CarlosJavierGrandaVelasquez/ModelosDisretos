#funcion para ingresar la base del triangulo
def ingresarBase():
    """
    Esta funcion nos ayuda a que el usuario ingrese la base del triangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable base
    """
    #el usuario ingresa la base del triangulo
    base = float(input("Ingrese la base que tiene el triangulo: "))
    #la funcion retorna la variable base
    return base

#funcion para ingresar la altura del triangulo
def ingresarAltura():
    """
    Esta funcion nos ayuda a que el usuario ingrese la altura del triangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable altura
    """
    #el usuario ingresa la altura del triangulo
    altura = float(input("Ingrese la altura que tiene el triangulo: "))
    #la funcion retorna la variable altura
    return altura

#funcion para calcular el area del triangulo
def calcularArea():
    """
    Esta funcion nos ayuda a calcular el area del triangulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable areaTriangulo
    """
    #a la variable areaTriangulo se le asigna el valor de la formula (baseTriangulo * alturaTriangulo)/ 2
    areaTriangulo = (baseTriangulo * alturaTriangulo)/ 2
    #la funcion retorna la variable areaTriangulo
    return areaTriangulo

#funcion principal
if __name__ == '__main__':
    #a la variable baseTriangulo se le asigna lo que retorna la funcion ingresarBase()
    baseTriangulo = ingresarBase()
    #a la variable alturaTriangulo se le asigna lo que retorna la funcion ingresarAltura()
    alturaTriangulo = ingresarAltura()
    #a la variable area se le asigna lo que retorna la funcion calcularArea()
    area = calcularArea()
    #imprime el resultado
    print("El area total del triangulo teniendo una base de", baseTriangulo, "y una altura de", alturaTriangulo, "es", area)