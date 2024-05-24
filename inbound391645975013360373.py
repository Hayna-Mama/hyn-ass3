# Save and Writing Files using Numpy

# Example 1: Saving a single array

import numpy as np

array1 = np.array([2, 4, 6, 8, 10])
np.save('array1.npy', array1)

#Example 2: Saving multiple arrays

import numpy as np

array2 = np.array([5, 10, 15])
array3 = np.array([50, 100, 150])
np.savez('arrays.npz', array2=array2, array3=array3)


#Example 3: Saving ang array to a text file

import numpy as np

array4 = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])
np.savetxt('array4.txt', array4)




# Load Data from Files using NumPy

#Example 1: Loading a single array from a .npy file

import numpy as np

loaded_array1 = np.load('array1.npy')
print(loaded_array1)


# Example 2: Loading multiple arrays from a .npz file

import numpy as np

loaded_data = np.load('arrays.npz')
loaded_array2 = loaded_data['array2']
loaded_array3 = loaded_data['array3']
print(loaded_array2)
print(loaded_array3)


# Example 3: Loading an array from a text file

import numpy as np

loaded_array4 = np.loadtxt('array4.txt')
print(loaded_array4)

 


