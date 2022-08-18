
from plyer import notification
import requests
from bs4 import BeautifulSoup

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10

    )

def getData(url):
    r = requests.get(url)
    return r.text    

if __name__ == "__main__":
    # notifyMe("Great", "Lets Fight with this virus")
    myHtmlData = getData('https://www.mohfw.gov.in/')

    
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    print(soup.prettify())
    myDataStr = ""
    for tr in soup.find_all('tbody')[1].find_all('tr'):
        myDataStr += tr.get_text()

    itemList =  myDataStr.split("\n\n")    

    for item in itemList:
        print(item.split('\n'))   


    # for tr in soup.find_all('tbody')[1].find_all('tr'):
    #     print(tr.get_text())
