# Función para generar la Serie de Fibonacci
def fibonacci(n):
    # Inicializar los dos primeros números de la serie
    a, b = 0, 1
    
    # Imprimir los primeros n números de la serie de Fibonacci
    print("Serie de Fibonacci:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Actualizar a y b para la siguiente iteración
    
    print()  # Salto de línea al final

# Solicitar al usuario cuántos términos desea en la Serie de Fibonacci
n = int(input("Ingrese el número de términos de la Serie de Fibonacci: "))

# Llamar a la función para generar y mostrar la serie
fibonacci(n)
