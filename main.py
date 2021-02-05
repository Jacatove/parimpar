from lib import parimpar

numero = input('ingrese un número para saber si es par/impar:')

try:

    resultado = parimpar(int(numero))
    print(resultado)
except ValueError:
    print(f'{numero} no es un número')