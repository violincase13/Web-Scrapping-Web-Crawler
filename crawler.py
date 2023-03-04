import requests
from bs4 import BeautifulSoup
 
urls = 'https://www.mai.gov.ro'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')
 
# opening a file in write mode
f = open("links.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("a"):
   data = link.get('href')
   f.write(data)
   f.write("\n")
 
f.close()
