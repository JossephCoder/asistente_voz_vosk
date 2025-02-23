import speech_recognition as sr
import locale

def listar_microfonos():
    """
    Funcion que retorna un diccionario de los microfonos
    que estan aptos para la grabacion de sonido
    """
    microfonos = sr.Microphone.list_working_microphones()
    codificacion_so = locale.getpreferredencoding()

    for clave, valor in microfonos.items():
        # Corregimos la codificacion de caracteres
        microfonos[clave] = valor.encode(codificacion_so).decode('utf-8')
    
    return microfonos

def escoger_microfono():
    """
    Funcion que nos muestra de manera visual la lista de microfonos
    aptos para grabar y que nos pregunta si queremos usar uno en
    especifico para posteriormente retornarlo, si no hay microfonos
    se retorna None
    """

    microfonos = listar_microfonos()

    if len(microfonos) > 1:
        for clave, valor in microfonos.items():
            print(f"[{clave}]: {valor}")

        while True:
            opcion_mic = input("Seleccione un microfono: ")

            try:
                opcion_mic = int(opcion_mic)
            except:
                print("ERROR: Opcion no valida")
                continue

            if opcion_mic not in microfonos:
                print("ERROR: Opcion no se encuentra en la lista")
                continue
            else:
                return opcion_mic
            
    elif len(microfonos) == 1:
        return None

    elif not microfonos:
        raise Exception("ERROR: No se ha detectado ningun microfono")

