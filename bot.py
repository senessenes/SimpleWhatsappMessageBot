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
        print(names)
        print(phone_numbers)

        if df.isnull().values.any():
            raise Exception("Missing Data")
        else:
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
wpbot.get_contacts()
message=input("Type your message...")
country_code=input("Country code of the phone numbers...")
if "+" not in country_code:
    raise Exception("Invalid country code")
else:
    wpbot.bot_message(message,country_code)





