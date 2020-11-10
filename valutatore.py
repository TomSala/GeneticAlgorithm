import random
import math
from music21 import *
int_chart = {'0': ('2', '9', '0'), '2': ('4', '2', '0'),
             '4': ('4', '5', '2'), '5': ('7', '4'),
             '7': ('5', '1', '7'), '9': ('0', '7', '9')}

scala = ['C4','C#4','D','D#4','E','F','F#','G','G#','A','A#','B']

    
def frequenza(f_melodia):
    c_d = 0
    for i in f_melodia:
        if i == 0 or i == 2:
            c_d += 1
    return c_d


def calcolo_fitness(melodia):
    moltiplicatore = frequenza(melodia)
    indice = 0
    for posizione, nota in enumerate(melodia):
        if str(nota) in int_chart:
            try:
                if str(melodia[posizione+1]) in int_chart[str(nota)]:
                    indice += int(int_chart[str(nota)].index(str(melodia[posizione+1])))+1
            except Exception as e:
                pass
                
    return moltiplicatore + indice



for n in range(0,10):
    melodia = []
    for i in range(0,16):
        melodia.append(random.randint(0,11))

    moltiplicatore = calcolo_fitness(melodia)
    print(moltiplicatore)
    stream1 = stream.Stream()
    for nota in melodia:
        stream1.append(note.Note(scala[nota]))
    stream1.write('midi', fp='cache_test//'+str(n)+'.midi')
    moltiplicatore = 1
    



