from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from math import ceil
from time import sleep
from sys import exit
import time
import re
import csv
import codecs
import pickle
import os


KEYWORD = 'sunfrog tee '
Output= open('FileToUp.csv', 'w')

browser = webdriver.Firefox()
browser.get('https://www.pinterest.com/')
# pickle.dump(browser.get_cookies() , open("cookies.pkl","wb"))
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)


print "START"

for ID in range (0,30):
    if ID == 0:
        NICHE = ""    
    elif ID == 1:
        NICHE = "therapy"
    elif ID == 2:
        NICHE = "automotive"
    elif ID == 3:
        NICHE = "Drinking"
    elif ID == 4:
        NICHE = "Faith"
    elif ID == 5:
        NICHE = "Fitness"
    elif ID == 6:
        NICHE = "Funny"
    elif ID == 7:
        NICHE = "Gamer"
    elif ID == 8:
        NICHE = "Geek-Tech"
    elif ID == 9:
        NICHE = "Hobby"
    elif ID == 10:
        NICHE = "Holidays"
    elif ID == 11:
        NICHE = "Jobs"
    elif ID == 12:
        NICHE = "LifeStyle"
    elif ID == 13:
        NICHE = "Movies"
    elif ID == 14:
        NICHE = "Music"
    elif ID == 15:
        NICHE = "Names"
    elif ID == 16:
        NICHE = "Outdoor"
    elif ID == 17:
        NICHE = "Pet"
    elif ID == 18:
        NICHE = "Political"
    elif ID == 19:
        NICHE = "Sports"
    elif ID == 20:
        NICHE = "States"
    elif ID == 21:
        NICHE = "TV Shows"
    elif ID == 22:
        NICHE = "Zombies"
    elif ID == 23:
        NICHE = "Yoga"
    elif ID == 24:
        NICHE = "Christmas"
    elif ID == 25:
        NICHE = "Marvel"
    elif ID == 26:
        NICHE = "Happy New Year"
    elif ID == 27:
        NICHE = "Skiing"
    elif ID == 28:
        NICHE = "Camp"
    else:
        os._exit(1)

    print "ID: " + str(ID)
    ID+=1


    browser.get('https://www.pinterest.com/search/pins/?q=' + KEYWORD + NICHE + '&rs=typed&term_meta%5B%5D=tees%7Ctyped')

    for i in range(1,30):
        print i
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)

    source = BeautifulSoup(browser.page_source, "html.parser")

    for a in source.find_all('a', attrs={'rel' : 'nofollow'}):
        if "sunfrog" in a['href']:
            link = a['href'].split('?')
            if "sunfrog" not in link[0]:
                link = 'http' + link[1].split('http')[1]
            else:
                link = link[0]
            #print link

            Output.write(link + '\n')




browser.quit()
Output.close()   
