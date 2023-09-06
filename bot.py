"""Whatsapp Bot Project using  "pywhatkit","pandas","pyautogui"
and "Tkinter"(Only for getting the width and height of the screen nothing else)"""
#By Suleyman Enes Gokkaya(github:senessenes)

import pywhatkit
import pandas as pd
import pyautogui
from tkinter import *

class Contact():
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number
    def send_message(self,message,countrycode):
        pywhatkit.sendwhatmsg_instantly(f"{countrycode}{self.phone_number}",f"{message}")

class Bot():
    def __init__(self,file_path):
        self.contacts=[]
        self.file_path=file_path
    def get_contacts(self):
        df=pd.read_excel(self.file_path)
        names=list(df["Names"])
        phone_numbers=list(df["Phone Numbers"])
        if not(len(names)==len(phone_numbers)):
            raise Exception("Missing Data")
        for i in range(0,len(names)):
            self.contacts.append(Contact(names[i],phone_numbers[i]))
    def bot_message(self,message,country_code):
        win = Tk()
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        self.get_contacts()
        for contact in self.contacts:
            contact.send_message(message,country_code)
            pyautogui.moveTo(screen_width * 0.694,screen_height * 0.964)
            pyautogui.click()
            pyautogui.press('enter')



wpbot=Bot("wpbotexcelfile.xlsx")
country_code=input("What is your country code?")
message=input("What is the message you want to send?")
wpbot.bot_message(message,country_code)





