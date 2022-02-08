import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2&sort=RD'
LIMIT = 1

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


def extract_element(html):
	global LIMIT
	company = html.find("div",{"class":"company_nm"}).find("a").string
	title = html.find("div",{"class":"job_tit"}).find("a").string
	works = []
	work_s = html.find("span",{"class":"job_sector"}).find_all("span")#span값
	for work in work_s:
		works.append(work.string)
	
	career = html.find("p",{"class":"career"}).string
	education = html.find("p",{"class":"education"}).string
	employment_t = html.find("p",{"class":"employment_type"}).string
	try:
		place = html.find("p",{"class":"work_place"}).string
	except Exception as e:
		place = "None"

	lim = html.find("span",{"class":"reg_date"}).string
#	print(lim)
	if(lim == '(1일 전 등록)'):
		LIMIT = 0

	return[title,  company,  works,  career,  education,  employment_t,  place]


def extract_info(last_p):
	jobs = []

	result = requests.get(f"{URL}&page={last_p}")

	soup = BeautifulSoup(result.text, "html.parser")

	infos= soup.find_all("div", {"class":"list_item"})

	for info in infos:
		job = extract_element(info)
		jobs.append(job)
	#	print(job)
	#	print("\n")
		
	return jobs


def main():
	global LIMIT
	a_jobs = []
	i = 2
	while(LIMIT):
		a_jobs.extend(extract_info(i))
		i = i+1

#	dataA = pd.DataFrame(a_jobs)
#	print(dataA)


main()

