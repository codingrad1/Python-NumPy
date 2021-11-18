# Example 1:
# Integer indexing 
import numpy as np 
x = np.array([[1, 2], [3, 4], [5, 6],[7,8]]) 
print ("The array used for Integer Indexing is:")
print(x)

y = x[[0,1,2,3], [0,1,0,0]] 
print("The Output is:")
print(y) 



# Example 2:
# ndarray object containing corner elements.
import numpy as np 
x = np.array([[1,2,3], [4,6,8], [10,20,30], [92, 93, 94]]) 
print ('The array is:') 
print (x)

# picking the 1st and last row
rows = np.array([[0], [3]])

# picking 0 index and 2nd index element from each row
cols = np.array([[0, 2], [0, 2]])

y = x[rows, cols] 
   
print ('The corner elements of the array are:') 
print (y)



# Example 3:
#Boolean indexing 
import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 

print ('The array is:' )
print (x )
print ('\n')  

# Now print the items greater than 5 
print ('The items greater than 4 are:') 
print (x[x > 4])



#Example 4:
# Using NAN 
import numpy as np 

a = np.array([np.nan, 1, 21, np.nan, 3, 51, 64]) 

print("After omitting NaN the output array is :")
print (a[~np.isnan(a)])



# Example 5:
import numpy as np 
a = np.array([1, 2.5+6j, 5, 3+5j]) 
print (a[np.iscomplex(a)])
