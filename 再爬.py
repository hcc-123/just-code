from urllib3 import *
import json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib.request as r
import requests
import threading

requests.packages.urllib3.disable_warings()

basepath = 'D:\\image'
http = PoolManager()
def getRTUTxt():
    f = open('db.txt', 'a', encoding = 'utf-8')
    for page_start in range(0, 340, 20):
        try:
            url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}".format(page_start)
            r = http.request('GET', url, headers = {'User-Agent': str(UserAgent().random)})
            c = r.data.decode('utf-8')
            c = c.replace('false', '"false"')
            c = c.replace('true', '"true"')
            jsonDict = json.loads(c)
        except Excepiton as e:
            pass
        List = jsonDict['subjects']
        for i in range(len(List)):
            f.write( str(List[i]['rate']) + ',' + str(List[i]['title']) + ',' + str(List[i]['url']) + '\n')
        print(page_start)
    f.close()

def getTUList():
    resList = []
    with open('db.txt', 'r', encoding = 'utf-8') as f:
        for line in f:
            resList.append(line)
    f.close()
    resList = list(set(resList))
    return resList


def getImgUrl(url):
    r = http.request('GET', url, headers = {'User-Agent': str(UserAgent().random)})
    c = r.data.decode('utf-8', 'ignore')
    soup = BeautifulSoup(c, 'lxml')
    imgUrl = soup.find('a', class_ = 'nbgnbg').find('img').get('src')
    return imgUrl

def download(imgUrl, filename):
    r.urlretrieve(imgUrl, filename)

if __name__ == '__main__':
    List = getTUList()
    tList = []
    for i in range(len(List)):
        try:
            title = str(List[i]).split(',')[1]
            imgUrl = getImgUrl(str(List[i]).split(',')[2])
            filename = basepath + title + '.jpg'
            t = threading.Thread(target = download, args = (imgUrl, filename))
            t.start()
            tList.append(t)
        except Exception as e:
            pass

    for t in tList:
        t.join()