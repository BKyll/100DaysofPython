import requests
import datetime as dt
import smtplib
import time

MY_LAT = 47.764127
MY_LNG = -122.199550
LOCAL_UTC_OFFSET = -8
GMAIL = "emptypork@gmail.com"
YAHOO = "redshift@myyahoo.com"
PASSWORD = "okamuchajpxxfcxv"
NOW = dt.datetime.now()


def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


def iss_is_in_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5) and (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    local_sunrise = utc_to_local(sunrise)
    local_sunset = utc_to_local(sunset)

    time_now = dt.datetime.now().hour

    if local_sunset <= time_now <= local_sunrise:
        return True


while True:
    if iss_is_in_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=GMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=GMAIL,
                to_addrs=YAHOO,
                msg=f"Subject:The ISS is Overhead!\n\n"
                    f"Time to go outside and look at some specks!🛰️"
                )
    time.sleep(60)
