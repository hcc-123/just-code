import requests
from lxml import etree
import parsel
'''
url = 'https://movie.douban.com/subject/26348103'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' 
                    '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
response = requests.get(url, headers = headers)
h = response.content.decode('utf-8')
data = parsel.Selector(h)

result = data.xpath('//ul')
print(result.extract())
'''
s = 0
i = 3
while True:
    if i <= n:
        s += i
        print('aaa')