# Example 1: numpy.arange function

#arange function
import numpy as np 
x = np.arange(6) 
print (x)


import numpy as np 
# dtype set to float
x = np.arange(6, dtype = float)
print (x)


# start and stop parameters set 
import numpy as np 
x = np.arange(10,30,2) 
print (x)


import numpy as np  
a = np.arange(5,50,2,int)  
print("The array over the given range is ",a) 


# Example 2: numpy.linspace function

#linspace function
import numpy as np  
x = np.linspace(10, 30, 5)  
print("The array over the given range is ",x)  


# endpoint set to false 
import numpy as np 
x = np.linspace(10,30, 5, endpoint = False) 
print (x)


# find retstep value 
import numpy as np 
x = np.linspace(1,3,5, retstep = True) 
# retstep here is 0.5
print (x)


Example 3: numpy.logspace function

#logspace function
import numpy as np 
# default base is 10 
a = np.logspace(10, 20, num = 10) 
print (a)


# set base of log space to 2 and endpoint is true
import numpy as np 
a = np.logspace(1, 10, num = 10,base = 2, endpoint = True)  
print (a)

