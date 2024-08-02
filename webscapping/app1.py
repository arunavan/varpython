import bs4  
import requests  
  
#Creating the requests  
  
res = requests.get("https://en.wikipedia.org/wiki/Machine_learning")  
print("The object type:",type(res))  
  
 
soup = bs4.BeautifulSoup(res.text,'html5lib')  
#print("The object type:",type(soup) )

soup.select('.mw-headline')  
for i in soup.select('.mw-headline'):  
    print(i.text,end = ',')  