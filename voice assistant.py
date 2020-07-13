#pip install SpeechRecognition
#pip install pyaudio
#pip install gTTS
#pip install playsound
#pip install wikipedia
import speech_recognition as sr
import webbrowser
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import playsound
import os

warnings.filterwarnings('ignore')


def input_audio():
    r=sr.Recognizer()#recognizer object
    #mic
    with sr.Microphone() as source:
        print("say something...")
        audio=r.listen(source)

    #google speech recognition
    data=''
    data=r.recognize_google(audio)
    try:
        print("you said :" +data)
    except sr.UnknownValueError:
        print("sorry! i can't understand.")
    except sr.RequestError as e:
        print("service error,check your connection.")
    return data

def output_audio(text):
    #convert text to speech
    obj=gTTS(text=text,lang='en')
    #save converted file
    obj.save("output.mp3")
    #play output
    playsound.playsound('output.mp3')
    os.remove('output.mp3')

#function to get the current date
def current_date():
    now=datetime.datetime.now()
    weekday=calendar.day_name[now.weekday()]#e.g friday
    monthnum=now.month
    daynum=now.day
    month_names=['january','february','march','april','may','june','july','august','september','october'
                 ,'november','december']
    date_names=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th'
                ,'19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    return 'today is '+date_names[daynum-1]+' '+month_names[monthnum-1]+" "+weekday

def time():
    hour=datetime.datetime.now().hour
    mins = datetime.datetime.now().minute
    return "current time is :" + str(hour) +" "+ str(mins)

def getname(text):
    wordlist=text.split()#splitting sentence intpo list of words
    for i in range(0,len(wordlist)):
        if wordlist[i].lower()=="who" and wordlist[i+1].lower()=='is':
            return wordlist[i+2] +' '+ wordlist[i+3]

def joke():
    jokes=['A sports store. Customer: Do you have jogging shorts? Me: We have running shorts. How fast were you planning on going?'
           ,'You know why you never see elephants hiding up in trees? Because they’re really good at it'
           ,'What is red and smells like blue paint?Red paint','As a scarecrow, people say I’m outstanding in my field.But hay, it’s in my jeans'
           ,'What is the resemblance between a green apple and a red apple? They’re both red except for the green one']
    return random.choice(jokes)

def weather():
    import requests, json
    api_key =  "d9bc71681edaecab08a32a57953f748d"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "amritsar"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"] - 273.15
        z = x["weather"]
        weather_description = z[0]["description"]
        return " Temperature in "+ city_name +" is " + str(current_temperature) + "celcius with " + str(weather_description)


def youtube():
    webbrowser.open('https://www.youtube.com/')


while True:
    #record audio and store as a text
    text=input_audio()
    text=text.lower()

    response=''

    if("date" in text):
        response=current_date()
        print(response)
        output_audio(response)

    if ('time' in text):
        response = time()
        print(response)
        output_audio(response)

        # check if user said "who is"
    if('who is' in text):
            person=getname(text)
            response=wikipedia.summary(person,sentences=2)
            print(response)
            output_audio(response)

    if('joke' in text):
            response=joke()
            print(response)
            output_audio(response)

    if ('weather' in text):
            response=weather()
            print(response)
            output_audio(response)

    if ('youtube' in text):
        response = response + "opening youtube , please wait"
        print(response)
        output_audio(response)
        youtube()



