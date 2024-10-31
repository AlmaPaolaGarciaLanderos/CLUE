#Alma Paola Garcia Landeros
#21110038
#7E1
#Inteligencia Artificial
#Centro de Enseñanza Tecnica Industrial 

import random

# Datos del juego
personajes = ["Ludwig van Beethoven", "Wolfgang Amadeus Mozart", "Johann Sebastian Bach", "Frédéric Chopin", "Pyotr Ilyich Tchaikovsky"]
locaciones = ["Teatro de Viena", "Sala de Conciertos Barroca", "Salón de la Ópera Imperial", "Estudio de Composición", "Biblioteca Musical Antigua"]
objetos = ["Batuta antigua", "Piano desafinado", "Cuerda de violín rota", "Atril caído", "Libreto envenenado"]

# Historias de misterio musical
historias = {
    0: (
        "En una majestuosa sala de conciertos, los cinco maestros se reunieron para discutir sus últimos trabajos. "
        "De repente, un estruendo resonó: Beethoven fue hallado inconsciente. "
        "Bach mencionó haber visto un atril tambaleante momentos antes. "
        "Mozart, con una sonrisa enigmática, sugirió que Chopin sabía más de lo que decía. "
        "Tchaikovsky observó una cuerda rota en el suelo, aumentando la tensión entre ellos."
    ),
    1: (
        "En el Teatro de Viena, bajo la luz de los candelabros, se escuchó un grito. "
        "Chopin fue encontrado en el suelo, con un libreto envenenado cerca. "
        "Mozart insinuó que alguien había alterado la partitura de Tchaikovsky, y Beethoven, furioso, señaló a Bach, quien sostenía una batuta antigua."
    ),
    2: (
        "En la biblioteca musical, los compositores debatían sobre la evolución de la música. "
        "De repente, un atril cayó sobre Mozart. "
        "Beethoven comentó que había visto a Tchaikovsky cerca del piano desafinado, mientras que Chopin observó una cuerda rota."
    ),
    3: (
        "En el salón de la ópera, durante los ensayos, un fuerte ruido interrumpió la melodía. "
        "Bach yacía desmayado junto al piano desafinado. "
        "Mozart aseguró que Tchaikovsky había estado cerca del libreto, y Chopin descubrió una batuta tirada en el suelo."
    ),
    4: (
        "En el estudio de composición, un escándalo hizo que todos voltearan. "
        "Tchaikovsky fue hallado sin sentido junto a una cuerda de violín rota. "
        "Beethoven observó el libreto envenenado, mientras que Bach comentó haber visto a Chopin con la batuta antigua poco antes del incidente."
    )
}

# Elección de culpable, objeto y locación
culpable_idx = random.randint(0, len(personajes) - 1)
objeto_idx = random.randint(0, len(objetos) - 1)
locacion_idx = random.randint(0, len(locaciones) - 1)
historia = historias.get(random.randint(0, 4))

# Introducción
print("¡Bienvenido al misterio de la música clásica!")
print("Un misterio ha ocurrido entre los grandes maestros de la música. Tú eres el detective encargado de resolverlo.")
print("A continuación, se te dará una historia que contiene pistas sobre quién es el culpable, qué objeto fue utilizado y en qué locación.\n")

# Mostrar la historia completa
print(historia)

# Pistas finales
print("\nPistas finales:")
print(f"El culpable es uno de estos compositores: {', '.join(personajes)}.")
print(f"El objeto utilizado es uno de estos: {', '.join(objetos)}.")
print(f"La locación del misterio es una de estas: {', '.join(locaciones)}.")
print("\n¡Buena suerte resolviendo el misterio!\n")

# Ciclo del juego
while True:
    print("\nOpciones de personajes:")
    for idx, personaje in enumerate(personajes):
        print(f"{idx + 1}. {personaje}")
    culpable_adivinado = input("¿Quién crees que es el culpable? (Ingresa el número): ")

    print("\nOpciones de objetos:")
    for idx, objeto in enumerate(objetos):
        print(f"{idx + 1}. {objeto}")
    objeto_adivinado = input("¿Qué objeto crees que se utilizó? (Ingresa el número): ")

    print("\nOpciones de locaciones:")
    for idx, locacion in enumerate(locaciones):
        print(f"{idx + 1}. {locacion}")
    locacion_adivinada = input("¿Qué locación crees que se utilizó? (Ingresa el número): ")

    try:
        culpable_adivinado = int(culpable_adivinado) - 1
        objeto_adivinado = int(objeto_adivinado) - 1
        locacion_adivinada = int(locacion_adivinada) - 1

        print("\n¡Resultados finales!")
        print(f"Culpable: {personajes[culpable_idx]}")
        print(f"Objeto: {objetos[objeto_idx]}")
        print(f"Locación: {locaciones[locacion_idx]}")
        print(f"Historia: {historia}")

        if (culpable_adivinado == culpable_idx and
            objeto_adivinado == objeto_idx and
            locacion_adivinada == locacion_idx):
            print("¡Felicidades! Has resuelto el misterio correctamente.")
            break
        else:
            print("No es correcto. Intenta de nuevo.")

    except (ValueError, IndexError):
        print("Entrada inválida. Por favor, ingresa un número válido.")

    jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
    if jugar_nuevamente != 's':
        print("Gracias por jugar. ¡Hasta la próxima!")
        break

