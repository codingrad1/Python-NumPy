#!/usr/bin/env python
# coding: utf-8

# In[28]:


#arange function
import numpy as np 
x = np.arange(6) 
print (x)


# In[29]:


import numpy as np 
# dtype set to float
x = np.arange(6, dtype = float)
print (x)


# In[30]:


# start and stop parameters set 
import numpy as np 
x = np.arange(10,30,2) 
print (x)


# In[31]:


import numpy as np  
a = np.arange(5,50,2,int)  
print("The array over the given range is ",a) 


# In[32]:


#linspace function
import numpy as np  
x = np.linspace(10, 30, 5)  
print("The array over the given range is ",x)  


# In[33]:


# endpoint set to false 
import numpy as np 
x = np.linspace(10,30, 5, endpoint = False) 
print (x)


# In[34]:


# find retstep value 
import numpy as np 

x = np.linspace(1,3,5, retstep = True) 
# retstep here is 0.5
print (x)


# In[35]:


#logspace function
import numpy as np 
# default base is 10 
a = np.logspace(10, 20, num = 10) 
print (a)


# In[36]:


# set base of log space to 2 and endpoint is true
import numpy as np 
a = np.logspace(1, 10, num = 10,base = 2, endpoint = True)  
print (a)

