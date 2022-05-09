from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+devloper&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')   # print(html_text)
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    job_published_date = job.find('span', class_='sim-posted').span.text
        # if 'few' in job_published_date:
    company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
    skills = job.find('span', class_='srp-skills').text.replace(' ','')
    more_info = job.header.h2.a['href']
        # if unfamiliar_skill not in skills:

    print(f"Company name: {company_name.strip()}")
    print(f"Required skills: {skills.strip()}")
    print(f'more_info : {more_info}')

    # print(job_published_date)
    print('')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
