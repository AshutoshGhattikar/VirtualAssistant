import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import wolframalpha
import datetime
import random
import os
import webbrowser
import subprocess as sp
import sys


#initializing the essential methods for using microphone
listener = sr.Recognizer()
engine = pt.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',rate-50)


#initializing the search engine
app_id = 'RLX34Q-AYKURQWQJJ' #unique key for authentication,registering account in wolframalpha's website is must
client = wolframalpha.Client(app_id)


#function for text to audio
def talk(text):
    engine.say(text)
    engine.runAndWait()

#function for listening user's voice
def hear():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice =  listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        talk('')
        return 'none'


#unction to greet user with username
def greet_user():
    print('say your name...')
    talk('what is your name?')
    print('hearing...')
    name = hear()
    if name != 'none':
        print('got your name..')
        greet_name = (f'Hello {name},my name is meow and i am your assistant, what would you like me to do?')
        print(greet_name)#r
        talk(greet_name)#r
    else:
        talk('okay it seems like you are a silent one')
        name = 'stranger'
        greet_name = (f'Hi {name},my name is meow and i am your virtual assistant, what would you like me to do?')
        print(greet_name)#r
        talk(greet_name)#r


#function for checking the wake word
def check_wake_word(word):
    wake_word_list = ['hello meow', 'hi meow', 'hey meow','ok meow','meow']

    for phrase in wake_word_list:
        if phrase in word:
            return True
    return False


#function for the running the assistant, using all the above functions
def run_assistant():
    command1 = hear()
    print(command1)



    if 'play' in command1:
        song = command1.replace('play','')
        talk('ok playing'+ song +' in youtube')
        pw.playonyt(song)



    elif 'open google' in command1:
        webbrowser.open('google.com')
        talk('google is opened')



    elif 'open gmail' in command1:
        webbrowser.open('https://mail.google.com/')
        talk('your gmail is opened')



    elif 'open spotify' in command1:
        sp.Popen('Spotify.exe')



    elif 'who' or 'what' or 'when' or 'why' or 'how' or 'where' in command1:  #head_ache
        search_query = command1
        res_query = client.query(search_query)
        ans = next(res_query.results).text
        talk(ans)
        talk('Do you want to know more about it?')
        subcommand1 = hear()
        url = 'https://www.google.com/search?q='
        print(subcommand1)
        if 'yes' or 'ya' in subcommand1:
            wb.open(url=url+search_query)
        elif 'no' or 'nope' or 'nah' in subcommand1:
            talk('okay')

    else:
        talk("Say agian please")


while True:
    command = hear()
    print(command)
    if (check_wake_word(command) == True):
        talk('Hey there')
        greet_user()
        run_assistant()

