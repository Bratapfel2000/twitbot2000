# twitbot2000, version 3.5 written in python 3.6.6
# will tweet a scraped word from another page and assess it with a
# german adjective, going from "gut" to "schlecht" etc
# and post it on its own on twitter

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from bs4 import BeautifulSoup
import requests
from time import sleep
import time
import random
import schedule

#scraping a specific word from a website
source = requests.get('---insert website----').text
soup = BeautifulSoup(source, 'lxml')
eins = soup.find(id="---insert---")  #here could also be "dev" or anything else instead of "id"
zwei = eins.find_all(class_="---insert---") #insert class name of word
drei = zwei[0]
#print(drei.text)  #this ist just to check the code


#creates a list of words (here german adjectives)
a = ["gut", "schlecht", "voll gut", "ziemlich fuer den Arsch", "naja", "geht so", "spitzenklasse",
     "erste Sahne", "zweite Sahne", "voll Zehlendorf", "unangenehm", "gar nicht mal so gut",
     "besser", "schlechter", "hipstermaessig"]
#print(random.choice(a))    #this ist just to check the code



#import twitter_credentials, need to open twitter account with developer options
consumer_key = '---insert key, careful:chars need to stay---'
consumer_secret = '---insert secret, careful:chars need to stay---'
access_token = '---insert token, careful:chars need to stay---'
access_token_secret = '---insert token secret, careful:chars need to stay---'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

user = api.me()
#print (user.name)  #this ist just to check the code


###this is to tweet pictures on twitter
##api-update_with_media('pic.job', 'Hello world with pic')


###this code prints all 5 seconds a status update, 3 times in total
##total_breaks = 3
##break_count = 0
##
##while(break_count < total_breaks):
##    time.sleep(5)
##    api.update_status(time.ctime() + drei.text + " ist " + random.choice(a))
##    break_count= break_count + 1


#this is doing the status update on twitter.
#below three options to tweet by minute, hour or daily "at"
def job():
   api.update_status(drei.text + " ist " + random.choice(a) + ".")
   
schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("12:35").do(job)

while 1:
   schedule.run_pending()
   time.sleep(1)

