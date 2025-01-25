import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak something...")

        # Adjust for ambient noise to improve accuracy
        recognizer.adjust_for_ambient_noise(source)

        try:
            # Listen to the input
            audio = recognizer.listen(source)

            # Convert speech to text
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Call the function
speech_to_text()
