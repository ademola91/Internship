#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import numpy as np


# In[2]:


# Q1. A python program to display all the header tags from wikipedia.org and make data frame


# In[3]:


page1 = requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[4]:


soup1 = BeautifulSoup(page1.content)


# In[5]:


header_all = []
for i in soup1.find_all('h2',class_="mp-h2"):
    header_all.append(i.text)


# In[6]:


dfwiki = pd.DataFrame({'Header Tags':header_all})


# In[7]:


dfwiki


# In[8]:


# Q2.A python program to display list of respected former presidents of India(i.e. Name , Term of office)


# In[9]:


page2 = requests.get('https://presidentofindia.nic.in/former-presidents.htm')


# In[11]:


# Names of former Presidents
soup2 = BeautifulSoup(page2.content)
name_all = []
for i in soup2.find_all('div',class_="presidentListing"):
    name_all.append(i.text.split('\n')[1])


# In[13]:


new_names = [re.sub(r'\(.*?\)', '', i).strip() for i in name_all]


# In[14]:


# Term of office
term_all = []
for i in soup2.find_all('div',class_="presidentListing"):
    term_all.append(i.text.split('\n')[2:3])


# In[15]:


updated_terms = []

for term in term_all:
    updated_term = term[0].replace('Term of Office: ', '').strip()
    updated_terms.append(updated_term)


# In[17]:


df_pres = pd.DataFrame({'Name':new_names, 'Term':updated_terms})
df_pres


# In[18]:


# Q3a Top 10 ODI teams in men’s cricket along with the records for matches, points and rating


# In[19]:


page3 = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')


# In[20]:


soup3 = BeautifulSoup(page3.content)


# In[34]:


Leader_team = soup3.find('tr' ,class_='rankings-block__banner')
leader= Leader_team.text.split('\n')[4:11]
leader=([leader [i] for i in (0,3,4,6)])
leader[-1] = leader[-1].strip()


# In[27]:


other_oditeams1 = []
for i in soup3.find_all('tr', class_="table-body"):
    other_oditeams1.append(i.text.split('\n')[4:10])


# In[28]:


odt3=([other_oditeams1 [i] for i in (0,1,2,3,4,5,6,7,8)])


# In[29]:


odt3


# In[32]:


for i in odt3:
    del i[1:2]


# In[35]:


odi_team3 = leader + [item for sublist in odt3 for item in sublist]


# In[36]:


odi_team3


# In[37]:


odi_tm4 = [odi_team3[i:i+4] for i in range(0, len(odi_team3), 4)]
dfteam2 = pd.DataFrame(odi_tm4, columns=['Country', 'Matches', 'Points', 'Rating'])
dfteam2


# In[38]:


# Q6 Write a python program to scrape the details of most downloaded articles from AI in last 90


# In[39]:


page6 = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')


# In[40]:


soup6 = BeautifulSoup(page6.content)


# In[41]:


#Paper Title


# In[42]:


Paper_title = []
for i in soup6.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    Paper_title.append(i.text)


# In[43]:


#Authors


# In[44]:


Paper_authors = []
for i in soup6.find_all('span', class_="sc-1w3fpd7-0 dnCnAO"):
    Paper_authors.append(i.text)


# In[45]:


#Published Date


# In[46]:


Published_dates = []
for i in soup6.find_all('span', class_="sc-1thf9ly-2 dvggWt"):
    Published_dates.append(i.text)


# In[47]:


#Paper URL


# In[52]:


Paper_URL = []
for i in soup6.find_all('a', class_="sc-5smygv-0 fIXTHm"):
    Paper_URL.append(i.text)


# In[56]:


print(len(Paper_title),len(Paper_authors),len(Published_dates))


# In[55]:


dfq6= pd.DataFrame({'Paper Tile':Paper_title,'Paper Authors':Paper_authors,'Published_dates':Published_dates})


# In[57]:


dfq6


# In[ ]:




