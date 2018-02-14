import requests
import os
import time
from bs4 import BeautifulSoup, Comment
from os.path  import basename
from datetime import datetime

def job():
    # download required page
    page = requests.get("https://bingwallpaper.com")
    soup = BeautifulSoup(page.content, 'html.parser')

    # get rid of comments in html
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]

    today = datetime.now()
    filename = str(today.day)+'-'+str(today.month)+'-'+str(today.year)+'.png'

    image = soup.select(".cursor_zoom img")
    url = image[0]['src']

    # download image and save
    with open(filename,"wb") as f:
        f.write(requests.get(url).content)
        
    # change desktop background
    os.system("gsettings set org.gnome.desktop.background picture-uri file:////home/foobar/PythonScripts/" + filename)
    return

while True:
    now = datetime.now()
    if(now.hour==10 and now.minute==0 and now.second==0):
        job()
        break
    time.sleep(60) # wait one minute

sys.exit()