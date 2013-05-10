#!/usr/bin/env python # -*- coding: utf-8 -*- 

from operator import itemgetter

def ingreso(diccionario, A):
    try:
        diccionario[A] = diccionario[A] + 1 
    except:
        diccionario[A] = 1

def funes():
    f= open("funes.txt", "r",encoding = 'utf-8')
    lines = f.read()
    lines = lines.lower()
    lista = lines.split()
    diccionario = {}
    diccionario = dict.fromkeys(lista,0)


    for A in lista:
        ingreso(diccionario,A) 

    diccionario = sorted(diccionario.items(),key=itemgetter(1),reverse=True)
    for A in diccionario:
        print (A)
    f.close()

funes()
