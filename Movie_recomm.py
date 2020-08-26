from bs4 import BeautifulSoup as bs 
import re 
import requests as req
from win10toast import ToastNotifier
  
def main(emotion): 
  
    if(emotion == "Sad"): 
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "Anger"): 
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "Fear"): 
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
        
    elif(emotion == "Enjoyment"): 
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    elif(emotion == "Surprise"): 
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    response = req.get(url) 
    data = response.text 
  
    soup = bs(data, "lxml") 
  
    title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    return title 

  

  
if __name__ == '__main__': 
  
    emotion = input("Enter Your emotion: ") 
    a = main(emotion) 
    count = 0
for i in a: 
            tmp = str(i).split('>') 
  
            if(len(tmp) == 3): 
                print(tmp[1][:-3]) 
  
            if(count > 27): 
                break
            count+=1
notifier = ToastNotifier()
message = "Suggested Movie is-" + str(tmp[1][:-3])
notifier.show_toast(msg=message,duration=20)