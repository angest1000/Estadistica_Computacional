import random

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)
    suma = 0
    for x in X:
        suma += (x - mu)**2
    return suma / len(X)

def desviacion_estandar(X):
    return (varianza(X))**0.5

if __name__ == "__main__":
    X = [random.randint(9,12) for i in range(20)]
    mu = media(X)
    var = varianza(X)
    sigma = desviacion_estandar(X)
    
    print(f'Arreglo X: {X}')
    print(f'Media: {mu}')
    print(f'Varianza: {var}')
    print(f'Desviacion estandar: {sigma}')