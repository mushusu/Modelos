#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 10:54:09 2019

@author: mushu

"""
#################################
########### FIGURITAS ###########
#################################

import random
import numpy as np

random.random()
a = np.arange(10)
len(a)
a[:3]
random.shuffle(a)
np.mean(a)
random.randint(1, 10)

## Funcion que simula comprar un paquete de figus
## Param1 es el tamano del album y Param2 es la cant de figus x paq
def generar_paquete(figus_total, figus_paquete=5):
    res = [] 
    for i in range(figus_paquete):
        res.append(random.randint(1, figus_total))
    return res

## Se define una función que interpreta si el album ya esta completo
def albumCompleto(album):
    res = True
    for i in range(len(album)):
        if album[i] == 0:
            res = False
    return res


## Esta funcion recibe el tamaño del mazo y la cant de figus por paquete 
## y devuelve la cantidad de paquetes necesarios para su llenado
def cuantas_figus(figus_total, figus_paquete=5):
    album = figus_total * [0]
    while not albumCompleto(album):
        a = generar_paquete(figus_total, figus_paquete)
        for i in range(len(a)):
            album[a[i]-1] = album[a[i]-1] + 1
    return sum(album)
 

## Funcion de repeticion(r cant de veces) del llenado de un album de n tamano
def nrep(r=1000, n=6,figus_paquete=5):
    res = []
    for i in range(r):
       a = cuantas_figus(n,figus_paquete)
       res.append(a/figus_paquete)
    print(np.mean(res))
    return res


#ejer 2
cuantas_figus(669,1)

#ejer 5
generar_paquete(6, 5)

#ej 8
cuantas_figus(669, 5)

# ejercicio 9 que probabilidad hay de llenar el album con p paquetes
a = nrep(100, 669, 5)

def probdecomp(a, p):
    res = 0
    for i in range(len(a)):
        if a[i] <= p:
            res = res + 1
    return res/len(a)

probdecomp(a, 1150)

