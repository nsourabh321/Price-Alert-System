import requests
import time
from bs4 import BeautifulSoup as BS
from smtplib import SMTP
URL= "https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_2?crid=39BJ0Z0BJ3XIU&dib=eyJ2IjoiMSJ9.0BpMlBBf3v-KzGqQg2MoJmtdRJJ6_-xuUaANnfQU8iJe0rc7rpDdcntzA1LNVTrrxaXWejs7V3Dgkc4_tS5uygwcMFyukiHvI5eCjrMyFlU6AoqEcfQQFTSsFnpcvot-0e7pRnLjPczQ5JGgoPSkovO4KKLLtE2T9Chfd6LY44ICLU5k9GPrYEB9kLMbwskjMlp46oxS1KCkV4lCV-LMUZ0iVV_LykTUgxswErhp6eg.4y6lTW8ScNNGZLAsExOxys-0rdIdIp3IWozMIOeLVLs&dib_tag=se&keywords=ps5&qid=1718175740&sprefix=ps%2Caps%2C228&sr=8-2"

#funciton for extracting price from the webpage
def extract_price():
         headers = {
             "User-Agent" : "Your user agent"
         }
         response = requests.get(URL,headers=headers)
         if response.status_code != 200:
             print(f"Failed to retrieve webpage. status code:{response.status_code}")
             return None
         soup=BS(response.content,"html.parser")
        #  print(soup)
         price_span=soup.find("span",attrs={"class" : "a-price-whole"}) 
         print(price_span)
         if not price_span:
             print("price element not found on the page.")
             return None
         try:
             price = float(price_span.text.replace(",","").replace(".",""))
             return price
         except ValueError as e:
             print(f"error converting price to float {e}")
             return None

SMTP_SERVER="smtp.gmail.com" 
PORT=587
Email_Id="your email address" 
Password="your-email=password" 
def notification():
    try:
        server = SMTP(SMTP_SERVER, PORT)
        server.starttls()
        server.login(Email_Id, Password)
        
        subject = "BUY NOW!!!"
        body = f"Price has fallen. Go buy it now\n{URL}"
        msg= f"subject:{subject}\n\n{body}"
        server.send_message(Email_Id,'your-email-address',msg)
        server.quit()
        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

#change to desired price 
Affordable_price=100   
while True:
     extraceted_price = extract_price()
     if extraceted_price == None:
         print("extraced price is None")
         break
     if extraceted_price<=Affordable_price:
         notification()
     time.sleep(30)