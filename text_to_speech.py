import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the voice
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Example usage
if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    text_to_speech(text)
