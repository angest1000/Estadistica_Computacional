import math
import time

def f(x):
    return math.sin(x)

decimales = int(input('¿Con cuantos decimales quieres aproximar a pi?: '))
start_time = time.time()
resultado = 2
lim_inf = 2
lim_sup = 4
tolerancia = float('0.' + '0'*decimales + '1')
start_time = time.time()
iteraciones=0
resultado_anterior = 0
while abs(f(resultado)) > tolerancia:

    resultado_anterior = f(resultado)
    resultado = (lim_inf + lim_sup) / 2
    print(f'sin({resultado}) = {f(resultado)}')
    if f(resultado) > 0:
        lim_inf = resultado
    else:
        lim_sup = resultado
    iteraciones += 1
    if f(resultado) == resultado_anterior:
        print('\nNo es posible iterar mas')
        break
    
print(f'Aproximacion de Pi: {resultado}\n Iteraciones: {iteraciones}')
# print(start_time)
# print(time.time())
print('--- %s seconds ---' % (time.time() - start_time))

     


if __name__ == "__main__":
    pass