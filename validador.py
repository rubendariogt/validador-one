# Validador RIPS - Creado por Rubén Darío García
# Experiencia trasladada de Hospital Central a Python

import csv

def validar_rips(archivo):
    print(f"Validando archivo: {archivo}")
    errores = []
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lector = csv.reader(f)
            for num_linea, fila in enumerate(lector, 1):
                # Ejemplo: validar que no haya campos vacíos
                if "" in fila or len(fila) < 5:
                    errores.append(f"Línea {num_linea}: campos incompletos -> {fila}")
        
        if not errores:
            print("✅ Archivo RIPS válido - Listo para cargue")
        else:
            print(f"❌ Se encontraron {len(errores)} errores:")
            for e in errores:
                print(e)
                
    except FileNotFoundError:
        print("Archivo no encontrado. Coloca un archivo .txt de RIPS en la carpeta")

# Ejemplo de uso
# validar_rips("AF123456.txt")
if __name__ == "__main__":
    print("Validador RIPS - Ruben Garcia - Python")
    print("Proyecto migrado de experiencia en Dirección de Sanidad")
