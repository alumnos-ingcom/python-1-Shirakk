################
# Santiago Catriman - @Shirakk
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def es_primo(numero):
    """
    Si el número es menor que 1, no es primo. Si es 2, es primo. De lo contrario, si es divisible por
    cualquier número entre 2 y él mismo, no es primo. De lo contrario, es primo
    
    :param numero: El número a comprobar
    :return: un valor booleano.
    """
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


def principal():
    """
    Toma un número como entrada y devuelve True si el número es primo y False si no lo es.
    """
    numero = int(input('Escribe un numero: '))
    resultado = es_primo(numero)

    if resultado == True:
        print('El numero es primo')
    else:
        print('El numero no es primo')


if __name__ == '__main__':
    principal()