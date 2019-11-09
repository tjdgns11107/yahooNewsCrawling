from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('D:\workSpace\PythonTest\chromedriver')
driver.implicitly_wait(3)

driver.get('https://accounts.kakao.com')
driver.find_element_by_name('email').send_keys('aos15@naver.com')
driver.find_element_by_name('password').send_keys('dydtjr1')
driver.find_element_by_xpath('//*[@class="btn_g btn_confirm submit"]').click()