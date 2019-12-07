import CrawlingModule


class MainCrawling():
    def __init__(self, keywords):
        # keyword = []
        # for val in keywords:
        #     keyword.append(val)
        #append로 키워드 추가해서 검색하기
        #keyword.append('')
        print(keywords)
        print(' '.join(keywords))
        cm = CrawlingModule.md(' '.join(keywords))


        cm.runCrawling()

if (__name__ == '__main__'):
    MainCrawling('ソフトバンク')
