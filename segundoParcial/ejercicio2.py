#funcion para ingresar el dinero invertido
def dineroInvertido():
    """
    Esta funcion nos ayuda a que el usuario ingrese el dinero invertido

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable cantidadInvertida
    """
    #e usuario ingresa la cantidad de dinero invertido
    cantidadInvertida = float(input("ingrese la cantidad invertida: "))
    #la funcion retorna la variable cantidadInvertida
    return cantidadInvertida

#funcion para ingresar el interes anual
def interes():
    """
    Esta funcion nos ayuda a que el usuario ingrese el valor del interes anual
    y lo divida para 100

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable interesAnual
    """
    #el usuario ingresa el interes anual
    valorInteres = int(input("Ingrese el valor del interes anual "))
    #a la variable interesAnual se le asigna valorInteres y se lo divide para 100
    interesAnual = valorInteres / 100
    #la funcion retorna la variable
    return interesAnual

#funcion para ingresar el tiempo de inversion
def tiempo():
    """
    Esta funcion nos ayuda a que el usuario ingrese el tiempo de anios de la inversion

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable aniosInteres
    """
    #el usuario ingresa el numero de anios de la inversion
    aniosInteres = int(input("ingrese el numero de anios de la inversion "))
    #la funcion retorna la variable
    return aniosInteres

#funcion para calcular el capital total de la inversion
def capital():
    """
    Esta funcion nos ayuda a que se calcule el capital total

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable capitalTotal
    """
    #a la variable capitalTotal se le asigna la formula para sacar el capital de una inversion
    capitalTotal = dineroinversion / 1 + (valorInteresAnual * tiempoAnual)
    #la funcion retorna la variable capitalTotal
    return capitalTotal

#funcion principal
if __name__ == '__main__':
    #a la variable dineroinversion se le asigna lo que retorna la funcion dineroInvertido()
    dineroinversion = dineroInvertido()
    #a la variable valorInteresAnual se le asigna lo que retorna la funcion interes()
    valorInteresAnual = interes()
    #a la variable tiempoAnual se le asigna lo que retorna la funcion tiempo()
    tiempoAnual = tiempo()
    #a la variable capTotal se le asigna lo que retorna la funcion capital()
    capTotal = capital()
    #se imprime los resultados
    print("el dinero invertido es: ", dineroinversion)
    print("el valor de interes anual es: ", valorInteresAnual)
    print("Los anios de la inversion son: ", tiempoAnual)
    print("El capital total de la inversion es: ", capTotal)
