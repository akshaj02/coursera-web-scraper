from bs4 import BeautifulSoup
import requests
import re

URL = "https://boards.greenhouse.io/embed/job_board?for=coursera"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
# list for all the URLs
urls = []
for link in soup.findAll('a'):
    #append the URL to the list
    urls.append(link.get('href'))

#list for new urls
newUrls = []
for i in range(len(urls)):
    #split the URL at = to get the token number
    x = re.split("=", urls[i])
    #join the token number with the new URL
    newUrl = "https://boards.greenhouse.io/embed/job_app?for=coursera&token=" + x[1]
    newUrls.append(newUrl) #append the new URL to the list

websiteContent = [] #empty list for all the content
for i in range(len(newUrls)):
    page = requests.get(newUrls[i]) #get the content of the URL
    soup = BeautifulSoup(page.content, "html.parser") #parse the content
    title = soup.find('h1', class_="app-title") #find the title
    websiteContent.append(title.text) #append the title to the list
    company = soup.find('span', class_="company-name") #find the company name
    websiteContent.append(company.text) #append the company name to the list
    location = soup.find('div', class_="location") #find the location
    websiteContent.append(location.text) #append the location to the list
    content = soup.find('div', id="content") #find the content of the job, qualifications, etc.
    websiteContent.append(content.text) #append the content to the list

"""
the list websiteContent contains all the content of the job postings. 
The first element is the title, the second is the company name, the third is the location, and
the fourth is the content of the job posting. The fifth element is the title of the next job posting, and so on.
For example, websiteContent[0] would output the title of the first job posting and so on.
"""

