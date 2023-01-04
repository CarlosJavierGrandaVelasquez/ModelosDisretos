#funcion para escoger una opcion
def escogerOpcion():
    """
    Esta funcion nos ayuda a que el usuario ingrese una opcion

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable opciones
    """
    #imprime las opciones a escoger
    print("------------CONVERTIDOR-----------")
    print("Escoge c para convertir De celcius a fahrenheint")
    print("Escoge f para convertir De fahrenheint a celcius")
    #el usuario ingresa una opcion y se le asigna a la varibale opciones
    opciones = input("Escoge la opcion ")
    #la funcion retorna la variable opciones
    return opciones

#funcion para ingresar una cantidad a convertir
def valor():
    """
    Esta funcion nos ayuda a que el usuario ingrese una cantidad

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable cantidad
    """
    #el usuario ingresa una cantidad que quiere convertir
    cantidad = float(input("Indica la cantidad a convertir: "))
    #la funcion retorna la variable cantidad
    return cantidad

#funcion para convertir de celcius a fahrenheint
def conversionesDeCelsius():
    """
    Esta funcion nos ayuda a que calcule de celsius a fahrenheint

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable fahrenheint
    """
    #a la variable metros se le asigna la formula para convertir de celsius a fahrenheint
    fahrenheint = (cantidad * 9 / 5 ) + 32
    #la funcion retorna la variable fahrenheint
    return fahrenheint

#funcion para convertir de fahrenheint a celcius
def conversionesDefahrenheint():
    """
    Esta funcion nos ayuda a que calcule de fahrenheint a celsius

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable celsius
    """
    #a la variable metros se le asigna la formula para convertir de fahrenheint a celsius
    celsius = (cantidad - 32 ) / 1,8
    #la funcion retorna la variable celsius
    return celsius

#funcion principal
if __name__ == '__main__':
    #a la varibale opcion se le asigna lo que retorna la funcion escogerOpcion()
    opcion = escogerOpcion()
    #a la varibale cantidad se le asigna lo que retorna la funcion valor()
    cantidad = valor()
    #a la varibale fahrenheint se le asigna lo que retorna la funcion conversionesDeCelsius()
    fahrenheint = conversionesDeCelsius()
    #a la varibale celsius se le asigna lo que retorna la funcion conversionesDefahrenheint()
    celsius = conversionesDefahrenheint()

    #condicional de si es c
    if opcion == "c":
        #imprime el resultado 
        print ("la conversion de celcius a fahrenheint es: ",  fahrenheint , "grados")

    #condicional de si es f
    if opcion == "f":
        #imprime el resultado
        print ("la conversion de celcius a fahrenheint es: ",  celsius , "grados")
