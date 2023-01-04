#funcion para ingresar un numero
def ingresarNumero():
    """
    Esta funcion nos ayuda a que el usuario ingrese un numero para calcular su raiz

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable num
    """
    #el usuario ingresa un numero para sacar su raiz
    num = float(input("Ingrese el numero a calcular su raiz: "))
    #la funcion retorna la variable num
    return num

#funcion para ingresar el valor de la raiz
def ingresarRaiz():
    """
    Esta funcion nos ayuda a que el usuario ingrese un numero a la raiz

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable raiz
    """
    #el usuario ingresa un numero para que sea la raiz
    raiz = int(input("Ingrese la raiz a calcular: "))
    #la funcion retorna la variable raiz
    return raiz

#funcion para calcular la raiz
def calcularRaiz():
    #la variable raizIngresada se le asigna el valor de 1 / numRaiz
    raizIngresada = 1 / numRaiz
    #la variable raizCalculada se le asigna el valor de numero**(raizIngresada)
    raizCalculada = numero**(raizIngresada)
    #la funcion retorna la variable raizCalculada
    return raizCalculada

#funcion principal
if __name__ == '__main__':
    #a la variable numero se le asigna lo que retorna la funcion ingresarNumero()
    numero = ingresarNumero()
    #a la variable numRaiz se le asigna lo que retorna la funcion ingresarRaiz()
    numRaiz = ingresarRaiz()
    #a la variable raizTotal se le asigna lo que retorna la funcion calcularRaiz()
    raizTotal = calcularRaiz()
    #se imprime el resultado
    print("La raiz a la", numRaiz, "de ",numero ,"es:", raizTotal)