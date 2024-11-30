# Función para generar el Triángulo de Pascal
def triangulo_pascala(filas):
    # Crear una lista vacía para almacenar el triángulo
    triángulo = []

    # Generar cada fila del triángulo
    for n in range(filas):
        # Iniciar la fila con 1's
        fila = [1] * (n + 1)

        # Llenar la fila con la suma de los dos números de arriba
        for i in range(1, n):
            fila[i] = triángulo[n - 1][i - 1] + triángulo[n - 1][i]

        # Añadir la fila generada al triángulo
        triángulo.append(fila)

    # Imprimir el triángulo con formato
    for fila in triángulo:
        print(' '.join(map(str, fila)).center(filas * 2))  # Centramos los números para mejor visualización


# Solicitar el número de filas al usuario
filas = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))

# Llamar a la función para generar y mostrar el Triángulo de Pascal
triangulo_pascala(filas)
