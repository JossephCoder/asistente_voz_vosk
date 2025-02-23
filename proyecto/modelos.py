"""
Modulo dedicado a cargar el Modelo IA VOSK y alojarlo
en una OBJETO MODEL, para importarlo para su uso.
Se puede cambiar el MODELO a usar accediendo al Modulo

Contiene un diccionario con las rutas a los modelos
(Usted puede agregar mas segun sus necesidades) 
"""

from os import getcwd
from time import time
from vosk import SetLogLevel, Model

# RUTA DEL MODELO DE IA
ruta_actual = getcwd()

modelos = {

# "normal_es" : ruta_actual + "\\..\\modelos_voz\\vosk-model-es-0.42",
"small_es" : ruta_actual + "\\..\\modelos_voz\\vosk-model-small-es-0.42"

}

# DESACTIVO INFORMACION SOBRE CARGA DEL MODELO
SetLogLevel(-1)

# CARGO EL MODELO
inicio = time()

MODEL = Model(modelos["small_es"])
"""
OBJETO MODEL: Encargado de cargar el Modelo VOSK a usar.

Modelo por defecto: 'small_es' (Modelo Pequeño en Español)
"""

print(f"Modelo cargado: {time() - inicio}")

