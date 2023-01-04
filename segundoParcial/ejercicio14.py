#funcion para ingresar el numero de dias
def ingresarDias():
    """
    Esta funcion nos ayuda a que el usuario ingrese el numero de dias

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable dias
    """
    #el usuario ingresa el numero de dias
    dias = int(input("Ingrese el numero de dias: "))
    #la funcion retorna la variable dias
    return dias

#funcion para convertir los dias a anios
def convertirAnios():
    """
    Esta funcion nos ayuda a calcular los anios

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable anios
    """
    #a la varibale anios se le asigna la formula de numeros de dias ingresados dividido por 365
    anios = numDias / 365
    #la funcion retorna la variable anios
    return anios

#funcion para convertir los dias a semanas
def convertirSemanas():
    """
    Esta funcion nos ayuda a calcular las semanas

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable semanas
    """
    #a la varibale anios se le asigna la formula de numeros de dias ingresados dividido por 7
    semanas = numDias / 7
    #la funcion retorna la variable semanas
    return semanas

#funcion para calcular los dias
def convertirDias():
    """
    Esta funcion nos ayuda a calcular los dias

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable dia
    """
    #a la varibale anios se le asigna la formula de numeros de dias ingresados menos el numero de semanas por 7
    dia = numDias-(semana * 7)
    #la funcion retorna la variable dia
    return dia

#funcion principal
if __name__ == '__main__':
    #a la variable numDias se le asigna lo que retorna la funcion ingresarDias()
    numDias = ingresarDias()
    #a la variable anio se le asigna lo que retorna la funcion convertirAnios()
    anio = int(convertirAnios())
    #a la variable semana se le asigna lo que retorna la funcion convertirSemanas()
    semana = int(convertirSemanas())
    #a la variable dia se le asigna lo que retorna la funcion convertirDias()
    dia = int(convertirDias())
    #imprime los resultados
    print("Para ",numDias, "dias Son:", anio, "anios", semana, "semanas y", dia ,"dias")