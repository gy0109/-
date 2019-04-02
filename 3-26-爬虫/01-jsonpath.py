import jsonpath
import requests
import json

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
response = requests.get(url)
html_str = response.content.decode()

json_obj = json.loads(html_str)

city_list = jsonpath.jsonpath(json_obj, '$..name')
fp = open('city.json', 'w')
content = json.dumps(city_list, ensure_ascii=False)
fp.write(content.encode('utf-8'))
fp.close()
