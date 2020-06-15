import requests
from pyquery import PyQuery as pq
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
proxies = {
    'https': '218.75.69.50:39590'
}
def start_requests(url):
    r = requests.get(url, headers = headers, proxies = proxies)
    r.encoding = 'GBK'
    html = r.text
    return html

def parse(text):
    doc = pq(text)
    images = doc('div.list ul li img').items()
    x = 0
    for image in images:
        img_url = image.attr('src')
        img = requests.get(img_url, headers = headers, proxies = proxies).content
        path = 'F:\\Program Files (x86)' + '.jpg'
        with open (path, 'wb') as f:
            f.write(img)
            time.sleep(1)
            print('正在下载第{}张'.format(x))
            x += 1
    print('写入完成')

def main():
    url = 'http://www.netbian.com'
    text = start_requests(url)
    parse(text)

if __name__ == '__main__':
    main()
