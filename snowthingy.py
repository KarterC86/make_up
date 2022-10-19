from bs4 import BeautifulSoup
from requests import get
from win32com.client import Dispatch

state = input("What is your state abbreviations?: ").lower()
url = f"https://www.wunderground.com/weather/us/{state}"
tEmail = input("What email would you like this to send to? ")
soup1 = BeautifulSoup(get(url).text,'html.parser')

def weatherCheck(soup):
    high = soup.find(class_ = "high").text
    low = soup.find(class_ = "low").text
    rain = soup.find(class_ = "amount of rain").text
    snow = soup.find(class_ = "amount of snow").text
    warmer = soup.find(class_ = "how hot is it").text
    weather = [high, low, warmer, rain, snow]
    global state
    sendmsg = f"The weather for {state.title()} is\n"
    sendmsg += f"The high for today is: {weather[0]}\n"
    sendmsg += f"The low for today is: {weather[1]}\n"
    sendmsg += weather[2] + "\n"
    rainIndex = weather[3].index("°")
    snowIndex = weather[4].index("°")
  

def Email():
    mail = Dispatch('outlook.application').CreateItem(0)
    msg = weatherCheck(soup1)
    mail.Subject = f'The Weather Today in {state.upper()}'
    mail.To = tEmail
    mail.body = msg
    mail.Send()
    print(msg)
    print("Sent!")

