from bs4 import BeautifulSoup
import requests
from datetime import datetime

def todayDate():
    now = datetime.now()
    return ('%s月%s日' %(now.month, now.day))

def todayNews(newsDate):
    if newsDate == todayDate():
        return 1
    else:
        return 0

page = 1
todayNewsCnt=0
news_links = []

while page <= 50:
    #검색 사이트
    url = "https://news.yahoo.co.jp/search/;_ylt=A2Rivc6iSMZdWQ4A0xeEmuZ7?p=ソフトバンク&vaop=a&to=0&st=&c_=dom&c_=c_int&c_=bus&c_=c_ent&c_=c_sci&c_=c_life&c_=loc&ei=UTF-8&&b="+str(page)

    #url 요청해서 응답 받아서 저장
    response = requests.get(url)
    #응답받은 text 을 html변수에 저장
    html = response.text
    #키워드로 검색한 내용 링크 리스트 저장용 변수 선언

    #bs4사용
    soup = BeautifulSoup(html, 'html.parser')

    getNewsCount = soup.select('.l > .txt > p > .d')

    #href를 찾는 코드
    goToATages = soup.select('h2.t > a')
    for atag in range(len(goToATages)):
        news_links.append(goToATages[atag]['href'])
        newsDate = soup.select('.l > .txt > p > .d')[atag].text.split('（')[0] # 월月일日추출
        if todayNews(newsDate):
            todayNewsCnt += todayNews(newsDate)
        else:
            break
        print(todayNewsCnt)


    # print(todayNewsCnt)
    page+=10



#=====================
#그냥 확인용 지워야함==
for i in range(len(news_links)):
    print(news_links[i])
#=====================
#=====================


#===================여기서 부턴 함수로 만들자==================
def getNewContents(news_link):
    response2 = requests.get(news_link)
    html2 = response2.text

    soup2 = BeautifulSoup(html2, 'html.parser')

    getTitle = soup2.select_one('.hd > h1').text
    getContent = soup2.select_one('p.ynDetailText').text
    getMedia = soup2.select_one('p.ynCobrandBanner > a> img')['alt']

    print(getTitle)
    print(getContent)
    print(getMedia)

