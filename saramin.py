import requests
from bs4 import BeautifulSoup

URL = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?cat_mcls=2'
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

	return{"title" : title, "company" : company, "works" : works, "career" : career, "education" : education, "employment_type": employment_t, "work_place" : place} 


def extract_info(last_p):
	jobs = []

	result = requests.get(f"{URL}&page={last_p}")

	soup = BeautifulSoup(result.text, "html.parser")

	infos= soup.find_all("div", {"class":"list_item"})

	for info in infos:
		job =extract_element(info)
		jobs.append(job)
		print(job)
		print("\n\n")
	return jobs



e_pages = extract_page()
for i in range(1, e_pages):
	a_jobs = extract_info(i)




