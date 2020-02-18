#!/usr/bin/env python
# coding: utf-8

# # Coronavirus Tweets

# Objective: Show how topics change and migrate from place to place through time.
# 
# Step 1: Using conda, pull original tweets that discuss coronavirus. 

# In[1]:


import os
import tweepy as tw
import pandas as pd
import datetime
from datetime import datetime


# In[2]:


consumer_key= 'xx'
consumer_secret= 'xx'
access_token= 'xx'
access_token_secret= 'xxx'


# In[3]:


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# The date is irrelevant with such a large sample size combined with limits imposed by not having the premium twitter API access.

# In[4]:


search_words = "coronavirus" 
new_search = search_words + " -filter:retweets"
new_search
date_since = "2020-02-04"


# In[5]:



tweets = tw.Cursor(api.search,
                       q=new_search,
                       lang="en",
                       since=date_since).items(1000)


tweet_data = [[tweet.text, tweet.created_at, tweet.coordinates, tweet.place, tweet.favorite_count, tweet.retweet_count, tweet.user] for tweet in tweets]


# Pulled 10K tweets at a time for POC, Markdown will go faster with 1K tweets. 

# In[6]:


tweet_df = pd.DataFrame(data=tweet_data, 
                   columns=['tweet', "date", "coordinates", "place", "favorite count", "retweet count", "user data"]  )


# In[7]:


now = datetime.now() # current date and time
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")


date_time = now.strftime("%m%d%Y")
print(date_time)


# In[8]:



tweet_df.to_csv(date_time+'coronatweets.csv')


# Optimizations:
# 
# Twitter Developer API access for faster pulls and older tweets.
# 
# Run starting 1/1/2020 to show start of Coronavirus. 
