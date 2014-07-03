#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

How you can clone a list in python?

¿Cómo se puede clonar una lista en python?
'''

#the copy() method allows to obtain a copy of the list.
#this method is add in python 3
lista = [5, 4, 3, 2, 1]
lista_clone = lista.copy()

#Make changes the list_clone
lista_clone.append(100)
print(lista_clone)
print(lista)

#another way is to make a copy using slice or the list() method
lista = [1, 2, 3, 4, 5]
lista_clone = lista[:]

#Make changes the list_clone
lista_clone.append(200)
print(lista_clone)
print(lista)

#copy list using list() method
lista = [3, 5, 1, 2, 4]
lista_clone = list(lista)

#Make changes the list_clone
lista_clone.append(300)
print(lista_clone)
print(lista)
