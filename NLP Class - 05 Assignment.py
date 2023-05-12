#!/usr/bin/env python
# coding: utf-8

# # Assignment
# Here is some dummy text
# - 'This is an example text, i am going to write anything here, use this text as your example'
# - 'You can use this text to convert into vectors'
# - 'Do remember to clean up the text before you start any processing'
# - 'Once you are done converting the text into numbers(vectors), do a shinchan dance'
# 
# # Question 1
# Write code that will these four sentences into count vectors.
# 
# # Question 2
# Write code that will these four sentences into tf-idf vectors.

# In[1]:


# I am writing some code as hints, feel free to solve it however you want
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:





# In[1]:


from sklearn.feature_extraction.text import CountVectorizer


# In[2]:


import pandas 


# In[3]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[4]:


x = (['This is an example text, i am going to write anything here, use this text as your example'
'You can use this text to convert into vectors'
'Do remember to clean up the text before you start any processing'
'Once you are done converting the text into numbers(vectors), do a shinchan dance'])


# In[13]:


vectorizer = CountVectorizer()


# In[14]:


vectorizer.fit(x)


# In[15]:


vector = vectorizer.transform(x)


# In[16]:


vector


# In[18]:


count = pandas.DataFrame(vector.toarray(), columns = vectorizer.get_feature_names_out())


# In[19]:


count


# In[14]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[15]:


vector = TfidfVectorizer()


# In[16]:


vector.fit(x)


# In[17]:


vector.get_feature_names_out()


# In[23]:


count_2 = vector.transform(x)


# In[24]:


count_2.toarray()


# In[ ]:




