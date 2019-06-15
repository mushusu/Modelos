# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Se importa modulo
import random

######### Consigna 0
## Se crea una fun. de rango para poder trabajar

def myrango(a, b, p = 1):
    i = a
    c = []
    while  i <= b:
        c.append(i)
        i = i + p
    return c

######### Consigna 0
## Se define una func. de repeticion

def repetirlista(mazoUnitario, c):
    i = 0
    res = []
    while i < c:
        j = 0
        while j < len(mazoUnitario):
            res.append(mazoUnitario[j])
            j = j + 1
        i = i + 1
    return res

######### Consigna 1
## Se define una func donde el parametro sea el n de jug y 
## devuelva ese total de mazos mezclados
    
def generarMazos(n):
    Unmazo = repetirlista(myrango(1,13), 4)
    random.shuffle(Unmazo)
    Mazoxjugador = repetirlista(Unmazo, n)
    return Mazoxjugador

######### Consigna 2
## Se define una func de jugada, toma un mazo m y deja de repartir 
## al llegar a n(21) en la sumatoria del numero de cartas individuales
    
def jugar(m, n=21):    
    suma = 0
    while suma < n and len(m) > 0:
        suma = suma + m.pop(0)
    return suma

######### Consigna 3
## Se define una func para que juegen n cantidad de jugadores
## Recibe un mazo m y j cant de jugadores
    
def jugar_varios(m, j=1):
    i = 0
    res = []
    while i < j:
        res.append(jugar(m))
        i = i + 1
    return res

######### Consigna 4
## Se def una func que diga quien gano 1 = gano; 0 = perdio
## Recibe resultados que es lo que devuelve jugar_varios

def ver_quien_gano(resultados):
    i = 0
    res = []
    while i < len(resultados):
        if resultados[i] == 21:
           res.append(1)
        else:            
            res.append(0)
        i = i + 1
    return res

######### Consigna 5
## Toma un num de repeticiones(nrep) y juega con n cantidad de jugadores

def experimentar(rep, n):
    i = 0
    res = []
    while i < n:
        res.append(0)
        i = i + 1
    while i < rep:
        m = generarMazos(n)
        mano = ver_quien_gano(jugar_varios(m, n))
        j = 0
        while j < len(mano):
            res[j] = res[j] + mano[j]
            j = j + 1
        i = i + 1
    return res
    
# Encontrar la estrategia optima para jugar contra la casa. La casa no
# sabe nuestra jugada. Los dos las muestran al mismo tiempo. Si hay empate gana
# la casa. Hacer una func que sea experimentar_estrategias_contra_la_casa que recibe el 
# rango de estrategias que se quiere experimentar y la cantidad de veces que se
# experimenta para cada par de estrategias. Comparar todas las estrategias 
# que pueden usar el jugador y la casa. Rango de 10 a 21.
# Lo que devuelve esta func es una matriz que tenga la cant de veces que gano 
# un j contra la casa.

## HACE FALTA:
# modificar jugar_varios para que reciba una lista de las diferentes estrategias
# de los jugadores. Cuando se llame ajugar tiene que jugar con su estrategia.
# Cambiar jugar_varios a jugar_casa 

# Nueva func Ver si_gano_ala_casa modificando ver_quien_gano