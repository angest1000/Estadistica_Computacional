import time
import sys

def fibonacci_rec(n):
    if n == 0 or n==1:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

def fibonacci_dinamico(n,memo = {}):
    if n == 0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo) + fibonacci_dinamico(n-2,memo)
        memo[n] = resultado

        return resultado

if __name__ == "__main__":
    sys.setrecursionlimit(10002)
    numero = int(input('Introduce los numeros de fibonacci que quieres calcular: '))
    for i in range(numero):
        time_ini = time.time()
        print(i,":",fibonacci_dinamico(i))
        tiempo_tot = time.time() - time_ini
        print(f'Tiempo de ejecucion: {round(tiempo_tot,2)}')
    