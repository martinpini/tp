# Escribir una función que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y la 
# cantidad de veces que aparece (frecuencia). 
# Escribir otra función que reciba el diccionario generado 
# con la función anterior y devuelva una tupla con la
# palabra más repetida y su frecuencia.


import string

def word_frequency(text):
    """
    Crea un diccionario con cada palabra en una cadena de caracteres y la cantidad de veces que aparece (frecuencia).

    Parámetros:
        text (str): La cadena de caracteres a analizar.

    Retorno:
        dict: Un diccionario con cada palabra en la cadena de caracteres y la cantidad de veces que aparece (frecuencia).
    """
    # Convertir a minúsculas y eliminar puntuación
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def most_repeated_word(freq):
    """
    Encuentra la palabra más repetida en un diccionario de frecuencias y devuelve una tupla con la palabra y su frecuencia.

    Parámetros:
        freq (dict): Un diccionario con cada palabra en una cadena de caracteres y la cantidad de veces que aparece (frecuencia).

    Retorno:
        tuple: Una tupla con la palabra más repetida y su frecuencia.
    """
    max_count = max(freq.values())
    for word, count in freq.items():
        if count == max_count:
            return word, max_count

def load_text_from_file(file_path):
    """
    Carga el contenido de un archivo de texto.

    Parámetros:
        file_path (str): La ruta al archivo de texto.

    Retorno:
        str: El contenido del archivo de texto.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Cargar datos desde un archivo de texto
    file_path = "example.txt"
    text = load_text_from_file(file_path)

    # Calcular la frecuencia de cada palabra
    freq = word_frequency(text)

    # Mostrar el resultado con explicación
    print("Frecuencia de cada palabra:")
    for word, count in freq.items():
        print(f"{word}: {count}")

    # Encontrar la palabra más repetida
    most_repeated = most_repeated_word(freq)

    # Mostrar el resultado con explicación
    print("\nPalabra más repetida:")
    print(f"{most_repeated[0]}: {most_repeated[1]}")

if __name__ == "__main__":
    main()
