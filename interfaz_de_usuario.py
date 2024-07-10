#interfaz_de_usuario.py

def obtener_datos_usuario(conocimiento):
    nombre = input("Ingrese el nombre del usuario: ")
    edad = int(input("Ingrese la edad del usuario: "))
    
    # Obtener lista de géneros únicos de la base de conocimiento
    generos = set()
    for pelicula, info in conocimiento['peliculas'].items():
        generos.add(info['genero'])
    
    # Mostrar los géneros disponibles al usuario
    print("\nGéneros cinematográficos disponibles:")
    for idx, genero in enumerate(generos, start=1):
        print(f"{idx}. {genero}")
    
    gustos = []
    while True:
        gusto = input("\nIngrese un gusto cinematográfico del usuario (o 'terminar' para finalizar): ")
        if gusto.lower() == 'terminar':
            break
        if gusto.capitalize() in generos:  # Verificar que el género ingresado esté en la lista de géneros disponibles
            gustos.append(gusto.capitalize())
        else:
            print("\nGénero no válido. Por favor ingrese un género válido de la lista.")
    
    return nombre, gustos, edad


def mostrar_recomendaciones(recomendaciones):
    if recomendaciones:
        print("\nPelículas recomendadas:")
        for pelicula in recomendaciones:
            print(f"- {pelicula}")
    else:
        print("\nNo hay recomendaciones disponibles.")
