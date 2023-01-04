#funcion para ingresar el numero de materias
def ingresarNumMaterias():
    """
    Esta funcion nos ayuda a que el usuario ingrese el numero de materias

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable materias
    """
    #el usuario ingresa el numero de materias
    materias = int(input("Ingrese el numero de materias a calcular: "))
    #la funcion retorna la varible materias
    return materias

#funcion para calcular la suma, el promedio y el porcentaje de las materias
def calcularNotas():
    """
    Esta funcion nos ayuda a calcular la suma, el promedio y el porcentaje de las materias

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna las variables notas, sumaNotas, promedioNotas y porcentajeNotas
    """
    #inicializo a x con el valor de 1
    x = 1
    #inicializo a sumaNotas con el valor de 0
    sumaNotas = 0
    #ciclo while si x <= numMaterias
    while x <= numMaterias:
        #el usuario ingresa las notas dependiendo las materias
        notas = float(input("Ingrese la nota (del 0 al 10): "))
        #a la variable sumaNotas asigno el valor de sumaNotas + notas
        sumaNotas = sumaNotas + notas
        #a la varibale promedioNotas asigno el valor de sumaNotas / numMaterias
        promedioNotas = sumaNotas / numMaterias
        #a la variable porcentajeNotas asigno el valor de (sumaNotas / (numMaterias * 0.1))
        porcentajeNotas = (sumaNotas / (numMaterias * 0.1))
        #al iterador x le asigno el valor siguiente
        x = x+1
    #la funcion retorna las variables notas, sumaNotas, promedioNotas y porcentajeNotas
    return notas, sumaNotas, promedioNotas, porcentajeNotas

#funcion principal
if __name__ == '__main__':
    #a la variable numMaterias se le asigna lo que retorna la funcion ingresarNumMaterias()
    numMaterias = ingresarNumMaterias()
    #a las variables notasTotal, sumatoria, promedio y porcentaje se le asignan lo que retorna la funcion calcularNotas()
    notasTotal, sumatoria, promedio, porcentaje= calcularNotas()
    #imprime los resultados
    print("El numero de materias es: ", numMaterias)
    print("La sumatoria total de las notas es: ", sumatoria)
    print("El promedio de las notas es: ", promedio)
    print("El porcentaje de las notas son: ", porcentaje, "%")