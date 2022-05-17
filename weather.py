from tkinter.font import _MetricsDict
import requests #pip install requests 맥북은 pip3 install requests
import json

city ='Seoul'
apikey = "9446492661af860487c728631b5106ea"
lang ="kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"

#units=metric 섭씨로
#units=imperial 켈빈으로
result = requests.get(api)
#print(result.text)

data= json.loads(result.text)
#print(type(result.text))
#print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는", data["weather"][0]["description"],"입니다")
print("현재 온도는",data["main"]["temp"],"입니다")
print("체감",data["main"]["temp_min"],"입니다")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ", data["wind"]["deg"],"입니다.")
print("풍속은 ", data["wind"]["speed"],"입니다.")
