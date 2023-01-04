#funcion para ingresar el primer y segundo angulo
def ingresarAngulos():
    """
    Esta funcion nos ayuda a que el usuario ingrese el primer y segundo angulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna las variables angulo1 y angulo2
    """
    #el usuario ingresa el valor del primer angulo
    angulo1 = float(input("Ingrese el angulo 1: "))
    #el usuario ingresa el valor del segundo angulo
    angulo2 = float(input("Ingrese el angulo 2: "))
    #la funcion retorna la variable angulo1 y angulo2
    return angulo1, angulo2

#funcion para calcular el tercer angulo
def calcularTercerAngulo(): 
    """
    Esta funcion nos ayuda a calcular el tercer angulo

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable angulo3
    """
    #a la variable angulo3 se le asigna el valor de 180 - (primerAngulo + segundoAngulo)
    angulo3 = 180 - (primerAngulo + segundoAngulo)
    #la funcion retorna la variable angulo3
    return angulo3

#funcion principal
if __name__ == '__main__':
    #a las variables primerAngulo y segundoAngulo se les asigna lo que retorna la funcion ingresarAngulos()
    primerAngulo, segundoAngulo = ingresarAngulos()
    #a la variable tercerAngulo se le asigna lo que retorna la funcion calcularTercerAngulo()
    tercerAngulo = calcularTercerAngulo()
    #imprime los resultados
    print("Ingrese los angulos: ")
    print("El primer angulo es: ",primerAngulo, "grados")
    print("El segundo angulo es: ",segundoAngulo, "grados")
    print("El tercer angulo tiene el valor de: ",tercerAngulo, "grados")
