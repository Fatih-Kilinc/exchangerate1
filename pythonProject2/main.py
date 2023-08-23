import requests
import socket
import time

from bs4 import BeautifulSoup

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.close()
    print("connecting")
except Exception:
    print("Error")
    time.sleep(3)
    exit()

while True:
    url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    data = soup.find("div", class_="YMlKec fxKbKc").getText()
    time.sleep(5)
    print("Dolar:")
    print(data)
