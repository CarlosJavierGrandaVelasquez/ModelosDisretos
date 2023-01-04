#funcion para ingresar el radio del circulo
def ingresarRadio():
    """
    Esta funcion nos ayuda a que el usuario ingrese el radio del circulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable radio
    """
    #el usuario ingresa el radio del circulo
    radio = float(input("Ingrese el radio del circulo: "))
    #la funcion retorna la variable radio
    return radio

#funcion para calcular el diametro de un circulo
def calcularDiametro():
    """
    Esta funcion nos ayuda a que se calcule el diametro

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable diametro
    """
    #se calcula el diametro del circulo con su formula
    diametro = 2 * radioCirculo
    #la funcion retorna la variable diametro
    return diametro

#funcion para calcular la circunferencia de un circulo
def calcularCircunferencia():
    """
    Esta funcion nos ayuda a que se calcule la circunferencia

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable circunferencia
    """
    #a la variable pi se le asigna el valor de 3.1416
    pi = 3.1416
    #a la variable circunferencia se le asigna la formula para calcular la circunferencia de un circulo
    circunferencia = pi * diametroCirculo
    #la funcion retorna la variable circunferencia
    return circunferencia

#funcion para calcular el area de un circulo
def calcularArea():
    """
    Esta funcion nos ayuda a que se calcule el area del circulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable area
    """
    #a la variable pi se le asigna el valor de 3.1416
    pi = 3.1416
    #a la variable area se le asigna la formula para calcular la area de un circulo
    area = pi * (radioCirculo * radioCirculo)
    #la funcion retorna la variable area
    return area

#funcion principal
if __name__ == '__main__':
    #a la variable radioCirculo se le asigna lo que retorna la funcion ingresarRadio()
    radioCirculo = ingresarRadio()
    #a la variable areaCirculo se le asigna lo que retorna la funcion calcularArea()
    areaCirculo = calcularArea()
    #a la variable diametroCirculo se le asigna lo que retorna la funcion calularDiametro()
    diametroCirculo = calcularDiametro()
    #a la variable circunferenciaCirculo se le asigna lo que retorna la funcion calcularCircunferencia()
    circunferenciaCirculo = calcularCircunferencia()
    #se imprime los resultados
    print("el radio del circulo es: ", radioCirculo)
    print("el area del circulo es: ", areaCirculo)
    print("El diametro del circulo es: ", diametroCirculo)
    print("La circunferencia del circulo es de: ", circunferenciaCirculo)