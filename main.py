from lib import parimpar

numero = input('ingrese un número para saber si es par/impar:')

try:

    resultado = parimpar(int(numero))

    print('{0} es {1}'.format(resultado,numero))

except ValueError:
    #Caso si es float
    if isinstance(float(numero),float):
        print(f'{numero} no es un número entero')
    else:
        print(f'{numero} no es un número')