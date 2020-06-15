import requests, time
from lxml import etree
from multiprocessing import Queue, Process
from threading import Thread
from urllib.parse import unquote
class C_s(object):
    def __init__(self):
        self.url = 'http://www.eso.org/public/archives/images/original/eso1242a.psb'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}
        self.folder = 'D:\\image'
        self.q = Queue()

    def work(self):
        self.get_link()

        L = []
        for i in range(16):
            th = Thread(target = self.down_load, args = (i + 1, ))
            th.start()
            L.append(th)

        for th in L:
            th.join()

    def get_link(self):
        res = requests.get(self.url, headers = self.headers)
        res.encoding = 'utf-8'
        html = res.text

        parseHtml = etree.HTML(html)
        r_list = parseHtml.xpath('//a/@href')[1:]

        for link in r_list:
            self.q.put(link)
            print('本次将下载', self.q.qsize(), '个文件')

    def down_load(self, n):
        while True:
            try:
                filename = unquote(self.q.get(block = True, timeout = 2))
            except:
                print('取不到链接，%s号线程结束工作'%n)
                break
            link = self.url + filename
            with closing(requests.get(link, headers = self.headers, stream = True, auth = ('tarenacode', 'code_2014')))


