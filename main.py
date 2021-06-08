#!/usr/bin/env python
# coding: utf-8

from music21 import *
import random

N_STEP = 5

scala = ['C4','C#4','D','D#4','E','F','F#','G','G#','A','A#','B']
musica = [0, 2, 4, 0, 0, 2, 4, 0, 4, 5, 7, 4, 5, 7, 7, 9]
musica2 = [0, 2, 4, 0, 0, 2, 4, 0, 4, 5, 7, 4, 5, 7, 7, 9]

def genera_lista():
    lista = []
    for i in range(0, 16):
        lista.append(random.randint(0,11))
    return lista

def esporta(sequenza, nome_file):
    scala = ['C4','C#4','D','D#4','E','F','F#','G','G#','A','A#','B']
    stream1 = stream.Stream()
    for nota in sequenza:
        stream1.append(note.Note(scala[nota]))
    stream1.write('midi', fp='T://datasets//musica//'+nome_file)

def crossover(lista1, lista2):
    lista1 = lista1.copy()
    lista2 = lista2.copy()
    p_troncamento = random.randint(1,14)
    testa1 = lista1[:p_troncamento]
    testa2 = lista2[:p_troncamento]
    coda1 = lista1[p_troncamento:]
    coda2 = lista2[p_troncamento:]
    return testa1 + coda2, testa2 + coda1

def mutazione(lista):
    lista = lista.copy()
    segno_mutazione = random.randint(0,1)
    p_mutazione = random.randint(0,15)
    if segno_mutazione == 1:
        if lista[p_mutazione] == 11:
            lista[p_mutazione] -= 1
        else:
            lista[p_mutazione] += 1
    if segno_mutazione == 0:
        if lista[p_mutazione] == 0:
            lista[p_mutazione] += 1
        else:
            lista[p_mutazione] -= 1
    return lista

def genitori(popolazione, fitness):
    def genitore(popolazione, fitness):
        poss_gen = []
        for i in range(0,3):
            poss = random.randint(0,9)
            poss_gen.append(poss)
        valori_fit = []
        for scelta in poss_gen:
            valori_fit.append(fitness[scelta])
        valori_fit.sort()
        valori_fit.reverse()
        pos_gen = valori_fit[0]
        pos_gen = fitness.index(pos_gen)
        gen = popolazione[pos_gen] #popolazione[pos_gen1]
        return gen
    gen1 = genitore(popolazione, fitness)
    gen2 = genitore(popolazione, fitness)
    return gen1, gen2

def assegna_fitness(labels):
    lista_vuota = []
    for i in labels:
        msg = str("Fitness sequenza" + str(i) + ': ')
        value = input(str(msg))
        lista_vuota.append(value)

def elitarismo(popolazione1, popolazione2, fitness1, fitness2):
    peggiore = min(fitness2)
    migliore = max(fitness1)
    indice_peggiore = fitness2.index(peggiore)
    indice_migliore = fitness1.index(migliore)
    del popolazione2[indice_peggiore]
    del fitness2[indice_peggiore]
    sequenza_migliore = popolazione1[indice_migliore]
    popolazione1.append(sequenza_migliore)
    fitness2.append(migliore)
    return popolazione2, fitness2

#STEP 0: creazione popolazione di partenza e associazione fitness
popolazione = []
nomi_esportazione = []

for i in range(0,10):
    popolazione.append(genera_lista())

for i, m in enumerate(popolazione):
    filename = str('m0 '+str(i)+'.midi')
    nomi_esportazione.append(filename)
    esporta(m, filename)

fitness = []

for i, m in enumerate(nomi_esportazione):
    msg = str('Fitness ' + str(m) + ' ')
    valore_fitness = input(str(msg))
    fitness.append(valore_fitness)


#STEP 1: elaborazione popolazione1 e associazione fitness1
for step in range(0, N_STEP):
    popolazione1 = []
    fitness1 = []
    for i in range(0,5):
        gen1, gen2 = genitori(popolazione, fitness)
        c1, c2 = crossover(gen1, gen2)
        c1 = mutazione(c1)
        c2 = mutazione(c2)
        popolazione1.append(c1)
        popolazione1.append(c2)
        
    nomi_esportazione = []
    for i, m in enumerate(popolazione1):
        filename = 'm'+str(step+1)+' '+str(i)+'.midi'
        nomi_esportazione.append(filename)
        esporta(m, filename)

    for i, m in enumerate(nomi_esportazione):
        msg = str('Fitness ' + str(m) + ' ')      
        valore_fitness = input(str(msg))
        fitness1.append(valore_fitness)
    
    popolazione1, fitness1 = elitarismo(popolazione, popolazione1, fitness, fitness1)
    popolazione = popolazione1
    fitness = fitness1
