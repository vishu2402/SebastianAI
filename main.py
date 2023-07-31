import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai
from config import apikey
import datetime
import random

chatStr = ""

def chat(query):
    openai.api_key = apikey

    # Define a single message using the user input
    messages = [
        {"role": "user", "content": query}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response and 'choices' in response and response['choices']:
        generated_text = response['choices'][0]['message']['content']

        # Save the AI's response in a file inside the "Openai" folder
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # Extract the prompt from the user's query
        prompt = query.lower()
        filename = f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"

        with open(filename, "w") as f:
            f.write(generated_text)

        # Speak the AI's response
        say(generated_text)

        return generated_text
    else:
        print("Failed to get a valid response.")
        return None

def ai(messages):
    openai.api_key = apikey

    # Your user input as a string
    user_input = messages

    # Define a single message using the user input
    messages = [
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=messages,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if response and 'choices' in response and response['choices']:
        generated_text = response['choices'][0]['message']['content']
        print(generated_text)

        # Save the AI's response in a file inside the "Openai" folder
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # Extract the prompt from the user_input
        prompt = user_input.lower()
        filename = f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt"

        with open(filename, "w") as f:
            f.write(generated_text)

        return generated_text
    else:
        print("Failed to get a valid response.")
        return None

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Sebastian"

if __name__ == '__main__':
    print('PyCharm')
    say("Sebastian AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = r'C:\Users\kumar\Downloads\downfall-21371.mp3'
            os.startfile(musicPath)

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} bajke {min} minutes")

        elif "open brave".lower() in query.lower():
            # Use raw string to avoid escape character issues
            brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            os.startfile(brave_path)

        elif "open batman".lower() in query.lower():
            # Use raw string to avoid escape character issues or escape backslashes
            batman_path = r"C:\Program Files (x86)\Batman - Arkham Asylum\Binaries\BmLauncher.exe"
            os.startfile(batman_path)

        elif "Using artificial intelligence".lower() in query.lower():
            response_text = ai(messages=query)
            if response_text:
                say(response_text)

        elif "Sebastian Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)
