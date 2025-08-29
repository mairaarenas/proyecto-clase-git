# ========================================================
# Proyecto: Ejemplo de Repositorio en GitHub
# Autor: Maira Arenas
# Institución: Institución Universitaria Antonio José Camacho
# ========================================================

def saludo():
    """
    Función que muestra un mensaje de saludo
    indicando que todo el proyecto fue realizado
    por la estudiante Maira Arenas.
    """
    print("Hola, soy Maira Arenas y realicé este trabajo completo en GitHub.")

def suma(a, b):
    """
    Función que suma dos números.
    """
    return a + b

def resta(a, b):
    """
    Función que resta dos números.
    """
    return a - b

def multiplicacion(a, b):
    """
    Función que multiplica dos números.
    """
    return a * b

def division(a, b):
    """
    Función que divide dos números, controlando la división por cero.
    """
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b


# ========================================================
# PROGRAMA PRINCIPAL
# ========================================================
if __name__ == "__main__":
    saludo()
    print("Ejemplos de operaciones matemáticas realizadas por Maira Arenas:")
    print("5 + 3 =", suma(5, 3))
    print("10 - 4 =", resta(10, 4))
    print("6 * 7 =", multiplicacion(6, 7))
    print("20 / 5 =", division(20, 5))
    print("20 / 0 =", division(20, 0))
