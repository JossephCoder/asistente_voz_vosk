"""
Modulo de Python dedicado al Audio:

- Grabacion
- Guardado (Disco: Permanente - RAM: Temporal)
- Reproducción

Con la ayuda del modulo wave
"""

import wave
import pyaudio
from io import BytesIO
from keyboard import is_pressed

def grabar_voz(
        FORMAT:int = pyaudio.paInt16,
        CHANNELS:int = 1,
        RATE:int = 44100,
        MICROFONO:int = None,
        CHUNK:int = 1024,
        RECORD_SECONDS:int = None
):
    """
    Parámetros de configuración para la grabación de voz:
    - FORMAT = pyaudio.paInt16 --> Tipo de formato de audio (16-bit PCM)
    - CHANNELS = 1 --> Número de canales (mono)
    - RATE = 44100 --> Frecuencia de muestreo (44.1kHz, común en grabaciones)
    - MICROFONO = None --> Microfono con el que se quiere grabar (Por defecto NONE)
    - CHUNK = 1024 --> Tamaño de buffer (número de frames por cada lectura)
    - RECORD_SECONDS = None --> Tiempo de Grabacion (Indefinido por defecto)
    """

    # Instancio PyAudio
    py_audio = pyaudio.PyAudio()

    # Abrir el stream para grabación con microfono
    try:
        stream = py_audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            input_device_index = MICROFONO,
            frames_per_buffer=CHUNK
        )
    except:
        print("ERROR: No se puede realizar la Grabacion")

    # Array/Lista que almacena el sonido
    frames = []

    print("\33[KEscuchando Voz...", end = "\r", flush = True)
    
    # Grabar indefinidamente
    if RECORD_SECONDS == None:
        while True:
            data = stream.read(CHUNK)  # Lee un chunk de datos (1000 frames)
            frames.append(data)        # Agrega el chunk a la lista de frames
            if is_pressed('q'):
                break

    # Grabar durante un limite de segundos
    else:
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

    print("\33[KGrabación terminada.", end = "\r", flush = True)

    # Detener y cerrar el stream
    stream.stop_stream()
    stream.close()
    py_audio.terminate()

    return frames

def guardar_voz_ram(frames:list):

    # Asigno un nombre al audio que se almacenara en ram
    name_audio = BytesIO()

    # Guardar el audio grabado en un archivo en memoria (BytesIO)
    with wave.open(name_audio, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))

    # Reproducir el audio desde BytesIO usando PyAudio
    name_audio.seek(0)  # Volver al inicio del archivo en memoria

    return name_audio

def guardar_voz_disk(name_audio:str, frames:list):

    # Guardar el audio grabado en un archivo en memoria (BytesIO)
    with wave.open(name_audio + ".wav", 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
    
    print(f"Audio guardado como '{name_audio}.wav'")

    return name_audio + ".wav"

def reproducir_voz(name_audio):

    # Instancio PyAudio
    py_audio = pyaudio.PyAudio()

    # Abro el audio
    with wave.open(name_audio, 'rb') as wf:

        # Crear un stream de PyAudio para reproducir el audio
        stream = py_audio.open(
            format=pyaudio.paInt16,
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        # Leer los datos y reproducir el audio
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # Detener y cerrar el stream
        stream.stop_stream()
        stream.close()
        py_audio.terminate()


