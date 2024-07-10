#main.py

import json
from base_de_conocimiento import conocimiento
from motor_de_inferencia import inferir_recomendaciones, agregar_usuario, mostrar_base_de_conocimiento
from interfaz_de_usuario import obtener_datos_usuario, mostrar_recomendaciones

def guardar_base_de_conocimiento(conocimiento):
    with open('base_de_conocimiento.py', 'w', encoding='utf-8') as file:
        file.write("conocimiento = {\n")
        
        # Escribir la sección de usuarios
        file.write("    'usuarios': {\n")
        for usuario, datos in conocimiento['usuarios'].items():
            file.write(f"        '{usuario}': {datos},\n")
        file.write("    },\n")
        
        # Escribir la sección de películas
        file.write("    'peliculas': {\n")
        for pelicula, info in conocimiento['peliculas'].items():
            file.write(f"        '{pelicula}': {info},\n")
        file.write("    }\n")
        
        file.write("}\n")

def sistema_experto(conocimiento):
    nombre, gustos, edad = obtener_datos_usuario(conocimiento)  # Pasar conocimiento como argumento
    
    if nombre not in conocimiento['usuarios']:
        agregar_usuario(conocimiento, nombre, gustos, edad)
        guardar_base_de_conocimiento(conocimiento)
        mostrar_base_de_conocimiento(conocimiento)
    
    recomendaciones = inferir_recomendaciones(nombre, conocimiento)
    mostrar_recomendaciones(recomendaciones)

# Ejecutar el sistema experto
sistema_experto(conocimiento)
