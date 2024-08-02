from bs4 import BeautifulSoup  
import requests  
  
url="https://www.javatpoint.com/"  
  
# Make a GET request to fetch the raw HTML content  
html_content = requests.get(url).text  
  
# Parse the html content  
soup = BeautifulSoup(html_content, "html5lib")  
print(soup.prettify()) # print the parsed data of html  
print(soup.title)