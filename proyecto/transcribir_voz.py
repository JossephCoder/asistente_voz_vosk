"""
Módulo creado netamente para el Asistente de voz,
que trabaja con un Modelo IA de VOSK ya definido
(aunque se puede cambiar) y siempre va a grabar y
trabajar con una frecuencia de muestreo de 44100 hz
(aunque se puede cambiar) ya que los datos de los audios
siempre van a ser los mismos y ahorramos recursos
"""

import wave
import json
from modelos import MODEL
from vosk import KaldiRecognizer
from audio_py.grabar_voz import grabar_voz, guardar_voz_ram

class TranscriptorVoz():

    # FRECUENCIA DE MUESTREO PARA GRABAR Y TRANSCRIBIR
    RATE = 44100
    """
    FRECUENCIA DE MUESTREO establecida en 44100 hz
    para grabar todos los audios a esa frecuencia
    """

    RECONOCEDOR = KaldiRecognizer(MODEL, RATE)
    """
    RECONOCEDOR es un objeto de la clase vosk.KaldiRecognizer, cuya funcion es
    recibir el MODELO con el que hara las transcripciones y la
    FRECUENCIA DE MUESTREO de los audios que va a recibir.
    (En este caso se establece un FRAMERATE fijo en 44100 hz ya que esa es la
    FRECUENCIA con la que todos los audios seran grabados y ahorramos recursos)
    """

    def __init__(self): pass

    def transcribir_voz(self, duracion, microfono = None):
        """
        Metodo encargado de escuchar nuestra voz y transcribirla a texto.
        Netamente creado para el Asistente de Voz.
        La carga del modelo se realiza apenas se importa el modulo.

        Parametros:
        - duracion: Establece la duracion (segundos) de la grabacion
        - microfono: Establece el microfono que se usara para grabar, sino se especifica se utilizara el microfono por defecto
        """

        # ~~~~ GRABAMOS EL AUDIO A 44100 HZ Y POR 5 SEG
        try:
            frames = grabar_voz(
                RATE = TranscriptorVoz.RATE,
                MICROFONO = microfono,
                RECORD_SECONDS = duracion
            )
            audio_data = guardar_voz_ram(frames)
            audio_data.seek(0)  # Rebobinador

        except Exception as e:
            print(f"No se puede Grabar ¡Error!\n{e}")
            return None

        # ~~~~ ABRO EL AUDIO GRABADO
        try:
            with wave.open(audio_data, "rb") as wf:
                
                print("\33[KTranscribiendo el audio...", end = "\r", flush = True)

                # ~~~~ TRANSCRIBIENDO A TEXTO
                while True:
                    
                    # ~~~~ LEEMOS EL AUDIO POR BLOQUES DE 4000 FRAMES
                    data = wf.readframes(4000)

                    # ~~~~ CUANDO TERMINAMOS DE LEER ROMPEMOS
                    if len(data) == 0:
                        break

                    # ~~~~ PROCESAMOS CADA BLOQUE CON EL RECONOCEDOR
                    if TranscriptorVoz.RECONOCEDOR.AcceptWaveform(data):
                        resultado = json.loads(TranscriptorVoz.RECONOCEDOR.Result())

            # ~~~~ AL FINALIZAR CERRAMOS EL AUDIO RAM (BYTESIO)
            audio_data.close()
            
            print("\33[KFin de la Transcripción.", end = "\r", flush = True)

            # ~~~~ OBTENEMOS EL RESULTADO FINAL DE LA TRANSCRIPCION
            resultado = json.loads(TranscriptorVoz.RECONOCEDOR.FinalResult())
            texto = resultado.get('text')

            # ~~~~ RETORNAMOS EL TEXTO TRANSCRITO
            return texto
        
        except Exception as e:
            print(f"No se puede Transcribir el Audio ¡Error!\n{e}")
            return None
