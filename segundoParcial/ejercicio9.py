#funcion para ingresar el radio del cilindro
def ingresarRadio():
    """
    Esta funcion nos ayuda a que el usuario ingrese el radio del cilindro

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable radio
    """
    #el usuario ingresa el valor del radio
    radio = float(input("Ingrese el radio del cilindro: "))
    #la funcion retorna la variable radio
    return radio

#funcion para ingresar la altura del cilindro
def ingresarAltura():
    """
    Esta funcion nos ayuda a que el usuario ingrese la altura del cilindro

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable altura
    """
    #el usuario ingresa el valor de la altura
    altura = float(input("Ingrese la altura que tiene el cilindro: "))
    #la funcion retorna la variable altura
    return altura

#funcion para calcular el area del cilindro
def calcularArea():
    """
    Esta funcion nos ayuda a que se calcule el area del cilindro

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable area
    """
    #a la variable pi se le asigna el valor de 3.1416
    pi = 3.1416
    #a la variable area se le asigna la formula para calcular el area del cilindro
    area = 2 * pi * radioCilindro * (radioCilindro + alturaCilindro)
    #la funcion retorna la variable area
    return area

#funcion principal
if __name__ == '__main__':

    #a la variable radioCilindro se le asigna lo que retorna la funcion ingresarRadio()
    radioCilindro = ingresarRadio()
    #a la variable alturaCilindro se le asigna lo que retorna la funcion ingresarAltura)
    alturaCilindro = ingresarAltura()
    #a la variable areaCilindro se le asigna lo que retorna la funcion calcularArea()
    areaCilindro = calcularArea()
    #se imprime los resultados
    print("el radio del Cilindro es: ", radioCilindro)
    print("La altura del cilindro es: ", alturaCilindro)
    print("el area del Cilindro es: ", areaCilindro)