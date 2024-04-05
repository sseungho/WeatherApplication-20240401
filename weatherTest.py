import requests  # pip install requests

from bs4 import BeautifulSoup  # pip install beautifulsoup4

inputArea = input("날씨를 조회하려는 지역을 입력하세요 :")

weatherHtml = requests.get(f"https://search.naver.com/search.naver?&query={inputArea}날씨")
# 네이버에서 한남동날씨로 검색한 결과 html 파일 가져오기
# print(weatherHtml.text)

weatherSoup = BeautifulSoup(weatherHtml.text, 'html.parser')
# print(weatherSoup)

areaText = weatherSoup.find("h2", {"class":"title"}).text  # 날씨 지역 이름 가져오기
areaText = areaText.strip()  # 양쪽 공백 제거
print(f"지역이름 : {areaText}")

todayTempText = weatherSoup.find("div",{"class":"temperature_text"}).text  # 현재온도 가져오기
todayTempText = todayTempText[6:12].strip()  # 6번째 글자부터 슬라이싱 후 양쪽 공백 제거
print(f"현재온도 : {todayTempText}")

# yesterdayTempText = weatherSoup.find("span", {"class":"temperature"}).text  #어제와의 날씨 비교
# yesterdayTempText.strip()
yesterdayTempText = weatherSoup.find("p", {"class":"summary"}).text  #어제와의 날씨 비교
yesterdayTempText = yesterdayTempText[:15].strip()
print(f"어제날씨비교 : {yesterdayTempText}")

todayWeatherText = weatherSoup.find("span", {"class":"weather before_slash"}).text  # 오늘 날씨 텍스트
todayWeatherText.strip()
print(f"오늘날씨 : {todayWeatherText}")

senseTempText = weatherSoup.find("dd", {"class":"desc"}).text  # 현재 체감온도
senseTempText = senseTempText.strip()
print(f"체감온도 : {senseTempText}")

todayInfoText = weatherSoup.select("ul.today_chart_list>li")  # 미세먼지, 초미세먼지, 자외선, 일몰
# print(todayInfoText)
# print("-------------------------------")
# print(todayInfoText[0])
dust1Info = todayInfoText[0].find("span",{"class":"txt"}).text  # 미세먼지 정보
dust1Info = dust1Info.strip()
print(f"미세먼지 : {dust1Info}")
dust2Info = todayInfoText[1].find("span",{"class":"txt"}).text  # 초미세먼지 정보
dust2Info = dust2Info.strip()
print(f"초미세먼지 : {dust2Info}")



