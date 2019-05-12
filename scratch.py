import requests
import xlwt
import json
from bs4 import BeautifulSoup

# 设置参数,ak和url
amap_api_key = 'aebe8987a93ab393b85e37c34b064f27'  # 输入自己的ak
poi_search_url = 'https://restapi.amap.com/v3/place/around?'

# 设置POI爬取区域
#location = '121.459126,31.162659'
#radius = '2000'

# 获取单页POI
def getPoi(location , radius , types ,page):
    req_url = poi_search_url + 'key=' + str(amap_api_key) + '&location=' + str(location) + '&radius=' + str(radius) + '&types=' + str(types) + '&page=' + str(page)
    try:
        r1 = requests.get(req_url)
        r1.raise_for_status()
        r1.encoding=r1.apparent_encoding
        print("服务器连接成功")                           # 请注意，此处数据抓取成功仅表示能否连接，并不代表数据是否已经获取到。
        print(r1.text)                               # 仅供试用，实际情况这里不显示所获取到的数据。
    except:
        print("服务器连接失败，请检查网络连接。")
    return

# 程序循环（暴力取值，取到100页）             一个想法：使用BeautifulSoup获取其含有多少项，用项目数去除以20，向上取整，其页数就是应该选择的上限，可以有效地节省时间。（但是能力有限...)
pages = 1
while pages < 100:
    getPoi('121.459126,31.162659' , '3000' , '120300' , pages)
    pages += 1
