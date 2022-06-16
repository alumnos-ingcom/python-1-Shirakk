################
# Nombre - @Shirakk
# Nombre - Santiago Catriman
# UNRN Andina - Introducción a la Ingenieria en Computación
# 1. Conversión de temperaturas
# Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

# Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit 
# como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. 
# Y viceversa.
################


def convertir_a_fahrenheit(centigrados):
    """
    Toma la temperatura en grados Celsius y la convierte a grados Fahrenheit
    
    :param centigrados: La temperatura en grados Celsius
    """
    fahrenheit = (centigrados * 9/5) + 32
    print(f"{centigrados} grados centigrados son {fahrenheit} grados fahrenheit")
    

def convertir_a_centigrados(fahrenheit):
    """
    Esta funcion toma la temperatura en fahrenheit e imprime la temperatura equivalente en celsius
    
    :para fahrenheit: La temperatura en fahrenheit
    """
    centigrados = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} grados fahrenheit son {centigrados} grados celcius")
    

def principal():
    fin = False
    while not(fin):
        print(
"""
#### Convertidor de temperatura ####
1) Centigrados a Fahrenheit
2) Fahrenheit a Centigrados
3) Salir
"""
)
        opc = int(input("Ingrese la opcion: "))
        if (opc == 1):
            centigrados = float(input("Ingrese los grados centigrados: "))
            convertir_a_fahrenheit(centigrados)
        elif (opc == 2):
            fahrenheit = float(input("Ingrese los grados fahrenheit: "))
            convertir_a_centigrados(fahrenheit)
        elif (opc == 3):
            exit()

if __name__ == "__main__":
    principal()