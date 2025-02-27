from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
  
# Request from the webpage  
myurl = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"  
  
  
uClient  = uReq(myurl)  
page_html = uClient.read()  
uClient.close()  
  
page_soup = soup(page_html, features="html.parser")  
  
#print(soup.prettify(containers[0]))  
  
#This variable held all html of webpage  
containers = page_soup.find_all("div",{"class": "_3O0U0u"})  
#container = containers[0]  
#print(soup.prettify(container))  
  
#price = container.find_all("div",{"class": "col col-5-12 _2o7WAb"})  
#print(price[0].text)  
 
#ratings = container.find_all("div",{"class": "niH0FQ"})  
#print(ratings[0].text)  
 
  
#print(len(containers))  
#print(container.div.img["alt"])  
  
# Creating CSV File that will store all data   
filename = "product.csv"  
f = open(filename,"w")  
  
headers = "Product_Name,Pricing,Ratings\n"  
f.write(headers)  
  
for container in containers:  
    product_name = container.div.img["alt"]  
    price_container = container.find_all("div", {"class": "col col-5-12 _2o7WAb"})  
    price = price_container[0].text.strip()  
    rating_container = container.find_all("div",{"class":"niH0FQ"})  
    ratings = rating_container[0].text  
  
    print("product_name:"+product_name)  
    print("price:"+price)  
    print("ratings:"+ str(ratings))  
  
    edit_price = ''.join(price.split(','))  
    sym_rupee = edit_price.split("?")  
    add_rs_price = "Rs"+sym_rupee[1]  
    split_price = add_rs_price.split("E")  
    final_price = split_price[0]  
  
    split_rating = str(ratings).split(" ")  
    final_rating = split_rating[0]  
  
    print(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
    f.write(product_name.replace(",", "|")+","+final_price+","+final_rating+"\n")  
    f.close()  