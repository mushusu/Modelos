#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:13:31 2019

@author: mushu
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# Se genera un bosque vacio de tamano n
def bosque(n):
    res = []
    i = 1
    while i <= n:
        res.append(0)
        i = i + 1
    return res

##### Ejercicio 2 #####
# Funcion para establecer la posibilidad de un evento
def suceso_aleatorio(prob):
    azar = random.random()
    if azar < prob:
        return True
    else:
        return False

# A partir de un bosque de tamaño n y un valor p puede generar un
# arbol en c/celda vacía con probabilidad p
def brotes(xbos, p=0.6):
    for i in range(len(xbos)):
        cond = suceso_aleatorio(p)
        if cond:
            xbos[i] = 1
        if not cond:
            xbos[i] = 0
    return xbos

############
# Consigna 3
# dale un bosque en lista y te tira el estado del bosque en numeros

def cuantos(bosque):
    celda0 = bosque.count(0)
    celda1 = bosque.count(1)
    celdam1 = bosque.count(-1)
    print('Lugares vacios: ', celda0)
    print('Arboles vivos: ', celda1)
    print('Arboles quemados: ', celdam1)
    return

############
# Consigna 4
# Se tira un rayo a ver que pasa, si le cae a un arbol se quema, si le cae a
# una celda vacia no pasa nada

def rayos(bosque, f=0.6):
    for i in range(len(bosque)):
        cond = suceso_aleatorio(f)
        if cond:
            if bosque[i] == 1:
                bosque[i] = -1
    return

############
# Consigna 5
# Tenemos un bosque con arb quemados, vivos y celdas vacias
# La idea es que se quemen los restantes arboles vivos que
# esten al lado de los incendiados:

def propagacion(bosque):
    for i in range(1, len(bosque)):
        if bosque[i] == 1 and bosque[i-1] == -1:
            bosque[i] = -1
    bosque2 = bosque[::-1]
    for i in range(1, len(bosque)):
         if bosque2[i] == 1 and bosque2[i-1] == -1:
            bosque2[i] = -1
    return

############
# Consigna 6
# Se reemplazan los arboles quemados por celdas vacias

def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] == -1:
            bosque[i] = 0
    return bosque

############
# Consigna 7
# acá se acopla todo para simular varios(nrep) incendios

def simulacion(tamano, nrep):
    i = 1
    viv = []
    while i == 1:
        modelo1 = bosque(tamano)
        brotes(modelo1)
        rayos(modelo1, 0.02)
        propagacion(modelo1)
        limpieza(modelo1)
        viv.append(modelo1.count(1))
        i = i + 1
    while i <= nrep:
        brotes(modelo1)
        rayos(modelo1, 0.02)
        propagacion(modelo1)
        limpieza(modelo1)
        viv.append(modelo1.count(1))
        i = i + 1
    return viv

a = simulacion(100,50)

plt.plot(a)
asdasd
#pltasdad
#asdasd
