import math

def calcular_mcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def descomponer_factores_primos(n):
    i = 2
    factores = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factores.append(i)
    if n > 1:
        factores.append(n)
    return factores

def explicar_mcm(num1, num2, mcm):
    factores_num1 = descomponer_factores_primos(num1)
    factores_num2 = descomponer_factores_primos(num2)
    
    print(f"\nPara encontrar el MCM de {num1} y {num2} seguimos estos pasos:")
    print(f"1. Descomponemos {num1} en factores primos.")
    print(f"   {num1} = {' * '.join(map(str, factores_num1))}")
    print(f"2. Descomponemos {num2} en factores primos.")
    print(f"   {num2} = {' * '.join(map(str, factores_num2))}")
    print("3. Tomamos el mayor exponente de cada factor primo presente en las descomposiciones.")
    print("4. Multiplicamos estos factores para obtener el MCM.")
    print(f"\nEntonces, el MCM de {num1} y {num2} es: {mcm}")

def main():
    while True:
        print("Este programa calcula el Mínimo Común Múltiplo (MCM) de dos números.")
        num1 = int(input("Por favor, introduce el primer número: "))
        num2 = int(input("Por favor, introduce el segundo número: "))

        mcm = calcular_mcm(num1, num2)
        
        explicar_mcm(num1, num2, mcm)

        repetir = input("\n¿Quieres calcular el MCM de otros números? (sí/no): ").strip().lower()
        if repetir != 'sí' and repetir != 'si':
            print("Gracias por usar el programa. ¡Adiós!")
            break

if __name__ == "__main__":
    main()

