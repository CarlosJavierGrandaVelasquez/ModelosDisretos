# Definición de hechos y reglas en lógica de predicados

# Hechos
hechos = [
    ('Juan', 'estudiante'),
    ('Maria', 'profesora'),
    ('Pedro', 'estudiante')
]

# Reglas
def es_estudiante(persona):
    return persona[1] == 'estudiante'

def es_profesor(persona):
    return persona[1] == 'profesor'

# Consultas de conocimiento
print("¿Juan es estudiante?")
print(es_estudiante(('Juan', 'estudiante')))

print("¿Maria es profesora?")
print(es_profesor(('Maria', 'profesora')))

