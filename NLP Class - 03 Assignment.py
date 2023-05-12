#!/usr/bin/env python
# coding: utf-8

# # Question
# Create a python function that takes a string as an input and returns a string without stopwords as an output. 

# In[77]:


# I am writing some code as hints, feel free to solve it however you want
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[78]:


stop_words = stopwords.words("english")


# In[ ]:





# In[1]:


import nltk


# In[2]:


a = "I'm just a little bit caught in the middle. Life is a maze and love is a riddle."


# In[3]:


from nltk.tokenize import word_tokenize


# In[4]:


a = nltk.word_tokenize(a)


# In[5]:


a


# In[6]:


from nltk.corpus import stopwords


# In[7]:


stop_words = stopwords.words("english")


# In[8]:


stop_words


# In[9]:


for i in a:
    if i in stop_words:
        pass
    else:
        print(i)

