from selenium import webdriver
import time
from random import randrange

refresh_time = 10
browser_list = []

for i in range(10):
    browser = webdriver.Chrome(executable_path='/Users/sriharshatanamala/opt/anaconda3/bin/chromedriver')
    browser_list.append(browser)


for browser in browser_list:
    browser.get("https://www.youtube.com/watch?v=POE4IQvfYUk")

while(True):
    browser_num = randrange(0, len(browser_list))
    browser_list[browser_num].refresh()
    print("browser number", browser_num, "refreshed")
    time.sleep(refresh_time)

browser.close()
