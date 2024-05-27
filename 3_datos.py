def word_frequency(text):
    """
    Calcula la frecuencia de palabras en una cadena de texto.

    Parámetros:
        text (str): La cadena de texto a analizar.

    Retorno:
        dict: Un diccionario donde las claves son las palabras y los valores son las frecuencias.

    Ejemplo:
        text = "Esta es una frase con palabras repetidas."
        freq = word_frequency(text)
        print(freq)
        # Salida: {'Esta': 1, 'es': 1, 'una': 1, 'frase': 1, 'con': 1, 'palabras': 2, 'repetidas': 1}
    """
    # Convertir el texto a minúsculas y eliminar espacios en blanco innecesarios
    text = text.lower().strip()

    # Dividir el texto en palabras
    words = text.split()

    # Inicializar un diccionario vacío para almacenar las frecuencias
    freq = {}

    # Recorrer cada palabra
    for word in words:
        # Verificar si la palabra ya está en el diccionario
        if word in freq:
            # Si la palabra ya está, incrementar su frecuencia
            freq[word] += 1
        else:
            # Si la palabra es nueva, agregarla al diccionario con frecuencia 1
            freq[word] = 1

    # Devolver el diccionario con las frecuencias de palabras
    return freq

# Ejemplo de uso
text = "Esta es una frase con palabras repetidas. La otra frase es similar pero con diferentes palabras."
freq = word_frequency(text)
print(freq)

# Leer datos de un archivo de texto
with open('datos.txt', 'r') as f:
    text = f.read()

# Calcular la frecuencia de palabras
freq = word_frequency(text)

# Procesar el resultado
print(f"Frecuencias de palabras:")
for word, count in freq.items():
    print(f"{word}: {count}")
