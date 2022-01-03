import numpy as np
#%matplotlib inline
import matplotlib.pyplot as plt
from scipy import sparse
import mglearn
from IPython.display import display
 

import sys
print("Python version:", sys.version)


import pandas as pd
print("pandas version:", pd.__version__)

 

import matplotlib
print("matplotlib version:", matplotlib.__version__)


print("NumPy version:", np.__version__)

 

import scipy as sp
print("SciPy version:", sp.__version__)

 

import IPython
print("IPython version:", IPython.__version__)

 

import sklearn
print("scikit-learn version:", sklearn.__version__)



x = np.array([[1, 2, 3], [4, 5, 6]])

print("x:\n{}".format(x))

 

# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(4)
print("NumPy array:\n", eye)

 

 

# Convert the NumPy array to a SciPy sparse matrix in CSR format
# Only the nonzero entries are stored

sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse CSR matrix:\n", sparse_matrix)


 

data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print("COO representation:\n", eye_coo)



 

# Generate a sequence of numbers from -10 to 10 with 100 steps in between
x = np.linspace(-10, 10, 100)
# Create a second array using sine
y = np.sin(x)
# The plot function makes a line chart of one array against another
plt.plot(x, y, marker="^")

 

# create a simple dataset of people
data = {'Name': ["John", "Anna", "Peter", "Linda"],
        'Location' : ["New York", "Paris", "Berlin", "London"],
        'Age' : [24, 13, 53, 33]
       }

data_pandas = pd.DataFrame(data)

 

 

# IPython.display allows "pretty printing" of dataframes
# in the Jupyter notebook

display(data_pandas)


 

# Select all rows that have an age column greater than 30
display(data_pandas[data_pandas.Age > 30])

 

plt.show()

