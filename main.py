# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from bs4 import BeautifulSoup
import requests

def getAllLinks(url)->list:
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
    try:
        # age = soup.find(attrs={'class': 'resume-online-status_online', 'data-qa': 'resume-personal-age'})[0].text
        # age = soup.select(".resume-online-status_online")[0].text
        age =soup.select_one('span[data-qa=resume-personal-age]').get_text()[0]+soup.select_one('span[data-qa=resume-personal-age]').get_text()[1]
        data.append(age)
    except Exception as excepttion:
        data.append(0)
    try:
        if len(soup.find("div", class_="resume-block-container").contents) <2:
            raise Exception("less than 2")
        employment = soup.find("div", class_="resume-block-container").contents[1].text
        employment = employment.replace("Занятость: ", '')
        data.append(employment)
    except Exception as excepttion:
        print(excepttion)
        data.append(0)
    try:
        # if len(soup.find("div", class_="resume-block-container").contents) <2:
        #     raise Exception("less than 2")
        schedule = soup.find("div", class_="resume-block-container").contents[2].text
        schedule = schedule.replace("График работы: ", '')
        data.append(schedule)
    except Exception as excepttion:
        print(excepttion)
        data.append(0)

    try:
        # if len(soup.find("div", class_="resume-block-container").contents) <2:
        #     raise Exception("less than 2")
        experience_years = soup.find("span", class_="resume-block__title-text resume-block__title-text_sub").contents
        experience_years = ' '.join([n.text for n in experience_years])
        # experience_years = list(filter(lambda x: x.isdigit(), experience_years))
        experience_years = experience_years.replace("Опыт работы ", '')
        experience_years = experience_years.split()[0:4]
        data.append(experience_years)
    except Exception as excepttion:
        print(excepttion)
        data.append(0)
    try:
        # if len(soup.find("div", class_="resume-block-container").contents) <2:
        #     raise Exception("less than 2")
        citisenship = soup.select('[data-qa="resume-block-additional"] > .resume-block-item-gap > ''.bloko-columns-row > .bloko-column > .resume-block-container > p')[0].text
        citisenship = citisenship.replace("Гражданство: ", '')
        data.append(citisenship)
    except Exception as excepttion:
        print(excepttion)
        data.append(0)

    # print(title,specialization,salary)
    return (data)
# print(getAllLinks())
n = 1
while n <3:
    n+=1
    url = "https://hh.kz/search/resume?page=" +str(n)
    for resumeUrl in getAllLinks(url):
        print(getResumeData(resumeUrl))
    url = ""
