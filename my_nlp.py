# import pyttsx3

# # Initialize the engine
# engine = pyttsx3.init()

# # Text to convert into speech
# text = "Hello! Welcome to kanduku:"

# # Speak the text
# engine.say(text)

# # Run the speech engine
# engine.runAndWait()
# print("hello")







# import speech_recognition as sr

# # Create recognizer object
# recognizer = sr.Recognizer()

# # Use microphone as input
# with sr.Microphone() as source:
#     print("Speak something...")
#     recognizer.adjust_for_ambient_noise(source)
#     audio = recognizer.listen(source)

# try:
#     # Convert speech to text
#     text = recognizer.recognize_google(audio)
#     print("You said:", text)

# except sr.UnknownValueError:
#     print("Sorry, I could not understand the audio.")

# except sr.RequestError:
#     print("Could not connect to Google Speech Recognition service.")