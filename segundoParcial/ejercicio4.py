#uncion para ingresar el radio
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

#funcion para calcular el area
def calcularArea():
    """
    Esta funcion nos ayuda a que se calcule el Area del circulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable area
    """
    #la variable pi vale 3.1416
    pi = 3.1416
    #a la variable area se le asigna la formula para calcular el area de un circulo
    area = pi * (radioCirculo * radioCirculo)
    #la funcion retorna la variable area
    return area

#funcion principal
if __name__ == '__main__':
    #a la variable radioCirculo se le asinga lo que retorna la funcion ingresarRadio()
    radioCirculo = ingresarRadio()
    #a a=la variable areaCirculo se le asigna lo que retorna la funcion calcularArea()
    areaCirculo = calcularArea()
    #se imprime los resultados
    print("el radio del circulo es: ", radioCirculo)
    print("el area del circulo es: ", areaCirculo)
