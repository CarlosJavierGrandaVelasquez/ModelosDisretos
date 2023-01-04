#funcion para ingresar el nombre
def ingresarNombre():
    """
    Esta funcion nos ayuda a que el usuario ingrese su nombre

    Parametros:
    -----------------
        no tiene parametros

    Retorna:
    -----------------
        retorna la variable nombre
    """
    #el usuario ingresa su nombre
    nombre = input("Ingrese su nombre: ")
    #la funcion retorna la variable nombre
    return nombre

#funcion principal
if __name__ == '__main__':
    #a la variable nombreUsuario se le asinga lo que retorna la funcion ingresarNombre()
    nombreUsuario = ingresarNombre()
    #se imprime el saludo
    print("Hola ", nombreUsuario, "Ten un buen dia y que pases bien, exitos.")