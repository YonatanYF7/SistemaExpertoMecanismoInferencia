#motor_de_inferencia.py
import json

def agregar_usuario(conocimiento, nombre, gustos, edad):
    conocimiento['usuarios'][nombre] = {'gusto': gustos, 'edad': edad}

def mostrar_base_de_conocimiento(conocimiento):
    print("\nBase de Conocimiento Actualizada:")
    for usuario, datos in conocimiento['usuarios'].items():
        print(f"Usuario: {usuario}, Gustos: {datos['gusto']}, Edad: {datos['edad']}")

def inferir_recomendaciones(nombre, conocimiento):
    gustos = conocimiento['usuarios'][nombre]['gusto']
    edad = conocimiento['usuarios'][nombre]['edad']
    
    recomendaciones = []
    
    for pelicula, info in conocimiento['peliculas'].items():
        if info['genero'] in gustos and edad >= info['edad_recomendada']:
            recomendaciones.append(pelicula)
    
    return recomendaciones
