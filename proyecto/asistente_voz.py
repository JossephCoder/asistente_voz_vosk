import comandos.comandos_win
from recopilador_objetos import recopilar_funciones
from transcribir_voz import TranscriptorVoz
import pyttsx3
import re

# Objeto Transcriptor encargado de grabar y transcribir
TRANSCRIPTOR = TranscriptorVoz()

# Motor de Voz del Asistente
engine = pyttsx3.init()

class Asistente():
    """Clase Asistente, aqui se crea el objeto Asistente y sus metodos"""

    def __init__(self, activacion = None):
        """
        Iniciamos el objeto con un nombre perzonalizado,
        si no hay ninguno por defecto sera "computadora".

        Tambien inicializamos la recopilacion de la lista
        de comandos que podremos ejecutar.
        
        Argumentos:
        - activacion (str, list, tuple): Nombre o frase para activar el Asistente
        """

        if not activacion:
            self.activacion = [
                "computadora",
                "hey computadora",
                "oye computadora"    
            ]

        elif isinstance(activacion, str):
            self.activacion = [activacion]
            
        elif isinstance(activacion, (list, tuple)):
            self.activacion = list(activacion)

        else:
            raise ValueError(f"ERROR: Dato no válido {activacion}")
        
        # Diccionario de todos los comandos para ejecutar (Windows)
        self.diccionario_comandos = recopilar_funciones(comandos.comandos_win)
    

    def activar(self, comando):

        for nombre in self.activacion:
            if nombre.lower() in comando.lower():
                return nombre.lower()
            
        return False
    

    def ejecutar_comando(self, comando):
    
        if "lista de comandos" in comando:
            print("LISTA DE COMANDOS Y ACCIONES:\n")
            for i in self.diccionario_comandos:
                print(f"- {i}")
            print("- lista de comandos")
            print("- momento de descansar")
            print("\n")
            return True
        
        elif "momento de descansar" in comando:
            print("Adios, cuidate mucho.")
            engine.say("Adios, cuidate mucho.")
            engine.runAndWait()
            return False

        for i in self.diccionario_comandos:

            if i in comando:
                try:
                    engine.say(i)
                    engine.runAndWait()
                    self.diccionario_comandos[i]()

                except:
                    print("Hubo un error con la ejecucion")
                    engine.say("Hubo un error con la ejecucion")
                    engine.runAndWait()

                finally:
                    return True

        else:
            engine.say("Lo siento, no te puedo ayudar con eso.")
            engine.runAndWait()
            return True

    
    def escuchar_comando(self, mic = None):

        try:
            comando = TRANSCRIPTOR.transcribir_voz(duracion = 7, microfono = mic)
              
            if comando is None:
                raise ValueError("Comando reconocido es 'None'\n")

            elif comando == "":
                print(f"\33[KTu: Silencio...")
                return ""

            else:
                print(f"\33[KTu: {comando}")
                return comando
  
        except Exception as e:
            print(f"Ha habido un problema con la transcripcion\n{e}")

    
    def start(self, mic = None):

        engine.say("Hola, buen día. Soy tu compañero virtual y estoy listo para ayudarte")
        engine.runAndWait()

        while True:
            try:
                # Transcribo voz a texto
                comando = self.escuchar_comando()

                # Verifico si estoy llamando a "computadora"
                encender = self.activar(comando)

                # Si llamamos a la "computadora" continuo sino no 
                if encender:
                    # Quito "computadora" del texto transcrito
                    # para verificar que no haya dicho solo "computadora"
                    comando = re.sub(encender, "", comando, count = 1).strip()
                    
                    # Si el comando tiene mas palabras continuo
                    if comando:
                        # Verifico si existe el comando y si es que se puede ejecutar
                        if not self.ejecutar_comando(comando):
                            break
            
            except KeyboardInterrupt:
                print("Ejecución interrumpida por el usuario")
                break
            
            except Exception as e:
                print(f"Error inesperado: {e}")
                break


asistente = Asistente()
asistente.start()
