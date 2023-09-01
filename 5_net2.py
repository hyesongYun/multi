from selenium import webdriver
from selenium.webdriver.chrome.options import Options #selenium 라이브러리에서 Options을 가져옴
from selenium.webdriver.common.by import By #selenium 라이브러리에서 By를 가져옴

#webdriver 함수
def chromdriveron():
    chrome_options=Options() #브라우저 option 설정선언
    chrome_options.add_argument("headless") #headless:브라우저 창을 숨기고 실행
    driver=webdriver.Chrome(options=chrome_options) #chrome을 사용하겠다고 선언 / option중 headless 사용
    driver.implicitly_wait(10) #암묵적 대기: 설정 시간동안 대기하여 실행될때까지 기다림,설정시간 내에 실행되면 다음으로 넘어감
    return driver #driver 반환

#날씨 정보를 가져오는 함수
def weather(city,driver):
    area=f'{city}날씨'
    weather_url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={area}'
    driver.get(weather_url) #해당 url로 접속
    wh=driver.find_element(By.CLASS_NAME,"temperature_text").text
    #날씨 정보를 찾아서 텍스트로 추출/ By.CLASS_NAME은 클래스 이름을 가지고 요소를 찾음
    return wh #날씨 정보를 반환

#메인 함수
def main():
    driver=chromdriveron()

    cities=['울산','부산','서울','대구'] #도시 정보
    whlist = list()
    for city in cities:
        wh=weather(city,driver) #도시의 날씨 정보 가져오기
        whlist.append(wh) #whlist에 wh의 정보를 저장
    driver.quit() #webdriver종료
    
    #도시와 온도를 저장할 리스트
    sorted_cities = list()
    sorted_whlist = list()

    #도시와 온도 정보를 묶고 온도를 기준으로 정렬
    #zip:두개의 리스트를 하나로 묶을 수 있음/ sorted: 정렬된 리스트를 생성, sort는 리스트를 정렬 해줌/ reverse=True로 내림차순 정렬
    weather_set = sorted(zip(whlist, cities), reverse=True)

    for wh, city in weather_set:
        sorted_cities.append(city) #정렬된 도시를 리스트에 저장
        sorted_whlist.append(wh) #정렬된 온도를 리스트에 저장

    #각 도시와 도시의 온도 출력
    for city, wh in zip(sorted_cities, sorted_whlist):
        print(f'{city}: {wh}°C')

main()
