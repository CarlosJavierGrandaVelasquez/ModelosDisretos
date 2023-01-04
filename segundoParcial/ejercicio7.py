#funcion para la cantidad de numeros a sumar
def cantNum():
    """
    La funcion nos ayuda a que el usuario ingrese la cantidad total de numeros 
    que desea sumar

    Parametros:
    -----------------
        cantidad de numeros a sumar

    Retorna:
    -----------------
        Retorna la cantidad de numeros a sumar
    """
    #se inicializa la variable cantidadNum para que el usuario eliga la cantidad de numeros a sumar
    cantidadNum = int(input("ingrese la cantidad de numeros que quiere resolver con las operaciones aritmeticas: "))
    #imprime la cantidad de numeros que quiere sumar el usuario
    print ("la cantidad de numeros a sumar es: ", {cantidadNum}) 
    #retorna la cantidad de numeros que quiere sumar el usuario
    return cantidadNum

#funcion para sumar los numeros
def operaciones():
    """
    Esta funcion nos ayuda a sumar, restar, multiplicar, dividir numeros que ingreso el usuario
    teniendo en cuenta que el usuario ingreso una cantidad de numeros a sumar, restar, multiplicar, dividir

    Parametros:
    -----------------
        numeros a sumar, restar, multiplicar, dividir
        suma, resta, multiplicacion, division total de los numeros

    Retorna:
    -----------------
        retorna la suma, resta, multiplicacion, division total de los numeros 
    """
    #se inicializa con 0 a la sumaTotal
    sumaTotal = 0
    restaTotal = 0
    multiplicacionTotal = 1
    divisionTotal = 1
    #se inicializa con el valor de 0 el iterador
    x = 1
    #se realiza un ciclo while hasta que el iterador llegue a la cantidad de numeros a sumar, restar, multiplicar, dividir y se repita el mensaje
    while x <= cantidadNumeros:
        #el usuario ingresa el valor de los numeros
        num = int(input("ingrese un numero: "))
        #se va realizando la suma, resta, multiplicacion, division total con el ultimo numero ingresado
        sumaTotal = sumaTotal + num
        restaTotal = restaTotal - num
        multiplicacionTotal = multiplicacionTotal * num
        divisionTotal =  num / divisionTotal 

        #se le aniade un valor mas por cada repeticion al iterador
        x = x+1
    
    #se retorna el valor de la suma, resta, multiplicacion, division total
    return (sumaTotal, restaTotal, multiplicacionTotal, divisionTotal)

#funcion principal o main
if __name__ == '__main__':
    """
    Es la funcion principal que nos ayuda a imprimir los datos de la suma total
    Parametros:
    ----------------
        No tiene parametros
    
    Retorna:
    ----------------
        No retorna nada
    """
    cantidadNumeros = cantNum()
    sumaTotal, restaTotal, multiplicacionTotal, divisionTotal = operaciones()
    #se imprime los resultados
    print("la suma total de los numeros es: ", sumaTotal)
    print("la resta total de los numeros es: ", restaTotal)
    print("la multiplicacion total de los numeros es: ", multiplicacionTotal)
    print(f"la division total de los numeros es: ", divisionTotal)
    