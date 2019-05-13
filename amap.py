import requests
import json
from bs4 import BeautifulSoup

# 设置参数key和url
amap_api_key = ''  # 输入自己的key
poi_search_url = 'https://restapi.amap.com/v3/place/around?'

# 设置POI爬取区域
# location = '121.459126,31.162659'
# radius = '2000'

# 获取单页POI
def getPoi(location, radius, types, page, times):
    req_url = poi_search_url + 'key=' + str(amap_api_key) + '&location=' + str(location) + '&radius=' + str(radius) + '&types=' + str(types) + '&page=' + str(page)
    try:
        result = requests.get(req_url)
        result.raise_for_status()
#        print(result.text)                               # 仅供调试
        content = result.text
        json_dict = json.loads(content)
        print(json_dict['pois'][k]['name'] +" ," + json_dict['pois'][k]['location'] +" ," + json_dict['pois'][k]['type'])
    except:
        print("获取数据失败。")
    return

# 测试用
#getPoi('121.459126,31.162659', 2000, 120300, 1, k)



# 程序循环（暴力取值，计数用i） 一个想法：使用BeautifulSoup获取其含有多少项，用项目数去除以20，向上取整，其页数就是应该选择的上限，可以有效地节省时间。（但是能力有限...)
i = 1
while i < 100:
    k = 1
    while k < 20:
        getPoi('121.459126,31.162659' , '3000' , '120300' , i, k)
        k += 1
    i += 1
