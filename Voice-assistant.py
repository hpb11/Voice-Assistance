import speech_recognition as sr
import sys
import os
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import wolframalpha 
from datetime import date

try:
    app=wolframalpha.Client("Q43K8Q-EX4RLJQY79")            
except Exception:
    print("Some feature are not working offline")

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()

def run_mini_alexa():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('\n')
        print("Start Speaking!!")
        engine_talk('listening.. ')
        recordedaudio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(recordedaudio, language='en-in')
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print('you said'+command)
        else:
            print('you said : '+command)
        if 'hello' in command:
            print('hello how can i help you ?')
            engine_talk('hello, how can i help you ?')

        elif 'who are you' in command:
            print('I am just like mini alexa-your personal virtual voice assistant')
            engine_talk('I am just like mini alexa-your personal virtual voice assistant')

        elif 'what can you do' in command:
            print('''i can do many small tasks like ..
            Open microsoft applications like word, power-point,excel,onenote,vs code\n 
            play songs or videos on youtube\n
            tell you a joke mostly related to computer science field\n
            search about specific person or thing on wikipedia\n
            tell you current date and time,can find your location\n
            locate any destination on map\n
            Calculate any type of integration / differentiation /  mathamatical calculation\n
            open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google\n
            You can give me commands,How may i help you ?''')
            engine_talk('''i can do many small tasks like ..Open microsoft applications like word, power-point,excel,onenote,vs code,play songs or videos on youtube , tell you a joke mostly related to computer science field, search about specific person or thing on wikipedia, tell you current date and time,can find your location, locate any destination on map,Calculate any type of integration / differentiation /  mathamatical calculation,open different websites like instagram, youtube,gmail, git hub, stack overflow and searches on google.You can give me commands,How may i help you ?''')

        elif 'who made you' in command or 'created by whom' in command:
            print('I have been created by Aditi,Devangi and Hetvi as a part of PSC innovative assignment.')
            engine_talk('I have been created by Aditi,Devangi and Hetvi as a part of PSC innovative assignment.')	
        
        elif 'excel' in command or 'open microsoft excel' in command:
            print('opening excel...')
            engine_talk('opening excel...')
            os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"')

        elif "word" in command or "open microsoft word" in command:
            print('opening word...')
            engine_talk('opening word...')
            os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"')
        
        elif "powerpoint" in command or "open microsoft powerpoint " in command:
            print('opening power-point...')
            engine_talk('opening power-point...')
            os.startfile('"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"')
        
        elif "Onenote" in command or "1 note" in command or "open onenote" in command:
            print('opening onenote...')
            engine_talk('opening onenote...')
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneNote.lnk")
        
        elif "vs code" in command or "open visual studio code" in command:
            print('opening vs code..happy coding...')
            engine_talk('opening vs code.happy coding...')
            os.startfile('"C:\\Users\\ADITI\\Desktop\Visual Studio Code.lnk"')

        elif 'play' in command:
            song = command.replace('play', '')
            print('Playing' + song)
            engine_talk('Playing' + song)
            pywhatkit.playonyt(song)


        elif 'date and time' in command:
            today = date.today()
            time = datetime.datetime.now().strftime('%I:%M %p')
# Textual month, day and year
            d2 = today.strftime("%B %d, %Y")
            print("Today's Date is ", d2, 'Current time is', time)
            engine_talk('Today is : ' + d2)
            engine_talk('and current time is ' + time)
        
        elif 'tell me about' in command:
            name = command.replace('tell me about', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'wikipedia' in command:
            name = command.replace('wikipedia', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'what is' in command:
            name = command.replace('what is ', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'who is ' in command:
            name = command.replace('who is', '')
            info = wikipedia.summary(name, 1)
            print(info)
            engine_talk(info)

        elif 'what is ' in command:
            search = 'https://www.google.com/search?q='+command
            print(' Here is what i found on the internet..')
            engine_talk('searching... Here is what i found on the internet..')
            webbrowser.open(search)

        elif 'joke' in command:
            _joke = pyjokes.get_joke()
            print(_joke)
            engine_talk(_joke)

        elif 'search' in command:
            search = 'https://www.google.com/search?q='+command
            engine_talk('searching... ')
            webbrowser.open(search)

        elif "my location" in command:
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            engine_talk("You must be somewhere near here, as per Google maps")

        elif 'locate ' in command or 'location of' in command or 'where is' in command:
            engine_talk('locating ...')
            loc = command.replace('locate', '')
            if 'on map' in loc:
                loc = loc.replace('on map', ' ')
            url = 'https://google.nl/maps/place/'+loc+'/&amp;'
            webbrowser.get().open(url)
            print('Here is the location of '+loc)
            engine_talk('Here is the location of '+loc)

        elif 'open google' in command:
            print('opening google ...')
            engine_talk('opening google..')
            webbrowser.open_new('https://www.google.co.in/')

        elif 'gmail' in command:
            print('opening gmail ...')
            engine_talk('opening gmail..')
            webbrowser.open_new('https://mail.google.com/')

        elif 'open youtube' in command:
           print('opening you tube ...')
           engine_talk('opening you tube..')
           webbrowser.open_new('https://www.youtube.com/')

        elif 'open instagram' in command:
          print('opening instagram ...')
          engine_talk('opening insta gram...')
          webbrowser.open_new('https://www.instagram.com/')

        elif 'open stack overflow' in command:
          print('opening stackoverflow ...')
          engine_talk('opening stack overflow...')
          webbrowser.open_new('https://stackoverflow.com/')

        elif 'open github' in command:
          print('opening git hub ...')
          engine_talk('opening git hub...')
          webbrowser.open_new('https://github.com/')
        
        elif 'calculate ' in command:
          try:
              res=app.query(command)
              print(next(res.results).text)
              engine_talk(next(res.results).text)
          except Exception:
                print("Some feature are not working offline")
         
        elif 'bye' in command or 'stop' in command or 'exit' in command:
             print('good bye, Thank you ,have a nice day !')
             engine_talk('good bye,Thank you, have a nice day !')
             sys.exit()

        elif 'thank you' in command:
            print("you are most welcome!")
            engine_talk('you are most welcome!')
    
        else:
           print(' I have searched on internet and Here is what i found..')
           engine_talk(' I have searched on internet and Here is what i found..')
           search = 'https://www.google.com/search?q='+command
           webbrowser.open(search)

    except Exception as exc:
        print(exc)

print('Setting the environment right...Clearing background noise...Please wait')
engine_talk('Setting the environment right...Clearing background noise...Please wait')

print('\n')

print("hello, i am your personal voice assistant just like mini alexa, how can i help you ?")
engine_talk("hello, i am your personal voice assistant just like mini alexa, how can i help you ?")

while True:
    run_mini_alexa()


 