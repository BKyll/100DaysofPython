import requests
from datetime import datetime

MY_LAT = 47.764127
MY_LNG = -122.199550
LOCAL_UTC_OFFSET = -8


# # ISS API
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
#
#
# print(iss_position)

# Sunset/Sunrise API
def utc_to_local(utc_hour):
    utc_hour += LOCAL_UTC_OFFSET
    if LOCAL_UTC_OFFSET > 0:
        if utc_hour > 23:
            utc_hour -= 24
    elif LOCAL_UTC_OFFSET < 0:
        if utc_hour < 0:
            utc_hour += 24
    return utc_hour


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
print(f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}")

data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

local_sunrise = utc_to_local(sunrise)
local_sunset = utc_to_local(sunset)

print(local_sunrise)
print(local_sunset)

time_now = datetime.now()
print(time_now.hour)
