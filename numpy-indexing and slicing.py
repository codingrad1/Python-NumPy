#!/usr/bin/env python
# coding: utf-8

# In[6]:


#slicing the sequence 
import numpy as np 
a = np.arange(10) 
s = slice(2,9,2) 
print (a[s])


# In[9]:


#using only one parameter 
import numpy as np 
a = np.arange(10) 
b = a[2:9:2] 
print (b)


# In[11]:


# slice single item 
import numpy as np
a = np.arange(10) 
b = a[5] 
print (b)


# In[13]:


# slice items starting from index 
import numpy as np 
a = np.arange(10) 
print (a[3:])


# In[16]:


# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print (a[3:6])


# In[21]:


import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6],[5,6,7]]) 
print (a)  

# slice items starting from index
print ('Now we will slice the array from the index a[2:]:' )
print (a[2:])


# In[27]:


# array to begin with 
import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6],[5,6,7]]) 

print ('Our array is:') 
print (a) 
print ('\n')  

# this returns array of items in the second column 
print ('The items in the second column are:')  
print (a[...,1]) 
print ('\n')  

# Now we will slice all items from the second row 
print ('The items in the second row are:' )
print (a[1,...])
print ('\n')

# Now we will slice all items from column 1 onwards 
print ('The items column 1 onwards are:') 
print (a[...,1:])

