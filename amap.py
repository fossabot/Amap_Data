import requests
import json

# 设置参数key和url
amap_api_key = ''  # 输入自己的key
poi_search_url = 'https://restapi.amap.com/v3/place/around?'

# 获取单页POI
def getPoi(location, radius, types, page, times):
    req_url = poi_search_url + 'key=' + str(amap_api_key) + '&location=' + str(location) + '&radius=' + str(radius) + '&types=' + str(types) + '&page=' + str(page)
    try:
        result = requests.get(req_url)
        result.raise_for_status()
        content = result.text
        json_dict = json.loads(content)
        print(json_dict['pois'][k]['name'] +" ," + json_dict['pois'][k]['location'] +" ," + json_dict['pois'][k]['type'])
    except:
        print("获取数据失败。")
    return

# 程序循环（暴力取值，计数用i），项数用k。
i = 1
while i < 100:
    k = 0
    while k < 20:
        getPoi('121.459126,31.162659' , '3000' , '120300' , i, k)
        k += 1
    i += 1