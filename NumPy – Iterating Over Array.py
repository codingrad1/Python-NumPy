# Example 1:
# nditer object

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)

print ('Original array is:')
print (a)
print ('\n')

print ('Modified array is:')
for x in np.nditer(a):
   print (x)



# Exmaple 2:
# Transpose of array

import numpy as np 
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a = a.reshape(3,4) 
   
print ('Original array is:')
print (a) 
print ('\n')  
   
print ('Transpose of the original array is:') 
b = a.T 
print (b) 
print ('\n')  
   
print ('Modified array is:') 
for x in np.nditer(b): 
   print (x)



# Example 3:
# Iteration order

import numpy as np
a = np.arange(10,100,8)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

print ('Transpose of the original array is:')
b = a.T
print (b)
print ('\n')

print ('Sorted in C-style order:')
c = b.copy(order = 'C')
print (c)
for x in np.nditer(c):
   print (x)

print ('\n')

print ('Sorted in F-style order:')
c = b.copy(order = 'F')
print (c)
for x in np.nditer(c):
   print (x)



# Exmaple 4

import numpy as np 
a = np.arange(10,100,8) 
a = a.reshape(3,4) 

print ('Original array is:' )
print (a )
print ('\n' ) 

print ('Sorted in C-style order:' )
for x in np.nditer(a, order = 'C'): 
   print (x)  
print ('\n') 

print ('Sorted in F-style order:' )
for x in np.nditer(a, order = 'F'): 
   print (x)


   
# Example 5:
# Modifying Array Values

import numpy as np
a = np.arange(10,100,8)
a = a.reshape(3,4)
print ('Original array is:')
print (a)
print ('\n')

for x in np.nditer(a, op_flags = ['readwrite']):
   x[...] = 2*x
print ('Modified array is:')
print (a)



# Example 6:
# one-dimensional array corresponding to each column is traversed by the iterator

import numpy as np 
a = np.arange(10,100,8) 
a = a.reshape(3,4) 

print ('Original array is:' )
print (a) 
print ('\n'  )

print ('Modified array is:' )
for x in np.nditer(a, flags = ['external_loop'], order = 'F'):
   print (x)



# Example 7
# Broadcasting Iteration

import numpy as np 
a = np.arange(10,100,8) 
a = a.reshape(3,4) 

print ('First array is:' )
print( a) 
print ('\n')  

print ('Second array is:' )
b = np.array([1, 2, 3, 4], dtype = int) 
print (b ) 
print ('\n') 

print ('Modified array is:' )
for x,y in np.nditer([a,b]): 
   print( "%d:%d" % (x,y))
