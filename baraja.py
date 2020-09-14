import random
import collections

PALOS = ('Espada','Corazon','Trebol','Diamante')
VALORES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((valor,palo))
    return barajas

def obtener_mano(barajas,tamanio_mano):
    mano = random.sample(barajas,tamanio_mano)
    return mano

def escalera(valores):
    valores_cartas = []
    for val in valores:
        if val in ['A','K','Q','J']:
            if val == 'A':
                valores_cartas.append(1)
            elif val == 'K':
                valores_cartas.append(13)
            elif val == 'Q':
                valores_cartas.append(12)
            else:
                valores_cartas.append(11)
        else:
            valores_cartas.append(int(val))

    valores_cartas = sorted(valores_cartas)
    consecutivos = 0

    for i in range(len(valores)-1):
        if valores_cartas[i+1] - valores_cartas[i] == 1:
            consecutivos += 1
    if consecutivos  == len(valores)-1:
        return 1
    elif valores_cartas == [1,10,11,12,13]:
        return 2
    else:
        return 0

def color(palos):
    contador = 0
    for i in range(len(palos)-1):
        if palos[i+1] == palos[i]:
            contador += 1
    if contador == len(palos)-1:
        return True
    else:
        return False

def main(tamanio_mano,intentos,mano_a_obtener):
    manos_de_poker = {1:'Un Par'
        ,2:'Dos Pares'
        ,3:'Tercia'
        ,4:'Escalera'
        ,5:'Color'
        ,6:'Full House'
        ,7:'Poker'
        ,8:'Escalera de color'
        ,9:'Escalera Real'}    

    barajas = crear_baraja()
    
    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas,tamanio_mano)
        manos.append(mano)

    juego = 0
    num_manos = 0

    for mano in manos:
        valores = []
        palos = []
        for carta in mano:
            valores.append(carta[0])
            palos.append(carta[1])
        counter = dict(collections.Counter(valores))
        # print(counter)

        if mano_a_obtener == 1:  #Par 
            par = 0
            for val in counter.values():
                if val == 2:
                    par +=1
            if par == 1:
                juego += 1
                # print(f'Numero de manos: {num_manos}')
                # print(mano)

        elif mano_a_obtener == 2:    #2 Pares
            par = 0
            for val in counter.values():
                if val == 2:
                    par += 1
            if par == 2:
                juego += 1
                # print(f'Numero de manos: {num_manos}')
                # print(mano)

        elif mano_a_obtener == 3:   #Tercia
            for val in counter.values():
                if val == 3:
                    juego += 1
                    # print(f'Numero de manos: {num_manos}')
                    # print(mano)
                    
        elif mano_a_obtener == 4:   #Escalera
            if escalera(valores) in [1,2]:
                juego += 1
                # print(f'Numero de manos: {num_manos}')
                # print(mano)
                # break

        elif mano_a_obtener == 5:   #Color
                if color(palos):
                    juego += 1
                    # print(f'Numero de manos: {num_manos}')
                    # print(mano)
                    # break

        elif mano_a_obtener == 6:   #Full House
            full_house = 0
            for val in counter.values():
                if val == 2:
                    full_house +=2
                elif val == 3:
                    full_house += 3
            if full_house == 5:
                juego += 1
                # print(f'Numero de manos: {num_manos}')
                # print(mano)
                # break

        elif mano_a_obtener == 7:   #Poker
            for val in counter.values():
                if val == 4:
                    juego += 1
                    # print(f'Numero de manos: {num_manos}')
                    # print(mano)
                    break

        elif mano_a_obtener == 8:   #Escalera de Color
            if escalera(valores) == 1:
                if color(palos):
                    juego += 1
                    # print(f'Numero de manos: {num_manos}')
                    # print(mano)
                    # break
        elif mano_a_obtener == 9:   #Escalera real
            if escalera(valores) == 2:
                if color(palos):
                    juego += 1
                    # print(f'Numero de manos: {num_manos}')
                    # print(mano)
                    # break
        num_manos += 1
    probabilidad_juego = juego / intentos

    # print(f'\n\nNumero de veces que aparece {manos_de_poker[mano_a_obtener]} :{juego}')
    # print(f'Intentos: {intentos}')
    print(f'\nProbabilidad de obtener {manos_de_poker[mano_a_obtener]} en una mano de {tamanio_mano} cartas es: {probabilidad_juego}')

if __name__ == "__main__":

    tamanio_mano = int(input('\nNumero de cartas en la mano: '))
    manos = """\nElija el numero de mano que quiere extraer:
    
    1:Par (Dos cartas del mismo valor)
    2:Dos Pares 
    3:Tercia (Tres cartas del mismo valor)
    4:Escalera (5 cartas consecutivas)
    5:Color (5 cartas con el mismo palo)
    6:Full House (3 cartas del mismo valor + 2 cartas del mismo valor)
    7:Poker (4 cartas del mismo valor)
    8:Escalera de color (5 cartas consecutivas del mismo palo)
    9:Escalera Real (A,K,Q,J,10 del mismo palo)
    10:Todas alv
    
Opcion: """
    mano_a_obtener = int(input(manos))
    intentos = int(input('\nIntentos para calcular la probabilidad: '))

    if mano_a_obtener == 10:
        for i in range(1,10):
            main(tamanio_mano,intentos,i)
    else:
        main(tamanio_mano,intentos,mano_a_obtener)
        