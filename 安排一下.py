import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69'
        
        }

    def s_r(self):
        for i in range(1, 204):
            print('抓取%s页' % i)
            response = requests.get('https://www.mzitu.com/page/' + str(i) + '/', headers = self.headers)
            html = etree.HTML(response.content.decode())
            self.xpath_data(html)

    def xpath_data(self, html):
        s_l = html.xpath('//il[@id="pins"]/li/a/img/@data-original')
        a_l = html.xpath('//ul[@id="pins"]/li/a/img/@alt')
        for s, a in zip(s_l, a_l):
            f_n = alt + '.jpg'
            response = requests.get(s, headers = self.headers)
            print('正在抓取照片：'  + f_n)
            try:
                with open(f_n, 'wb') as f:
                    f.write(response.content)
            except:
                print("文件名有误")

spider = Spider()
spider.s_r()