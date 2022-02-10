import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2&sort=RD'
I_URL = 'https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx='
LIMIT = 1
'''
def extract_page():
	result = requests.get(URL)

	soup = BeautifulSoup(result.text, "html.parser")
	pagination = soup.find("div",{"class":"pagination"})
	link = pagination.find_all('a')
	pages = []

	for link in link[:-1]:
		pages.append(int(link.string))

	last_page = pages[-1]

	return last_page

'''
def extract_element(html):
	global LIMIT
	idx = html['id'][4:]
	result = requests.get(f"{I_URL}{idx}")
	soup = BeautifulSoup(result.text, "html.parser")
	infos = soup.find("div",{"class":"wrap_jview"})
		
	print()

	company = html.find("div",{"class":"company_nm"}).find("a").string
	title = html.find("div",{"class":"job_tit"}).find("a").string
	works = []
	work_s = html.find("span",{"class":"job_sector"}).find_all("span")#span값
	for work in work_s:
		works.append(work.string)
	
	career = html.find("p",{"class":"career"}).string
	education = html.find("p",{"class":"education"}).string
	employment_t = html.find("p",{"class":"employment_type"}).string
	place = html.find("p",{"class":"work_place"}).string
	lim = html.find("span",{"class":"reg_date"}).string
	if(lim == '(1일 전 등록)'):
		LIMIT = 0#수정필요
		return{"title" : title, "company" : company, "works" : works, "career" : career, "education" : education, "employment_type": employment_t, "work_place" : place} 


#	return[title,  company,  works,  career,  education,  employment_t,  place]
	return{"title" : title, "company" : company, "works" : works, "career" : career, "education" : education, "employment_type": employment_t, "work_place" : place} 


def extract_info(last_p):
	jobs = []

	result = requests.get(f"{URL}&page={last_p}")

	soup = BeautifulSoup(result.text, "html.parser")

	infos= soup.find_all("div", {"class":"list_item"})

	for info in infos:
		job = extract_element(info)
#		print(info['id'][4:])
		jobs.append(job)
	#	print(job)
		break
		
	return jobs


def main():
	global LIMIT
	a_jobs = []
	i = 2
	while(LIMIT):
		a_jobs.extend(extract_info(i))
		break
	dataA = pd.DataFrame(a_jobs)
#	print(dataA)



main()
