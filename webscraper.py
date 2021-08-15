from bs4 import BeautifulSoup
import requests
import json

jobArr = []
url = 'https://www.simplyhired.com/search?q=rn+new+grad+program&l=San+Francisco+Bay+Area%2C+CA'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

for job in content.findAll('div', attrs={"class": "SerpJob-jobCard card"}):
    jobObject = {
        "jobName" : job.find('a', attrs={"class": "SerpJob-link card-link"}).text,
        "company" : job.find('span', attrs={"class": "JobPosting-labelWithIcon jobposting-company"}).text,
        "jobDescription": job.find('p', attrs={"class": "jobposting-snippet"}).text
    }
    if("dialysis" not in jobObject["jobDescription"] and "Skilled Nursing" not in jobObject["jobDescription"] and "sub-acute" not in jobObject["jobDescription"]):
        jobArr.append(jobObject)

url = 'https://www.indeed.com/jobs?q=New%20Grad%20RN%20Opportunity%20-LVN&l=San%20Francisco%20Bay%20Area%2C%20CA'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")
for job in content.findAll('div', attrs={"class": "job_seen_beacon"}):
    jobObject = {
        "jobName" : job.find('h2', attrs={"class": "jobTitle"}).text,
        "company" : job.find('span', attrs={"class": "companyName"}).text,
        "jobDescription": job.find('li').text
    }
    if("dialysis" not in jobObject["jobDescription"] and "Skilled Nursing" not in jobObject["jobDescription"] and "sub-acute" not in jobObject["jobDescription"]):
        jobArr.append(jobObject)


with open('jobData.json', 'w', encoding='utf-8') as outfile:
    json.dump(jobArr, outfile)