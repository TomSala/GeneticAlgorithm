import random
import math
from music21 import *

'''
int_chart = {'0': ('2', '9', '0'), '2': ('4', '2', '0'),
             '4': ('4', '5', '2'), '5': ('7', '4'),
             '7': ('5', '1', '7'), '9': ('0', '7', '9')}
'''
#Interval Distributions, Mode, and Tonal Strength of Melodies as Predictors of Perceived Emotion

main_chart = {'1': 12.04, '-1': 14.86, '2': 12.91,
         '-2': 17.64, '3': 5.38, '-3':4.53, '4':2.77, '-4': 3.55,
         '5': 4.24, '-5': 2.69}
scala = ['C4','C#4','D','D#4','E','F','F#','G','G#','A','A#','B']



def ascdesc(melodia, chart=main_chart):
    moltiplicatore = 1
    for i in range(0,len(melodia)-1):
        s = i + 1
        delta = melodia[s]-melodia[i]
        if delta != 0 and delta in range(-5,6):
            delta = str(delta)
            moltiplicatore *= chart[delta]
        elif delta == 0:
            moltiplicatore *= 2
        else:
            moltiplicatore *= 0.3
    return math.sqrt(math.sqrt(moltiplicatore))

'''    
def frequenza(f_melodia):
    c_d = 0
    for i in f_melodia:
        if i == 0 or i == 2:
            c_d += 1
    return c_d

def calcolo_fitness(melodia):
    delta_lista
    for i in range(len(melodia)):
        delta = abs(melodia[i]-melodia[i+1])


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
'''


for n in range(0,10):
    melodia = []
    for i in range(0,10):
        melodia.append(random.randint(0,11))

    moltiplicatore = math.sqrt(math.sqrt(ascdesc(melodia)))
    stream1 = stream.Stream()
    for nota in melodia:
        stream1.append(note.Note(scala[nota]))
    stream1.write('midi', fp='T://datasets//musica//'+str(n)+".midi")
    print(moltiplicatore)

    



