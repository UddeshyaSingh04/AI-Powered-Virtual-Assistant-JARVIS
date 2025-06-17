import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import openai as OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d47a439f126904674b7bb63d0deb4e278"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="s4k-proj-cFtIvUj3nd8sITcSCdUmZ3HrwiVSeYOWr1lbjZXXJE01AwBe4DMp2G-KVNWUobxAvpav0a5DK-T3BlbkFJtGrgQ8iM7Dgr6KDj8N01VRIyh8wxxcEfwUC-QVaMtnIGZkCMofs8cQaFwtZqqr34nzf7lkBloA",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Or any other model you want to use
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general task like Alexa and google cloud"},
        {"role": "user", "content": command }
    ]
    )

# Step 3: Print the reply
    return completion.choices[0].message.content

# basically this function(aiProcess) will not run because, this OpenAI API is paid 


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
 
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}") #its a normal news api link just i editit and write  in unique way
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            #Exact the articles
            articles = data.get("articles", [])

            #print the headlines
            for article in articles:
                speak(article["title"])

    else:
        # let OpenAI handle the report
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listen for a the wake word "Jarvis"
        # obtain audio from the microphone

        r = sr.Recognizer()
        

        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=7, phrase_time_limit=7)
            word = recognizer.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya, how can I help you")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activate...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
