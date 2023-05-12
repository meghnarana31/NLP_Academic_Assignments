#!/usr/bin/env python
# coding: utf-8

# # Question
# Create a python function that takes a string as an input and returns a string with every word lemmatized as an output. 

# In[6]:


# I am writing some code as hints, feel free to solve it however you want
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


# In[7]:


lemmatizer.lemmatize('Something')


# In[8]:


lemmatizer.lemmatize('running')


# In[ ]:





# In[17]:


import nltk


# In[18]:


from nltk.tokenize import word_tokenize


# In[19]:


a = "Be an encourager. The world has plenty of critics already."


# In[20]:


a = nltk.word_tokenize(a)


# In[24]:


from nltk.corpus import stopwords


# In[25]:


stop_words = stopwords.words("english")


# In[27]:


x = []
for i in a:
    if i in stop_words:
        pass
    else:
        print(i)
    x.append(i) 


# In[33]:


x


# In[28]:


from nltk.stem import WordNetLemmatizer


# In[31]:


lemmatizer = WordNetLemmatizer()


# In[35]:


for i in x:
    print(i + " > " + lemmatizer.lemmatize(i))

