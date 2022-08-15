'''
Session 4 
Task 2:
    Write script to send an email for your friend when your device is on with its location
'''
from time import sleep
import pyautogui as pag
import requests
import datetime

url = requests.get("https://api.ipify.org/?format=json")
myIP =  str(url.json()['ip']) 
url = requests.get("https://ipinfo.io/"+ myIP +"/geo")
city = url.json()['city']
region = url.json()['region']
country = url.json()['country']
location = url.json()['loc']


pag.press('win')
sleep(1)
pag.press(['c','h','r','o','m','e'])
pag.press('return')
sleep(3)
pag.write('gmail.com', interval=0.1)
pag.press('return')

pointxy = None
while pointxy is None :
    pointxy = pag.locateOnScreen('D:\EmbeddedLinux\Workspace\session4\compose.png')
pag.moveTo(pointxy[0]+50, pointxy[1]+30 , duration=0.5)
pag.click()

pointxy = None
while pointxy is None :
    pointxy = pag.locateOnScreen('D:\EmbeddedLinux\Workspace\session4\msgbox.png', confidence = 0.3)

sleep(1)
pag.write('tuhami.10.8@gmail.com', interval=0.1)
pag.press('tab')
pag.press('tab')
pag.write('Hello pyautogui', interval=0.1)
pag.press('tab')
pag.write('Hi \nThis is an automated message\n')

pag.write(f"Just wanted to register a new log in at { datetime.datetime.now() } \n")
pag.write(f"from \nCity :{city} \nRegion :{region},{country} \nLocation :{location}\n" )
pag.write("Powered up and ready to go ;)\n")

point_send = None
while point_send == None :
    point_send = pag.locateOnScreen('D:\EmbeddedLinux\Workspace\session4\send.png', confidence = 0.7)
pag.moveTo(point_send[0]+30, point_send[1]+30 , duration=0.5)
pag.click()





