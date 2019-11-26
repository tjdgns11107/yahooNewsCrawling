import requests
from bs4 import BeautifulSoup


class NotYnDetailTextException(Exception):
    def __init__(self):
        super().__init__('에러메시지')
class NotYjDirectSLinkTargetException(Exception):
    def __init__(self):
        super().__init__('에러메시지')

def getNewContents(news_link,keyword):
    response2 = requests.get(news_link)
    html2 = response2.text
    soup2 = BeautifulSoup(html2, 'html.parser')

    try:
        mediaNullCheck = soup2.select_one('p.ynCobrandBanner > a> img')['alt']
    except:
        mediaNullCheck=0
        print('not media');

    title = soup2.select_one('.hd > h1').text
    try:
        if(soup2.select_one('p.ynDetailText')):
            content = soup2.select_one('p.ynDetailText').text
        elif(soup2.select_one('.yjDirectSLinkTarget')):
            content = soup2.select_one('.yjDirectSLinkTarget').text
        else:
            content=0

    except:
        print(e)

    # media가 없을 경우를 위한 3항 연산
    media = mediaNullCheck if mediaNullCheck else "None media"

    # 디버깅용이니 삭제하면됨==
    print(title)
    print(media)
    # ========================

    return title, content, media, keyword
    # getTitle = soup2.select_one('.hd > h1').text
    # getContent = soup2.select_one('p.ynDetailText').text
    # getMedia = soup2.select_one('p.ynCobrandBanner > a> img')['alt']

    # print(getTitle)
    # print(getContent)
    # print(getMedia)