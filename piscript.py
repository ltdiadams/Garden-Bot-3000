# Growbot: post csv file to webapp
# To be run on Raspberry Pi

# Logan DiAdams,
# For PHYS/COMP-3361
# 2019

import requests
import time

# function for posting the values.csv file to form

def upload_it():
    with open("values.csv", "rb") as f:
        s = requests.Session()
        # fetch the CSRF cookie
        r1 = s.get("http://ltdiadams.pythonanywhere.com/upload/")
        assert r1.status_code == 200
        csrf_token = r1.cookies["csrftoken"]
        print("got csrf token", csrf_token)

        # post stored.csv
        r2 = s.post(
            "http://ltdiadams.pythonanywhere.com/upload/",
            data={"csrfmiddlewaretoken": csrf_token},
            files={"file": f},
        )
        print(r2.status_code)

#infinite loop to upload csv every second

while True:
    upload_it()
    time.sleep(1)
