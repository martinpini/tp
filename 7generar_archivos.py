import random

# Definir rangos para los valores aleatorios
nombres = ["Ana", "Juan", "María", "Pedro", "Laura", "Carlos", "Isabel", "David", "Sandra", "Pablo", "Roberto", "Cristina", "José", "Marta", "Francisco", "Luis", "Rosa", "Alberto", "Elena", "Antonio", "Jessica", "Alejandro", "Daniel", "Patricia", "Carlos", "Ana", "Juan", "María", "Pedro", "Laura", "Carlos", "Isabel", "David", "Sandra", "Pablo", "Roberto", "Cristina", "José", "Marta", "Francisco", "Luis", "Rosa", "Alberto", "Elena", "Antonio", "Jessica", "Alejandro", "Daniel", "Patricia"]
edades = range(18, 101)
saldos = range(-10000, 100000)

# Abrir archivo en modo escritura
with open("file1.txt", "w") as archivo:
    # Generar 50 registros y escribirlos en el archivo
    for _ in range(50):
        nombre_aleatorio = random.choice(nombres)
        edad_aleatoria = random.choice(edades)
        saldo_aleatorio = random.choice(saldos)
        registro = f"{nombre_aleatorio},{edad_aleatoria},{saldo_aleatorio}\n"
        archivo.write(registro)
