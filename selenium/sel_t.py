from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


URL = "https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2&sort=RD&page=2"
browser = webdriver.Chrome("/usr/local/bin/chromedriver");	#chromedriver 위치

browser.get(URL);	# 페이지 열기

browser.implicitly_wait(2)

#before_h = browser.execute_script("return window.scrollY")
# 스크롤
brower.execute_script("window.scrollTo(0, 20)")

'''
while True:
	browser.find_element_by_css_selector("body").send_keys(Keys.END)
	after_h = browser.execute_script("return window.scrollY")
	if after_h == before_h:
		break
'''
items = browser.find_elements(By.CSS_SELECTOR,'.list_item')

for item in items:
	company = item.find_element(By.CSS_SELECTOR,".company_nm").text
	title = item.find_element(By.CSS_SELECTOR,".notification_info").text
	works = []
	meta = item.find_elements(By.CSS_SELECTOR, ".job_meta")
	for metas in meta:
		works.append(metas.text)
#	career = item.find_element(By.CSS_SELECTOR,".recruit_conditio").text
#	support_info = item.find_element(By.CSS_SELECTOR,"col support_info").text
	print(company, title, works)




#	link = item.find_element_by_css_selector(".job_titi > a").get_attribute('href')
#	print(compay, recuit, support_info)



