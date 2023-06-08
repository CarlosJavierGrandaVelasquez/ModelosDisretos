# Definir la base de conocimientos como un diccionario de listas
base_conocimientos = {
    'es_hijo_de': [
        ('Juan', 'Pedro'),
        ('María', 'Pedro'),
        ('Pedro', 'Luisa')
    ],
    'es_padre_de': [
        ('Pedro', 'Carlos'),
        ('Pedro', 'Laura'),
        ('Luisa', 'Pedro')
    ]
}

# Definir las consultas
consulta_1 = lambda x: [hijo for hijo, padre in base_conocimientos['es_hijo_de'] if padre == x]
consulta_2 = lambda x: [padre for hijo, padre in base_conocimientos['es_hijo_de'] if hijo == x]
consulta_3 = lambda x: [hijo for padre, hijo in base_conocimientos['es_padre_de'] if padre == x]
consulta_4 = lambda x: [padre for padre, hijo in base_conocimientos['es_padre_de'] if hijo == x]

# Realizar consultas e imprimir resultados
print("Hijos de Pedro:")
print(consulta_1('Pedro'))

print("Padre de María:")
print(consulta_2('María'))

print("Hijos de Pedro:")
print(consulta_3('Pedro'))

print("Padre de Laura:")
print(consulta_4('Laura'))
