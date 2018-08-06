import requests
from urllib import request
def tiebaSpider(url,beginPage,endPage):
    for page in range(beginPage,endPage):
        pn = (page-1) * 50
        filename = "第"+str(page)+"页.html"
        fullurl = url + "&pn=" + str(pn)
        html = loadPage(fullurl, filename)
        writeFile(html, filename)
        print('已完成第%d页'%page)

def loadPage(url, filename):
     print("正在下载" + filename)
     headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
     request_name = request.Request(url = url,headers=headers)
     response = request.urlopen(request_name)
     return response.read().decode('utf-8')

def writeFile(html, filename):
    print("正在存储" + filename)
    with open("C:\\Users\\123\\test\\%s"%filename, 'w',encoding='utf-8') as f:
        f.write(html)
    print("-" * 20)

if __name__ == '__main__':
    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))
    url_f = "http://tieba.baidu.com/f?"
    key = {"kw": kw}
    r = requests.get(url_f, params=key)
    url = r.url
    tiebaSpider(url, beginPage, endPage)