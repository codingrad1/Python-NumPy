# Example 1:
# Aritnmatic operations

import numpy as np 
a = np.array([2,4,6,8]) 
b = np.array([10,20,30,40]) 
c = a * b 
print (c)



# Example 2:
# Broadcasting 

import numpy as np 
a = np.array([[0.0,0.0,0.0],[10.0,10.0,10.0],[20.0,20.0,20.0],[30.0,30.0,30.0]]) 
b = np.array([1.0,2.0,3.0])  
   
print ('First array:') 
print( a )
print ('\n' ) 
   
print ('Second array:' )
print( b )
print ('\n')  
   
print ('First Array + Second Array' )
print (a + b)
