from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

import pywhatkit as pk

import speech_recognition as sr


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "C:\\Users\\dipak gaikwad\Desktop\\Full stack data science\\chromedriver.exe"

service = Service(executable_path=r"C:\Users\dipak gaikwad\Desktop\Full stack data science\Projects\jarvis\chromedriver-win64\chromedriver.exe")


driver = webdriver.Chrome(service= service,options=chrome_options)

driver.maximize_window()


website = r"https://ttsmp3.com/text-to-speech/British%20English/"
driver.get(website)
ButtonSelection = Select(driver.find_element(by = By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('British English / Brian')


def speak(voice):
    lengthoftext= len(str(voice))
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"jarvis:{text}.")
        print("")
        Data = str(text)
        xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value ='//*[@id="vorlesenbutton"]').click()
        driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()
        
        if lengthoftext >=30 :
            sleep(4)
            
        elif lengthoftext >= 60:
            sleep(6)
            
        elif lengthoftext >=55:
            sleep(8)
            
        elif lengthoftext >= 70:
            sleep(10)
            
        elif lengthoftext >= 100:
            sleep(13)
            
        else:
            sleep(2)

'''**********************************************************'''

listening = sr.Recognizer()
def hear():
    with sr.Microphone() as mic:
        print('listening.........')
        audio = listening.listen(mic)
        
    try:
        print('recognizing......')
        voice = listening.recognize_google(audio)
        print(f'user said:{voice}\n')
    except Exception as e:
        speak('i cant hear you')
        return "none"
    return voice



def run():
    voice = hear()
    if 'play' in voice:
        song = voice.replace('play','')
        speak('playing'+song)
        pk.playonyt('playing'+song)
        
