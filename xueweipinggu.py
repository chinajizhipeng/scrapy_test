from lxml import etree
import pandas as pd
def first_class():
    html = etree.parse('http://www.chinadegrees.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?yjxkdm=0201&xkdm=01,02,03,04,05,06',etree.HTMLParser())
    ps = html.xpath('//table//td[@width="13%"]/p')
    for p in ps:
        url = p.xpath('./a/@href')[0]
        fir_name = p.xpath('./a/text()')[0]
        print(fir_name[0])
        main_url = 'http://www.chinadegrees.cn/webrms/pages/Ranking/%s'%url
        sec_class(main_url,fir_name)
def sec_class(main_url,fir_name):
    html = etree.parse(main_url,etree.HTMLParser())
    p2s = html.xpath('//td[@style="line-height:25px;"]/p')
    for ps in p2s:
        #第二级学科网页的属性
        sec_url = ps.xpath('./a/@href')[0]
        #代码 学科
        num_class = ps.xpath('./a/text()')[0]
        #第二级学科的代码
        sec_num = num_class.split(' ')[0]  
        #第二级学科的名字
        sec_class = num_class.split(' ')[1]
        #最终爬取的网页
        fin_url = 'http://www.chinadegrees.cn/webrms/pages/Ranking/%s'%sec_url
        scrapy_rating(fin_url,fir_name,sec_class,sec_num)
def scrapy_rating(url,fir_name,sec_class,sec_num):
    html = etree.parse(url,etree.HTMLParser())
    trs = html.xpath('//div[@style="height:510px; overflow:scroll;"]//tr') 
    for tr in trs:
        fir_names.append(fir_name)
        sec_nums.append(sec_num)
        sec_names.append(sec_class)
        if tr.xpath('./td[@align="center"]/text()'):
            r = tr.xpath('./td[@align="center"]/text()')
            rate.append(r[0])
            num_schs= tr.xpath('./td[@width="70%"]/div/text()')
            num.append(num_schs[0].split('\xa0\xa0\xa0\xa0\xa0\xa0')[0])
            schs.append(num_schs[0].split('\xa0\xa0\xa0\xa0\xa0\xa0')[1])
        else:
            rate.append(r[0])
            num_schs= tr.xpath('./td[@width="70%"]/div/text()')
            num.append(num_schs[0].split('\xa0\xa0\xa0\xa0\xa0\xa0')[0])
            schs.append(num_schs[0].split('\xa0\xa0\xa0\xa0\xa0\xa0')[1])
    data = {'第一大类学科':fir_names,'第二大类学科代码':sec_nums,'第二大类学科名称':sec_names,'等级':rate,'学校代码':num,'学校名称':schs}
    df_data = pd.DataFrame(data)
    df_data.to_excel('学校等级1.xlsx',header=True)
if __name__ == '__main__':
	rate = []
	num  = []
	schs = []
	fir_names = []
	sec_nums = []
	sec_names = []
	first_class()