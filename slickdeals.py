
# coding: utf-8

# In[1]:

import urllib3
from bs4 import BeautifulSoup
import re
import pandas as pd

os.chdir("C:\\Users\\mohantyk\\lab\\scrape")

with open('p.txt', 'r') as myfile:
    pwd=myfile.read().replace('\n', '')

# In[2]:

# specify the url
quote_page = 'http://www.slickdeals.net'


# In[41]:

s_list=['dell']


# In[42]:

http = urllib3.PoolManager()


# In[43]:

# query the website and return the html to the variable ‘page’
response=http.request('GET', quote_page)


# In[44]:

soup = BeautifulSoup(response.data,"lxml")


# In[45]:

url_list=[]
title_list=[]
for a in soup.find_all('a', href=True):
    x=a['href']
    for s in s_list:
        if re.search('^/f.*'+s,x):
            url='https://slickdeals.net'+a['href']
            url_list.append(url)
            title_list.append(a['title'])
            #print(url)


# In[46]:

url_list,title_list


# In[37]:

data=pd.DataFrame({'title':title_list,'url':url_list})


# In[38]:

#from IPython.display import HTML
#HTML(data.to_html())


# In[39]:

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[40]:

if data.shape[0] > 0:
    me = "kirtiraj.careers@gmail.com"
    you = "kr.mohanty@gmail.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Slickdeals Alert"
    msg['From'] = me
    msg['To'] = you
    html = data.to_html()
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('kirtiraj.careers', pwd)
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
    print('email sent')


# In[ ]:



