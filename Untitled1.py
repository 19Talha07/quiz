#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[20]:


from numpy import array
from numpy import ndarray


# In[21]:


array1: ndarray = array([
    [7,-88,11],
    [-3,7,12],
    [-4,5,-99],
    [3,8,-12]
])
   


# In[22]:


array1


# In[23]:


array1.shape


# In[24]:


np.min(array1)


# In[25]:


array1[0,1] = 101


# In[26]:


array1


# In[27]:


array1[2,2] = 0


# In[28]:


array1


# In[34]:


array1.reshape(1,12)


# In[39]:


qmarks = np.load(r"C:\Users\musta\OneDrive\Masaüstü\marks (1).npy") 


# In[40]:


qmarks


# In[41]:


len(qmarks)


# In[42]:


np.max(qmarks)


# In[43]:


np.min(qmarks)


# In[45]:


np.median(qmarks)


# In[46]:


np.mean(qmarks)


# In[47]:


np.std(qmarks)


# In[48]:


np.var(qmarks)


# In[49]:


np.ptp(qmarks)


# In[53]:


x = np.arange(0,15)
y = (np.sin(x)*x**1/2)/(x**2+1)


# In[56]:


import matplotlib.pyplot as plt


# In[67]:


plt.plot(x,y, "red")
plt.axvline("blue")
plt.axhline("b")


# In[70]:


array2: ndarray = array([
    [7,-8,11],
    [-4,5,1],
    [3,8,-2]
])


# In[71]:


array2


# In[72]:


np.linalg.det(array2)


# In[73]:


np.linalg.eigvals(array2)


# In[74]:


np.linalg.inv(array2)


# In[75]:


np.linalg.cond(array2)


# In[76]:


np.linalg.norm(array2)


# In[77]:


matris_A: ndarray = array([
    [1,2],
    [4,5]
])


# In[78]:


matris_B: ndarray = array([
    [4,5]
])


# In[79]:


matris_A


# In[82]:


matris_B


# 

# In[83]:


matris_A * matris_B


# In[85]:


matris_A_2: ndarray = array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

matris_B_2: ndarray = array([
    [2],
    [0],
    [-1]
])


# In[88]:


np.linalg.solve(matris_A_2,matris_B_2)


# In[ ]:




