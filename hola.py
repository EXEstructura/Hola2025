def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError as e:
        print(f"Archivo no encontrado: {e}")
    except IOError as e:
        print(f"Error de E/S: {e}")
    else:
        print("El archivo se leyó correctamente.")
    finally:
        print("Finalización del intento de lectura del archivo.")

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print(f"No se puede dividir por cero: {e}")
        return None
    except TypeError as e:
        print(f"Error de tipo: {e}")
        return None
    else:
        print("La división se realizó correctamente.")
        return resultado
    finally:
        print("Fin del bloque try-except.")

# Ejemplos de uso
print(dividir(10, 2))  # División válida
print(dividir(10, 0))  # División por cero
print(dividir(10, "a"))  # Error de tipo
