import CrawlingModule



keyword = ['ソフトバンク']
#append로 키워드 추가해서 검색하기
#keyword.append('')

print(' '.join(keyword))
cm = CrawlingModule.md(' '.join(keyword))


cm.runCrawling()
