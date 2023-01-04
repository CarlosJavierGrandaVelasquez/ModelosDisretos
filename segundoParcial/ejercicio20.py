#funcion para ingresar la base del paralelogramo
def ingresarBase():
    """
    Esta funcion nos ayuda a que el usuario ingrese la base del paralelogramo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable base
    """
    #el usuario ingresa la base del paralelogramo
    base = float(input("Ingrese la base que tiene el paralelogramo: "))
    #la funcion retorna la variable base
    return base

#funcion para ingresar la altura del paralelogramo
def ingresarAltura():
    """
    Esta funcion nos ayuda a que el usuario ingrese la altura del paralelogramo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable altura
    """
    #el usuario ingresa la altura del paralelogramo
    altura = float(input("Ingrese la altura que tiene el paralelogramo: "))
    #la funcion retorna la variable altura
    return altura

#funcion para calular el area del paralelogramo
def calcularArea():
    """
    Esta funcion nos ayuda a calcuar el area del paralelogramo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable areaParalelogramo
    """
    #a la variable areaParalelogramo se le asigna el valor de la formula baseParalelogramo * alturaParalelogramo
    areaParalelogramo = baseParalelogramo * alturaParalelogramo
    #la funcion retorna la variable areaParalelogramo
    return areaParalelogramo

#funcion principal
if __name__ == '__main__':
    #a la variable baseParalelogramo se le asigna lo que retorna la funcion ingresarBase()
    baseParalelogramo = ingresarBase()
    #a la variable alturaParalelogramo se le asigna lo que retorna la funcion ingresarAltura()
    alturaParalelogramo = ingresarAltura()
    #a la variable area se le asigna lo que retorna la funcion calcularArea()
    area = calcularArea()
    #se imprime el resultado
    print("El area total del Paralelogramo teniendo una base de", baseParalelogramo, "y una altura de", alturaParalelogramo, "es", area, "cm2")