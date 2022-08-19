#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')


# In[6]:


df= pd.read_csv("C:/Users/Farhan Anjum/Desktop/Datasets/Mall_Customers.csv")


# In[7]:


df.head()


# # Univariate Analysis

# In[9]:


df.describe()


# In[13]:


sns.distplot(df['Annual Income (k$)'])


# In[14]:


df.columns


# In[16]:


columns =['Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.distplot(df[i])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




