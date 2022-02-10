import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit=50"

def extract_indeed_pages():
	result = requests.get(URL)

	soup = BeautifulSoup(result.text, "html.parser")

	pagination = soup.find("div",{"class":"pagination"})

	links = pagination.find_all('a')

	pages = []
	for link in links[:-1]:
		pages.append(int(link.string))

	last_page = pages[-1]
	return last_page


def extract_jobs(html):
	title = html.find("h2",{"class":"jobTitle"}).find_all('span')[-1].string #title
	company = html.find("span",{"class":"companyName"}).string
	location = html.find("div",{"class":"companyLocation"}).text
	job_id = html
	return {'title' : title, "company": company, "location" : location}


def extract_indeed_jobs(l_page):
	jobs = []
	#for page in range(l_page):
	result = requests.get(f"{URL}&start={l_page*LIMIT}")
	soup = BeautifulSoup(result.text, "html.parser")
	results = soup.find_all("div",{"class":"job_seen_beacon"})

	for result in results:
		job = extract_jobs(result)
		jobs.append(job)
		print(job)
		
	return jobs 

f_page = extract_indeed_pages()
for i in range(1,f_page+1):
	ajobs = extract_indeed_jobs(i)
	




