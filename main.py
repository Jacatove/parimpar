from lib import parimpar
#supervisado por Anita


numero = input('Anita pide que ingrese un número para saber si es par o impar: ')

try:

    resultado = parimpar(int(numero))


    print(f'{numero} es un  {resultado}.')

except ValueError:
    #Caso si es float
    if isinstance(float(numero),float):
        print(f'{numero} no es un número entero.')
    else:
        print(f'{numero} no es un número.')
