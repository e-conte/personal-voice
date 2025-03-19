import speech_recognition as sr

def reconocer_voz():
    # Crear un reconocedor de voz
    recognizer = sr.Recognizer()

    # Usar el micrófono como fuente de audio
    with sr.Microphone() as source:
        print("Di algo...")
        # Ajustar el reconocedor para el ruido ambiental
        recognizer.adjust_for_ambient_noise(source)
        # Escuchar la entrada del micrófono
        audio = recognizer.listen(source)

        try:
            # Reconocer el habla usando Google Web Speech API
            texto = recognizer.recognize_google(audio, language="es-ES")
            print("Has dicho: " + texto)
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
        except sr.RequestError as e:
            print(f"Error al solicitar resultados desde el servicio de reconocimiento de voz; {e}")

if __name__ == "__main__":
    reconocer_voz()