# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests

def getAllLinks()->list:
    url = "https://astana.hh.kz/search/resume?customDomain=1"
    page = requests.get(url,headers={'User-agent': 'Edge (Standard)'})
    print(page)
    result = []
    soup = BeautifulSoup(page.content,'html.parser')
    # print (soup.find_all('a', class_="serp-item__title", href=True))
    for a in soup.find_all('a', class_="serp-item__title", href=True):
        result.append("https://astana.hh.kz/" +a['href'])
    return result

def getResumeData(url):
    data = []
    page = requests.get(url, headers={'User-agent': 'Edge (Standard)'})
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.select(".resume-block__title-text")[0].text
    data.append(title)
    specialization = soup.select(".resume-block__specialization")[0].text
    data.append(specialization)
    try:
        salary = soup.select(".resume-block__salary")[0].text
        salary = salary.split()[0:-2]
        salary = list(filter(lambda x: x.isdigit(),salary))[0] + list(filter(lambda x: x.isdigit(),salary))[1]
        data.append(salary)
    except Exception as excepttion:
        data.append(0)

    # print(title,specialization,salary)
    print(data)
print(getAllLinks())
for resumeUrl in getAllLinks():
    getResumeData(resumeUrl)
