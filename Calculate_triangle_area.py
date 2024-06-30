# Titulo: calculate_triangle_area.py
# Este programa calcula el área de un triángulo basándose en la base y
# la altura proporcionadas por el usuario que haga uso del programa.

def calculate_area(base, height):
    """
    Calcula el área de un triángulo.

    Args:
    base (float): La base del triángulo.
    height (float): La altura del triángulo.

    Returns:
    float: El área del triángulo.
    """
    return 0.5 * base * height


def main():
    """
    Función principal que pide al usuario la base y la altura del triángulo,
    y luego imprime el área calculada.
    """
    # Solicitaremos al usuario la base y la altura del triángulo
    base = float(input("Introduce la base del triángulo: "))
    height = float(input("Introduce la altura del triángulo: "))

    # Calcular el área
    area = calculate_area(base, height)

    # Nos mostrara el resultado
    print(f"El área del triángulo con base {base} y altura {height} es {area}")


if __name__ == "__main__":
    main()

#El programa ha funcionado correctamente