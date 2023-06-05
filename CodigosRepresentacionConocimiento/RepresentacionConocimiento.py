# Representación del conocimiento en Python

# Definición de hechos
hechos = {
    'Juan': {
        'edad': 25,
        'profesion': 'Ingeniero',
        'ciudad': 'Madrid'
    },
    'Maria': {
        'edad': 30,
        'profesion': 'Abogada',
        'ciudad': 'Barcelona'
    }
}

# Definición de reglas
def es_mayor_de_edad(persona):
    if hechos[persona]['edad'] >= 18:
        return True
    else:
        return False

# Consulta de conocimiento
nombre = 'Juan'
print(f"¿{nombre} es mayor de edad?")
if es_mayor_de_edad(nombre):
    print("Sí, es mayor de edad.")
else:
    print("No, no es mayor de edad.")