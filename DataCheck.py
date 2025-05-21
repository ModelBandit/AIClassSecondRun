import requests
import xmltodict
import pandas

url = 'http://apis.data.go.kr/B551172/CancerScreenorCohortStatusService/getCancerScreenorCohortCancerIncCnt'
params ={'serviceKey' : 'oB7JQ8sJkU7rc9AyjjkqDStU9Dcd/nmsN2S4AlUIWYAUPdREEp1a+YKU6+B2W0LKte2WMtXiHQkiSOQJybsXNw==', 'numOfRows' : '10', 'pageNo' : '1', 'resultType' : 'xml' }

response = requests.get(url, params=params)

print(f"response - {response}")

content = response.text

print(f"content - {content}")

dic = xmltodict.parse(content)

df = pandas.DataFrame(dic)

print("데이터프레임", df)