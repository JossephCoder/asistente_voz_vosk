"""
Modulo dedicado a recopilar las funciones de otro modulo.

Proximamente podra recopilar mas objetos.
"""

from inspect import getmembers, isfunction

def recopilar_funciones(modulo):
    """
    Función que recopila las funciones de un modulo y
    las agrega a un diccionario automáticamente
    """

    diccionario:dict = {}
    
    for nombre, funcion in getmembers(modulo, isfunction):
        # Reemplaza los guiones bajos con espacios
        nombre_modificado = nombre.replace('_', ' ')
        diccionario[nombre_modificado] = funcion

    return diccionario

# recopilar_funciones(__import__(__name__))