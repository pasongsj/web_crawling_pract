from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


URL = "https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2&sort=RD&page=2"
browser = webdriver.Chrome("/usr/local/bin/chromedriver");	#chromedriver 위치

browser.get(URL);	# 페이지 열기

browser.implicitly_wait(2)

#before_h = browser.execute_script("return window.scrollY")
# 스크롤
#browser.execute_script("window.scrollTo(0, 20)")
#print(browser)

'''
while True:
	browser.find_element_by_css_selector("body").send_keys(Keys.END)
	after_h = browser.execute_script("return window.scrollY")
	if after_h == before_h:
		break
'''

items = browser.find_elements(By.CSS_SELECTOR,'.list_item')
'''
for item in items:
	company = item.find_element(By.CSS_SELECTOR,".company_nm").text
	title = item.find_element(By.CSS_SELECTOR,".notification_info").text
	works = []
	sector = item.find_elements(By.CSS_SELECTOR, ".job_sector::before")
	i = 1
	print(sector[0])
#	for sec in sector:
#		works.append(metas.text)
#		print(i,sec.text)
#		i = i+1
'''
def get_info(html):
    items = html.find_elements(By.CSS_SELECTOR,'.list_item')

    for item in html:
        #id
        idx = item.get_attribute('id')[4:]
    
        # 회사
        company = item.find_element(By.CSS_SELECTOR,".company_nm").text
    
        # 제목
        title = item.find_element(By.CSS_SELECTOR,".notification_info").text
    
        # 경력
        career = item.find_element(By.CSS_SELECTOR,".career").text
    
        # 학력
        education = item.find_element(By.CSS_SELECTOR,".education").text
    
        # 근무형태
        employment_type = item.find_element(By.CSS_SELECTOR,".employment_type").text
    
        # 근무 위치
        work_place = item.find_element(By.CSS_SELECTOR,".work_place").text
    
        #마감일,등록일
        time = item.find_element(By.CSS_SELECTOR,".deadlines").text.split('\n')
        deadline = time[0]
        reg_date = time[1]
    return {'company' : company, 'title' : title, 'stack': 0, 'career' : career, 
            'education' : education, 'em_type' : employment_type, 'work_place':work_place, 'deadeline' : deadline }

print(get_info(browser))



#	career = item.find_element(By.CSS_SELECTOR,".recruit_conditio").text
#	support_info = item.find_element(By.CSS_SELECTOR,"col support_info").text
#	print(company, title, works)
#	print(works)




#	link = item.find_element_by_css_selector(".job_titi > a").get_attribute('href')
#	print(compay, recuit, support_info)



