# Import libraries
import requests
from bs4 import BeautifulSoup
import os

# URL from which pdfs to be downloaded
url = "https://www.mai.gov.ro/informatii-publice/achizitii-publice/"
  
# Requests URL and get response object
response = requests.get(url)
  
# Parse text obtained
soup = BeautifulSoup(response.text, 'html.parser')
  
# Find all hyperlinks present on webpage
links = soup.find_all('a')
  
i = 0
  
# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        print("Downloading file: ", i)
  
        # Get response object for link
        response = requests.get(link.get('href'))

        os.makedirs('/home/flavia/Desktop/crawler/pdf', exist_ok=True)
        with open(os.path.join('/home/user/Desktop/crawler/pdf', "pdf"+str(i)+".pdf"), mode = 'wb') as f:
            f.write(response.content)
            f.close
            print("File ", i, " downloaded")
  
        # Write content in pdf file
        #pdf = open("pdf"+str(i)+".pdf", 'wb')
        #pdf.write(response.content)
        #pdf.close()
        #print("File ", i, " downloaded")
  
print("All PDF files downloaded")
