#importamos la libreria math
import math

#funcion para ingresar un numero
def ingresarNumero():
    """
    Esta funcion nos ayuda a que el usuario ingrese un numero

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable numero
    """
    #el usuario ingresa un numero para sacar su potencia
    numero = float(input("Ingrese un numero para sacar su potencia: "))
    #la funcion retorna la variable numero
    return numero

#funcion para ingresar la potencia
def ingresarPotencia():
    """
    Esta funcion nos ayuda a que el usuario ingrese el exponente

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable exponente
    """
    #el usuario ingresa el exponente
    exponente = int(input("Ingrese el exponete de la potencia:"))
    #la funcion retorna la variable exponente
    return exponente

#funcion para calcular la potencia
def calcularPotencia():
    """
    Esta funcion nos ayuda a que se calcule la potencia del numero

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable potencia
    """
    #a la variable potencia se le calcula la pontencia de dicho numero
    potencia = pow(numeroElevar, numeroExponente)
    #la funcion retorna la variable potencia
    return potencia

#funcion principal
if __name__ == '__main__':
    #a la variable numeroElevar se le asigna lo que retorna la funcion ingresarNumero()
    numeroElevar = ingresarNumero()
    #a la variable numeroExponente se le asigna lo que retorna la funcion ingresarExponente()
    numeroExponente = ingresarPotencia()
    #a la variable potenciaCalculada se le asigna lo que retorna la funcion calcularPotencia()
    potenciaCalculada = calcularPotencia()
    #imprime los resultados
    print("La potencia del numero ",numeroElevar , "con exponente ",numeroExponente , "es ",potenciaCalculada)
