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
    print("Escoge cm para convertir De cm a m y km")
    print("Escoge m para convertir De m a cm y km")
    print("Escoge km para convertir De km a cm y m")
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

#funcion para convertir de cm a m y km
def conversionesDeCm():
    """
    Esta funcion nos ayuda a que calcule de centimetros a metros y kilometros

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna las variables metros y kilometros
    """
    #a la variable metros se le asigna la formula para convertir de centimetros a metros
    metros = cantidad / 100
    #a la variable metros se le asigna la formula para convertir de centimetros a kilometros
    kilometros = cantidad / 1000
    #a funcion retorna las variables metros y kilometros
    return metros, kilometros

#funcion para convertir de m a cm y km
def conversionesDeM():
    """
    Esta funcion nos ayuda a que calcule de metros a centimetros y kilometros

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna las variables centimetros y kilometros
    """
    #a la variable metros se le asigna la formula para convertir de metros a centimetros
    centimetros = cantidad * 100
    #a la variable metros se le asigna la formula para convertir de metros a kilometros
    kilometros = cantidad / 1000
    #a funcion retorna las variables centimetros y kilometros
    return centimetros, kilometros

#funcion para convertir de km a cm y m
def conversionesDeKm():
    """
    Esta funcion nos ayuda a que calcule de kilometros a metros y centimetros

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna las variables metros y centimetros
    """
    #a la variable metros se le asigna la formula para convertir de kilometros a centimetros
    centimetros = cantidad * 100000
    #a la variable metros se le asigna la formula para convertir de kilometros a metros
    metros = cantidad * 1000
    #a funcion retorna las variables centimetros y metros
    return centimetros, metros

#funcion principal
if __name__ == '__main__':
    #a la varibale opcion se le asigna lo que retorna la funcion escogerOpcion()
    opcion = escogerOpcion()
    #a la varibale opcion se le asigna lo que retorna la funcion valor()
    cantidad = valor()
    #a las varibales metros y kilometros se le asigna lo que retorna la funcion conversionesDeCm()
    metros, kilometros = conversionesDeCm()
    #a las varibales centimetro y kilometro se le asigna lo que retorna la funcion conversionesDeM()
    centimetro, kilometro = conversionesDeM()
    #a las varibales centimetros y metro se le asigna lo que retorna la funcion conversionesDeKm()
    centimetros, metro = conversionesDeKm()

    #condicional si la opcion es cm
    if opcion == "cm":
        #imprime los resultados
        print ("la conversion a cm es: ", metros, "m")
        print ("la conversion a cm es: ", kilometros, "km")

    #condicional si la opcion es m
    if opcion == "m":
        #imprime los resultados
        print ("La conversion a centimetros es: ", centimetro, "cm")
        print ("La conversion a kilometros es: ", kilometro, "km")

    #condicional si la opcion es km
    if opcion == "km":
        #imprime los resultados
        print ("la conversion a cm es: ", centimetro, "cm")
        print ("la conversion a cm es: ", metro, "m")
