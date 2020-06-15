import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69'
}
url = 'https://www.tohomh123.com/zhegezongcaiyoudiancan/11.html'
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, 'html.parser')
a = soup.find_all("div", class_ = "mCustomScrollBox")
print(a)
