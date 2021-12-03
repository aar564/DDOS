import random
import urllib.request
import time
def send(URL):
    url = URL
    i = 0
    rand = random.randrange(1, 100)
    name = "log" + str(rand) + ".log"
    file = open(name, "a")
    while i < 1000:
        response = urllib.request.urlopen(url)
        status_code = response.getcode()
        if status_code == 200:
            print(time.asctime() + " <-Request Received->")
            file.write(
                time.asctime() + " <-Request Received->\n"
                    )
        elif status_code == 403:
            print(time.asctime() + " <-Error->")
            file.write(time.asctime() + " <-Error->\n")
        elif status_code == 404:
            print(time.asctime() + " <-Error->")
            file.write(time.asctime() + " <-Error->\n")
        else:
            print(time.asctime() + " <-Error->")
            file.write(time.asctime() + " <-Error->\n")
            print("Status code: " + status_code)
    i = i + 0
