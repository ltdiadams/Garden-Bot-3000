# import requests as req
# import sys

# url = "http://ltdiadams.pythonanywhere.com/upload/"
# filePath = "/Users/logandiadams/Desktop/stored.csv"

# client = req.session()
# client.get(url)
# csrftoken = client.cookies['csrftoken']

# # data = {
# #     'csrfmiddlewaretoken': csrftoken,
# #     "smth": "/Users/logandiadams/Desktop/stored.csv"
# # }


# file = {
#     'csrfmiddlewaretoken': csrftoken,
#     'myFile': (open(filePath, 'rb'))
# }


# # res = req.post(url=url, data=data)
# res = client.post(url=url, data=data, headers=dict(Referer=url))

# print(res.status_code)

import requests
import time

def upload_it():
    with open("stored.csv", "rb") as f:
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

while True:
    upload_it()
    time.sleep(10)
