from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("/usr/local/bin/chromedriver");
browser.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=30&filter=0&vjk=9f1b3a55c974207a");

items = browser.find_elements(By.CSS_SELECTOR, "div.jobTitle jobTitle-color-purple > span")
i = 1
for item in items:
	print(item.text,"\n")
	print(i)
	i = i + 1
