# coding:utf-8
import requests
from lxml import etree
page = list(range(160))
url = "http://www.ccxi.com.cn/cn/Init/bond/180/0?&page="
headers = {
"Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
# "Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Connection": "keep-alive",
"Cookie": "lu=bebaa9coZm3cz%2Bcxcuf2zKQQ92KFrqle83CZeO9pQ4FbbhtR3gxA; lm=191304aATvxoyGMTXItBkqBUvcjxFw%2Fdad%2Bkpr81HYQNktdFjxINtG; rlu=bebaa9coZm3cz%2Bcxcuf2zKQQ92KFrqle83CZeO9pQ4FbbhtR3gxA; rlm=191304aATvxoyGMTXItBkqBUvcjxFw%2Fdad%2Bkpr81HYQNktdFjxINtG; shop=beb43cdaa62455185b18f5d92c75ed3fd38a99ec",
"Host": "www.ccxi.com.cn",
# "Referer": "http://www.ccxi.com.cn/cn/Init/bond/180/184?&page=2",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
for i in page:
    html = requests.get("http://www.ccxi.com.cn/cn/Init/bond/180/0?&page=%s"%page, headers=headers).text.encode("utf-8")
    tree = etree.HTML(html)
    ul = tree.xpath('//li[@class="l1"]//a/text()')
    for i in ul:
        print(i)