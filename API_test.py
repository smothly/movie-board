import requests
from collections import defaultdict
import json

# 예시
# http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=430156241533f1d058c603178cc3ca0e&targetDt=20120101
URL = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
PARAMS = {}


PARAMS["key"] = "430156241533f1d058c603178cc3ca0e"
PARAMS["targetDt"] = "20200816"

r = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
data = r.json() 
print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii = False))
# print(data)