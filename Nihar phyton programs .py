#!/usr/bin/env python
# coding: utf-8

# In[13]:


print(2+3)


# In[14]:


print(5+2)


# In[17]:


phrase ="Girrafe academy"
print(phrase.upper().isupper())


# In[18]:


phrase ="Girrafe academy"
print(len(phrase))


# In[30]:


phrase="Giraffe academy"
print(phrase.index("acad"))


# In[31]:


print(3*(4+5))


# In[32]:


print(10%3)


# In[33]:


my_num=5
print(my_num)


# In[36]:


my_num=5
print(str(my_num)+ "my favoriate number")


# In[38]:


my_num=-5
print(abs(my_num))


# In[1]:


x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


# In[7]:


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


# In[8]:


import matplotlib.pyplot as plt

import seaborn as sns; sns.set()

import numpy as np

from sklearn.datasets.samples_generator import make_blobs

get_ipython().run_line_magic('matplotlib', 'inline')

X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

plt.scatter(X[:, 0], X[:, 1], s=50);


# In[9]:


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)

kmeans.fit(X)

y_kmeans = kmeans.predict(X)
y_kmeans


# In[3]:


num1=input("enter a number:")
num2=input("enter a another number")
result=int(num1)+int(num2)

print(result)


# In[4]:


num1=input("enter a number:")
num2=input("enter a another number")
result=float(num1)+float(num2)

print(result)


# In[ ]:



    

