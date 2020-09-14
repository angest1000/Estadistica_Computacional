#Crear un programa que calcule la probabilidad de que salga 12 tirando 2 dados 10 veces

import random 

def tirar_dados(numero_de_dados,numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = 0
        for _ in range(numero_de_dados):
            tiro = tiro + random.choice([1,2,3,4,5,6])
        
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros,numero_de_intentos,tiro_acert,numero_de_dados):
    tiros = []

    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dados(numero_de_dados,numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_acertados = 0
    for tiro in tiros:
        if tiro_acert in tiro:
            tiros_acertados += 1

    probabilidad_tiros_acertados = tiros_acertados / numero_de_intentos
    print(f'Probabilidad de obtener por lo menos un {tiro_acert} con {numero_de_dados} {"dados" if numero_de_dados > 1 else "dado"}\n en {numero_de_tiros} tiros = {probabilidad_tiros_acertados}')    
    print(f'Probabilidad de no obtener un {tiro_acert} con {numero_de_dados} {"dados" if numero_de_dados > 1 else "dado"}\n en {numero_de_tiros} tiros = {1 - probabilidad_tiros_acertados}')
if __name__ == "__main__":
    
    tiro_acert =  int(input('Que numero quieres estudiar: '))
    numero_de_dados = int(input('Cuantos dados quieres simular: '))
    numero_de_tiros = int(input('Tiros del dado: '))
    numero_de_intentos = int(input('Numero de simulaciones: '))

    main(numero_de_tiros,numero_de_intentos,tiro_acert,numero_de_dados)