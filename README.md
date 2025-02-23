# Asistente Virtual con Vosk

Este es un asistente virtual que utiliza un modelo de transcripción de voz a texto basado en **Vosk**. El asistente te ayudará a realizar diversas tareas como ejecutar comandos, abrir programas, dictado y más. El funcionamiento es completamente offline, lo que significa que no necesitas una conexión a Internet (excepto para la navegación web).

## Requisitos

Para ejecutar este proyecto, necesitarás:

- **Python 3.10 o superior**
- **Virtualenv** (herramienta para crear entornos virtuales en Python)

## Instalación

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone <URL del repositorio>
    ```

2. Después de descargar el repositorio, crea un entorno virtual dentro del repositorio con el siguiente comando:
    ```bash
    virtualenv env
    ```

3. Activa el entorno virtual:
    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```

4. Con el entorno activado, instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución

Dentro del repositorio encontrarás un archivo `.bat` llamado `asistente_vosk.bat`. Al ejecutar este archivo, el entorno virtual se activará automáticamente y se ejecutará el archivo `asistente.py`, que iniciará el asistente y comenzará a escuchar tu voz, listo para ejecutar comandos.

Si prefieres ejecutar el programa desde cualquier ruta, puedes agregar el repositorio a las variables de entorno. Además, si quieres que el asistente se ejecute automáticamente cada vez que inicies tu computadora, puedes agregarlo al Programador de Tareas de Windows.

## Lista de Comandos

Los comandos disponibles están definidos en el archivo `comandos_win.py`, ubicado en la carpeta `comandos`. Para obtener una lista completa de los comandos, simplemente di `"lista de comandos"` y el asistente te mostrará todos los comandos disponibles.

Si los comandos predeterminados no se ajustan a tus necesidades, puedes modificarlos o agregar nuevos comandos en el archivo mencionado.

### Ejemplo de uso:
- Si deseas abrir el Bloc de notas, solo di: 
    > "Computadora, por favor, abrir Bloc de notas"
  
## Uso

Cuando inicies el programa, este te saludará y te indicará que está listo para escuchar. En la terminal, verás los mensajes que indican el estado actual del asistente y las acciones que está realizando. Puedes empezar a dictar tus comandos y el asistente ejecutará las acciones correspondientes.
Para obtener una mejor precisión en la transcripción de voz, asegúrate de hablar con claridad y a un volumen adecuado. Es recomendable que utilices frases completas para mejorar la detección de comandos.

> [!NOTE]
> ### Nota importante:
> El Asistente Virtual responde ante un nombre en específico para ejecutar comandos, por defecto es **`"computadora"`** (aunque puedes cambiarlo en el `asistente_voz.py` en el objeto asistente de la clase Asistente), si no se menciona su nombre omitira los mensajes, esto se hace para evitar el consumo de recursos al intentar ejecutar todo lo que escucha.

## Consideraciones Importantes

Este código es un ejemplo y debe adaptarse a tus necesidades y requisitos específicos. Es posible que debas modificar algunos fragmentos del código para que funcione en tu entorno o sistema operativo particular. Además, asegúrate de manejar adecuadamente los errores y excepciones.

## Estructura del Proyecto

A continuación, se muestra la estructura de carpetas del proyecto:

- `modelos_voz/`: Aquí podrás descargar los modelos de Vosk necesarios para el funcionamiento del asistente. Puedes obtenerlos desde [la página oficial de Vosk](https://alphacephei.com/vosk/models).
  - El modelo por defecto es **SMALL ESPAÑOL**. Ten en cuenta que cuanto más pesado sea el modelo, más recursos y tiempo requerirá, pero tendrá una mejor precisión en la transcripción.

- `proyecto/`: Carpeta principal que contiene el código del programa.

- `audio_py/`: Carpeta que contiene los módulos relacionados con la grabación, reproducción y transcripción de audio.

- `comandos/`: Aquí se encuentra el módulo que gestiona la lista de comandos y acciones que el asistente puede ejecutar (por ahora solo soporta Windows).

- `fase_beta/`: Código experimental que puedes ignorar, ya que está en fase de pruebas.

### Archivos importantes:

- `modelos.py`: Este archivo carga los modelos de voz y contiene un diccionario con las rutas de los modelos. Puedes cambiar la ruta del modelo aquí si deseas utilizar otro modelo.
  
- `transcribir_voz.py`: Contiene la clase `TranscriptorVoz`, que se encarga de grabar, transcribir y devolver el texto correspondiente al audio.

- `asistente_voz.py`: Este archivo es el principal encargado de levantar todo el programa, ya que aqui se llama a todos los modulos antes mencionados y es el que mantiene abierto el programa y la escucha de los comandos.

- `recopilador_objetos.py`: Este archivo contiene una función que extrae automáticamente las funciones y comandos de los módulos, y las guarda en un diccionario.
Se usa para extraer las funciones del modulo `comandos_win.py`.

## Contribuciones

Este código está disponible para que cualquiera pueda utilizarlo, modificarlo y mejorarlo. Si deseas contribuir con mejoras, correcciones o nuevas funcionalidades, puedes enviar tus propuestas a través de un *pull request* en GitHub.

## Licencia

Este proyecto se encuentra bajo la licencia **Apache License 2.0**. Puedes consultar la licencia completa [aquí](https://opensource.org/licenses/Apache-2.0).

## Autor

Este proyecto fue creado por **Josseph Coder** el dueño de este perfil de **GitHub**.

El modelo de transcripción de voz utilizado en este proyecto proviene de **Vosk**, que está bajo la licencia **Apache License 2.0**.
