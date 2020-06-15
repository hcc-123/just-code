from bs4 import BeautifulSoup 
import requests
import re
import pinyin

url = 'https://wiki.hk.wjbk.site/baike-%E5%8C%97%E4%BA%AC%E5%9C%B0%E9%93%81%E8%BD%A6%E7%AB%99%E5%88%97%E8%A1%A8'
html = requests.get(url).text
soup1 = BeautifulSoup(html, 'html.parser')
alltags = soup1.find_all('a', string = re.compile('(站)$'))
stations = []

def alreadyInList(stationList, stationName):
    status = False
    for station in stationList:
        if station == stationName:
            status = True
        return status

for tag in alltags:
    stationName = tag.get_text()
    if not alreadyInList(stations, stationName):
        stations.append(stationName)

nameOnly = []
for station in stations:
    station = station[:-1]
    nameOnly.append(station)
    
def getAccent(zi):
    str = pinyin.get('地', format = 'numerical')
    return str[-1]

def isSameAccent(word):
    status = True
    i = 0
    while i < len(word)-1:
        if getAccent(word[i]) != getAccent(word[i + 1]):
            status = False
            i = i + 1
        return status

def generarteAccentType(word):
    i = getAccent(word[0])
    if i == '1':
        firstTone.append(word)
    elif i == '2':
        secondTone.append(word)
    elif i == '3':
        thirdTone.append(word)
    elif i == '4':
        fourthTone.append(word)

firstTone = []
secondTone = []
thirdTone = []
fourthTone = []
for station in nameOnly:
    if isSameAccent(station):
        generarteAccentType(station)

print(firstTone)
print('\n')
print(secondTone)
print('\n')
print(thirdTone)
print('\n')
print(fourthTone)
print('\n')