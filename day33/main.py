import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 33.351358 # Your latitude
MY_LONG = 44.413769 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
def is_iss_overhead():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    return False

def send_mail(message):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("deviddevid287@gmail.com","kuvw hjak qwgt waxr")
        server.sendmail("deviddevid287@gmail.com","deviddevid287@gmail.com",message)
        server.quit()

def is_dark():
    time_now = int(datetime.now().hour)
    if time_now < sunrise or time_now > sunset:
        return True
    return False


while True:
    time.sleep(60)
    if (is_iss_overhead and is_dark):
        send_mail("look up iss is above you ")



