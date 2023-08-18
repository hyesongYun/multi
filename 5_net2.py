import requests #requests:http를 사용하기 위해 쓰는 라이브러리
from bs4 import BeautifulSoup #BeautifulSoup:텍스트 형태의 데이터에서 원하는 html태그 추출
from pprint import pprint #pprint:pretty print 보기좋게 정렬

html=requests.get('https://search.naver.com/search.naver?query=날씨')
pprint(html.text)

soup = BeautifulSoup(html.text,'html.parser') #parsing:입력 데이터를 구조화된 형식으로 변환
data1 = soup.find('div', {'class':'weather_box'})

find_address = data1.find('span', {'class':'location_name'}).text
print('현재 위치: '+find_address)

find_currenttemp = data1.find('span',{'class':'current'}).text
print('현재 온도: '+find_currenttemp+'℃')
