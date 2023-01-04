"""
NOMBRE: CARLOS JAVIER GRANDA VELASQUEZ
MATERIA: MODELOS DISCRETOS 8001
FECHA: 03 - 01 - 2023
"""
#funcion para ingresar el nombre del trabajador
def ingresoNombre():
    """
    Esta funcion nos ayuda a que el usuario ingrese el nombre del trabajador

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable nombre
    """
    #el usuario ingresa el nombre del trabajador y lo guarda en un variable nombre
    nombre = input("ingrese el nombre del trabajador: ")
    #la funcion retorna la variable nombre
    return nombre

#funcion para ingresar el sueldo por hora
def sueldoPorHora():
    """
    Esta funcion nos ayuda a que el usuario ingrese el sueldo por hora

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable sueldoHoras
    """
    #el usuario ingresa el sueldo por hora
    sueldoHoras = int(input("ingrese el sueldo por hora: "))
    #la funcion retorna la variable sueldoHoras
    return sueldoHoras

#funcion para ingresar las horas trabajadas
def HorasTrabajo():
    """
    Esta funcion nos ayuda a que el usuario ingrese las horas trabajadas por el trabajador

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable horasTrabajadas
    """
    #el usuario ingresa las horas que trabajo
    horasTrabajadas = int(input("ingrese las horas trabajadas: "))
    #la funcion retorna la variable horasTrabajadas
    return horasTrabajadas

#funcion para calcular el sueldo total
def sueldoTotal():
    """
    Esta funcion nos ayuda a que se calcule el sueldo total

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable sueldo
    """
    #a la variable sueldo se le asigna la multiplicacion de sueldoPorHoras con horasDeTrabajo
    sueldo = sueldoPorHoras * horasDeTrabajo
    #la funcion retorna la variable sueldo
    return sueldo

#funcion principal
if __name__ == '__main__':
    #a la variable nombreTrabajador se le asigna lo que retorna la funcion ingresoNombre()
    nombreTrabajador = ingresoNombre()
    #a la variable sueldoPorHoras se le asigna lo que retorna la funcion sueldoPorHora()
    sueldoPorHoras = sueldoPorHora()
    #a la variable horasDeTrabajo se le asigna lo que retorna la funcion HorasTrabajo()
    horasDeTrabajo = HorasTrabajo()
    #a la variable salarioTotal se le asigna lo que retorna la funcion sueldoTotal()
    salarioTotal = sueldoTotal()
    #se imprime los resultados
    print("El nombre del trabajador es: ", nombreTrabajador)
    print("El sueldo por cada hora es: ", sueldoPorHoras)
    print("Las horas trabajadas por el trabajador son: ", horasDeTrabajo)
    print("El sueldo total ganado por el trabajador es: ", salarioTotal)
