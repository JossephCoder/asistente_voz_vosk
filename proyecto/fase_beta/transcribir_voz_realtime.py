from vosk import Model, KaldiRecognizer, SetLogLevel
import pyaudio

RATE = int(input("Rate: "))
lectura = int(input("Lectura: "))

SetLogLevel(-1)

model = Model("modelos_voz\\vosk-model-small-es-0.42")
recognizer = KaldiRecognizer(model, RATE)

mic = pyaudio.PyAudio()

stream = mic.open(
	format=pyaudio.paInt16,
	channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=8192
)

stream.start_stream()

while True:
	data = stream.read(lectura)
	# if len(data) == 0:
		# break
	if recognizer.AcceptWaveform(data):
		text = recognizer.Result()
		print(text)
		print(text[14:-3])