"""
Modulo de Python con una lista de funciones que ejecutan
comandos y/o acciones en el Sistema Operativo Windows
"""

import subprocess
import pyautogui
import keyboard
import pyttsx3
import os
from time import sleep
from datetime import datetime
from transcribir_voz import TranscriptorVoz

TRANSCRIPTOR = TranscriptorVoz()
WIDTH, HEIGHT = pyautogui.size()
engine = pyttsx3.init()


# ~~~~ COMANDOS DE WINDOWS NATIVOS

# 1. Abrir Programas

def abrir_bloc_de_notas():
    subprocess.Popen(["notepad.exe"])

def abrir_biblioteca():
    os.system("explorer.exe")

def abrir_navegador():
    os.system("start msedge --inprivate")

def abrir_cmd():
    os.system("cmd.exe")

def abrir_calculadora():
    os.system("calc.exe")

def abrir_panel_de_control():
    os.system("control.exe")

def abrir_administrador_de_tareas():
    keyboard.send('ctrl + shift + esc')

# 2. Ejecutar acciones

def minimizar_todo():
    keyboard.send('win + d')

def cerrar_ventana():
    keyboard.send('alt + f4')

def copiar():
    keyboard.send('ctrl + c')

def pegar():
    keyboard.send('ctrl + v')

def cambiar_ventana():
    keyboard.send('alt + tab')




# ~~~~ COMANDOS ESPECIALES

def escritura(
        TRANSCRIPTOR = TRANSCRIPTOR,
        duracion:int = 5,
        microfono:int = None,
        engine = engine
):
    engine.say("Listo para escribir")
    engine.runAndWait()

    while True:

        try:
            print(f"\33[KESCUCHANDO ESCRITURA")
            engine.say("Escribiendo")
            engine.runAndWait()

            comando = TRANSCRIPTOR.transcribir_voz(duracion, microfono)

            if comando is None:
                raise ValueError("Algo ha pasado. Texto reconocido es 'None'\n")
            
            elif comando == "":
                print(f"\33[KTu: No se escucha lo que has dicho")
                engine.say("No se escucha lo que has dicho")
                engine.runAndWait()
            
            elif "cerrar escritura" in comando:
                engine.say("Cerrando escritura")
                engine.runAndWait()
                break

            else:
                print(f"\33[KTu: {comando}")
                pyautogui.write(comando + " ", interval = 0.1)

        except KeyboardInterrupt:
            print("Ejecución interrumpida por el usuario")
            break
        
        except Exception as e:
            print(f"Error inesperado con la transcripcion: {e}")
            break

def hora_actual(engine = engine):
    tiempo = datetime.now()
    hora = tiempo.hour

    if hora > 12:
        hora -= 12

    engine.say(f"La hora es {hora} con {tiempo.minute}")
    engine.runAndWait()


# ~~~~ COMANDOS DE WINDOWS PERSONALIZADOS

# 1. Abrir Paginas Web

def abrir_youtube():
    os.system("start msedge --inprivate https://www.youtube.com/")

def abrir_fase_bloc():
    os.system("start msedge --inprivate https://www.facebook.com/")

def abrir_copiloto():
    os.system("start msedge --inprivate https://copilot.microsoft.com/")

# 2. Ejecutar acciones

def buscar_en_youtube(
        WIDTH = WIDTH,
        HEIGHT = HEIGHT
):
    pyautogui.click(x = WIDTH/2, y = HEIGHT/2)
    pyautogui.press('tab', presses = 4, interval = 0.25)
    sleep(2)
    escritura(duracion = 7)

