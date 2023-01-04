#funcion para ingresar un dato entero
def ingreseDatoEntero():
    """
    Esta funcion nos ayuda a que el usuario ingrese un dato entero

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable entero
    """
    #el usuario ingresa un dato entero
    entero = int(input("Ingrese un dato entero: "))
    #la funcion retorna la variable entero
    return entero

#funcion para ingresar un dato flotante
def ingreseDatoFlotante():
    """
    Esta funcion nos ayuda a que el usuario ingrese un dato flotante

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable flotante
    """
    #el usuario ingresa un dato flotante
    flotante = float(input("ingrese un dato flotante o decimal: "))
    #la funcion retorna la variable flotante
    return flotante

#funcion para ingresar un dato string
def ingreseDatoString():
    """
    Esta funcion nos ayuda a que el usuario ingrese un dato string

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable string
    """
    #el usuario ingresa un dato string
    string = input("Ingrese un dato string: ")
    #la funcion retorna la variable string
    return string

#funcion para ingresar un dato lista
def ingreseDatoLista():
    """
    Esta funcion nos ayuda a que el usuario ingrese datos a una lista

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable lista
    """
    #se inicializa la lista
    lista = []
    #el usuario ingresa un dato a la lista
    valores = input("Ingrese valores a la lista: ")
    #la variable lista agarra los datos ingresados
    lista.append(valores)
    #el usuario ingresa una opcion
    opcion = input("desea aniadir otro valor a la lista? ")

    #se crea un ciclo repetitivo para aniadir mas elementos a la lista
    while opcion == "s" or opcion == "S":
        #el usuario ingresa un dato a la lista
        valores = input("Ingrese valores a la lista: ")
        #la variable lista agarra los datos ingresados
        lista.append(valores)
        #el usuario ingresa una opcion
        opcion = input("desea aniadir otro valor a la lista? ")
    #la funcion retorna la variable lista
    return lista

#funcion para ingresar un dato boolean
def ingreseDatoBoolean():
    """
    Esta funcion nos ayuda a que el usuario ingrese datos boolean

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable boolean
    """
    #el usuario ingresa un dato boolean
    datoBoolean = int(input("ingrese el primer valor: "))
    #el usuario ingresa un dato boolean
    datoBoolean2 = int(input("Ingrese el segundo valor: "))
    #se asigna los valores a el dato boolean para true y false
    boolean = datoBoolean > datoBoolean2
    #la funcion retorna la variable boolean
    return boolean

#funcion principal
if __name__ == '__main__':
    #a la variable datoEntero se le asigna lo que retorna la funcion ingreseDatoEntero()
    datoEntero = ingreseDatoEntero()
    #a la variable datoFlotante se le asigna lo que retorna la funcion ingreseDatoFlotante()
    datoFlotante = ingreseDatoFlotante()
    #a la variable datoString se le asigna lo que retorna la funcion ingreseDatoString()
    datoString = ingreseDatoString()
    #a la variable datoLista se le asigna lo que retorna la funcion ingreseDatoLista()
    datoLista = ingreseDatoLista()
    #a la variable datoBool se le asigna lo que retorna la funcion ingreseDatoBoolean()
    datoBool = ingreseDatoBoolean()
    #se imprime los resultados
    print("El valor ", datoEntero,"es un dato de tipo: ", type(datoEntero))
    print("El valor ", datoFlotante,"es un dato de tipo: ", type(datoFlotante))
    print("El valor ", datoString,"es un dato de tipo: ", type(datoString))
    print("Los valores ", datoLista,"son datos de tipo: ", type(datoLista))
    print("El valor ", datoBool,"es un dato de tipo: ", type(datoBool))
