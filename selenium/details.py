from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('headless')

URL = "https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2&sort=RD&page=2"
browser = webdriver.Chrome("/usr/local/bin/chromedriver");	#chromedriver 위치

browser.get(URL);	# 페이지 열기

browser.implicitly_wait(2)

def get_stack(d_url):
    
    d_browser = webdriver.Chrome("/usr/local/bin/chromedriver",chrome_options=options)
    d_browser.get(d_url)

    d_browser.implicitly_wait(2)

    stacks = d_browser.find_element(By.CSS_SELECTOR,'.scroll')
    tmps = stacks.find_elements(By.TAG_NAME, 'a')
    stack = []
    for tmp in tmps:
        url = tmp.get_attribute('href')
        index = url.find('kewd')
        if(index != -1):
            stack.append(url[index+5:])
	
    return stack
    
def get_info():

    items = browser.find_elements(By.CSS_SELECTOR,'.list_item')
    ann_list = []
    for item in items:
        #id
        idx = item.get_attribute('id')[4:]
        D_URL = 'https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx='+idx
        stack = []
        #stack = get_stack(D_URL)
        
        # 회사
        company = item.find_element(By.CSS_SELECTOR,".company_nm").find_element(By.TAG_NAME, 'a').text
    
        # 제목
        title = item.find_element(By.CSS_SELECTOR,".notification_info").find_element(By.TAG_NAME, 'a').text
    
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
        info = {'company' : company, 'title' : title, 'stack': stack, 'career' : career, 
            'education' : education, 'em_type' : employment_type, 'work_place':work_place, 'deadeline' : deadline }
        ann_list.append(info)
        print(info, idx)
        print("\n")
    return ann_list

get_info()

quit()
