import requests
from lxml import etree
import re

url = 'https://m.qidian.com/book/1009482425/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.69'
}

next_chapter_code = '376011494'
for i in range(5):
    response = requests.get(url + next_chapter_code, headers = headers)
    print('打开' + url + next_chapter_code + '...')
    next_chapter_code = re.findall('"next":(.*?),"', response.text, re.S)[0]
    content = re.findall('<section class = "read-section jsChapterWrapper" data-chapter-id="\d+" >(.*?)')
    f = open('f:\\pic\\声优.html', 'a')
    f.write(content)
    f.close()