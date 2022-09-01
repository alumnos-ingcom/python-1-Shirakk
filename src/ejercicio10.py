################
# Santiago Catriman - @Shirakk
# UNRN Andina - Introducción a la Ingenieria en Computación

#Palindromos.
#Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. 
# Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
################
def es_palindromo(texto):
    """
    Toma una cadena, elimina todos los espacios, la pone en minúsculas y luego verifica si la primera
    mitad de la cadena es igual a la segunda mitad de la cadena invertida.
    
    :param texto: la cadena a comprobar
    :return: un valor booleano.
    """
    texto = texto.lower()
    texto = texto.replace(" ", "")
    longitud = len(texto)
    if longitud % 2 == 0:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2:]
    else:
        izquierda = texto[:longitud // 2]
        derecha = texto[longitud // 2 + 1:]

    return izquierda == derecha[::-1]

def principal():
    """
    Imprime un mensaje, le pide al usuario una palabra y luego llama a la función es_palindromo con la
    palabra como argumento.
    :return: El resultado de la función es_palindromo()
    """
    print('El siguiente script le dira si una palabra es palindroma o no ')
    palabra = input('Ingrese la palabra: ')

    resultado = es_palindromo(palabra)
    print(resultado)

if __name__ == "__main__":
    principal()