# Example 1: Slicing 

#slicing the sequence 
import numpy as np 
a = np.arange(10) 
s = slice(2,9,2) 
print (a[s])



# Example 2:

#using only one parameter 
import numpy as np 
a = np.arange(10) 
b = a[2:9:2] 
print (b)



Example 3:
  
# slice single item 
import numpy as np
a = np.arange(10) 
b = a[5] 
print (b)



# Example 4:

# slice items starting from index 
import numpy as np 
a = np.arange(10) 
print (a[3:])



# Example 5:

# slice items between indexes 
import numpy as np 
a = np.arange(10) 
print (a[3:6])



# Example 6:

import numpy as np 
a = np.array([[1,2,3],[3,4,5],[4,5,6],[5,6,7]]) 
print (a)  

# slice items starting from index
print ('Now we will slice the array from the index a[2:]:' )
print (a[2:])



# Example 7:

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

