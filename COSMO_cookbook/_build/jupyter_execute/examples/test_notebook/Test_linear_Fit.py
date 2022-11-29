#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt


# In[2]:


X = np.random.rand(10000)*400
Y = 0.1*X+10.1
Y_p = Y + np.random.randn(10000)*1.5


# In[3]:


p = np.polyfit(X,Y_p,deg=1)


# In[4]:


p


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams.update({'font.size': 25})
fig , ax =plt.subplots(1,figsize=(10,8))
ax.set_ylabel('Y')
ax.set_xlabel('X')

ax.plot(X,Y_p,'.')
ax.plot(X,p[0]*X+p[1],lw=5,ls='-.',c='black',label='{:3.2f}*X+{:3.2f}'.format(p[0],p[1]))
ax.legend()


# In[ ]:




