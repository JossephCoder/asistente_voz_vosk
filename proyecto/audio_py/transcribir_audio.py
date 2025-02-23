"""
Este modulo sirve para transcribir audios.wav grabados a texto.

La transcripción se realiza con el Modelo de IA Vosk.

Pero para evitar sobrecarga, el Modelo Vosk solo debe ser cargado
una única vez en el archivo.py donde lo va a utilizar.
"""

import wave
import json
from io import BytesIO
from vosk import KaldiRecognizer


def transcribir_audio(audio_data, model):
    """
    Funcion que transcribe el audio y devuelve el texto.
    
    Recibe dos parametros:
    - audio_data: recibe el AUDIO.WAV a transcribir
    - model: recibe el MODELO a utilizar, ya cargado previamente

    La carga del modelo la realiza usted, en el archivo.py
    donde va a utilizar la funcion, para que la funcion
    reciba el modelo listo para transcribir y evitar la sobrecarga.
    """

    # ~~~~ Abro el audio
    try:
        with wave.open(audio_data, "rb") as wf:

            reconocedor = KaldiRecognizer(model, wf.getframerate)

            # ~~~~ Obtengo por palabras
            reconocedor.SetWords(True)

            # ~~~~ Rebobino el audio si es BytesIO (En la RAM)
            if isinstance(audio_data, BytesIO):
                audio_data.seek(0)
            else:
                pass

            print(f"Transcribiendo el audio con Vosk\n")

            # ~~~~ Transcribiendo a texto
            while True:
                data = wf.readframes(4000)

                if len(data) == 0:
                    break

                if reconocedor.AcceptWaveform(data):
                    resultado = json.loads(reconocedor.Result())

        if isinstance(audio_data, BytesIO):
            audio_data.close()
        else:
            pass

        print(f"Fin de la Transcripcion\n")

        resultado = json.loads(reconocedor.FinalResult())
        texto = resultado.get('text')
        
        # ~~~~ Retornamos el texto
        return texto

    except Exception as e:
        print(f"No se puede Transcribir el Audio ¡Error!\n{e}")
        return None
