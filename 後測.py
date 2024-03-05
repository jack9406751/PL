#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("123.csv")
df.head()


# In[4]:


salaries = df['Income']
mean_Income = np.mean(salaries)
std_dev_Income = np.std(salaries)
print("Mean salary:", mean_Income)
print("Standard deviation of salary:", std_dev_Income)
plt.hist(salaries, bins=np.arange(np.mean(salaries)-10000, np.mean(salaries)+10000))
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# In[ ]:





# In[ ]:




