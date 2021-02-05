
def parimpar(num):
    """Esta función determina si un número entero es par o impar

    input:
        num (entero)

    output:
        'par' (str)
        'impar' (str)
    """
    #Utilizamos el concepto del modulo % matemático
    if num%2 == 0:
        return 'par'
    return 'impar'