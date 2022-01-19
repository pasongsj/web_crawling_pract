import requests
from bs4 import BeautifulSoup


LIMIT = 50
URL = "https://www.indeed.com/jobs?q=python&limit={LIMIT}"

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


def extract_indeed_jobs(l_page):
	for page in range(l_page):
		print(f"&start={page*LIMIT}")


'''
#print(max_pages)

def extract_indeed_jobs(last_pages):
	url = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=25&l&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=1654acb6db3db1e0"
	indeed_result = requests.get(url)
	soup = BeautifulSoup(result.text, "html,parser")
	result = soup.find_add("div", {"class":"job_seen_beacon"})
	print(result)
	return jobs

extract_indeed_jobs(1)
'''