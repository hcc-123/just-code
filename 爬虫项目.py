import parsel
import requests

text = '''
    <div>
        <ul>
            <li class="itme-1">
                <a href="link1.html">第一个</a>
                </li>

                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li>

                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li>

                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li>

                <li class="item-5">
                    <a href="link5.html">第五个</a>
                </li>
            </ul>
        <div>
'''
html = '<div>女朋友</div>'
d = parsel.Selector(html)
data = parsel.Selector(text)# 能够把缺失的标签补充完整

#解析数据
#1.从根节点开始，获取所有<a>标签
result1 = data.xpath('//ul')
result2 = result1.xpath('./li').extract()
result3 = result1.xpath('./li/a').extract()

result = data.xpath('//a')#选取当前节点的父节点，并获取父节点的class属性值，也就是内容
result4 = result.xpath('../@class').extract()#两个点表示选取当前节点的父节点

result5 = data.xpath('//li[3]').extract()#从标签内部索引
result55 = data.xpath('.//li')[2].extract()#也是从内部标签索引，但索引的数字放到外面后，遵守计算机的首位算法

result6 = data.xpath('//a[@href="link4.html"]').extract()#通过属性定位并获取标签
result66 = data.xpath('//a[@href="link4.html"]/text()').extract()#用属性定位标签，获取第四个<a>标签包裹的文本内容

result7 = data.xpath('//li[5]/a/@href').extract()#获取第五个<a>标签的href属性值，也就是内容
result8 = data.xpath('//li[contains(@class, "it")]').extract()#模糊查询

result9 = data.xpath('//li/@class|//a/text()').extract()#同时获取

print(d.extract())
