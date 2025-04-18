"""NUMERICAL COMPUTING WITH NUMPY 
The "data" in Data Analysis refers to numerical data e.g stock prices, sales figures, 
sports scores etc. The Numpy library provides specialized data structures, 
functions and other tools for numerical computing in Python. Let's work through
an example to see why & how to use Numpy for working with numerical data.""" 

"""Let's say we want to use climate data like temperature, rainfall and humidity in a 
region to determine if the region is well suited for growing apples. A really 
simple approach for doing this would be to formulate the relationship between the annual 
yield of apples (tons per hectare) and the climatic conditions like the average 
temperature (in degrees Fahreheit), rainfall (in millimeters) & average humidity (in percentage) 
as a linear equation. 

yield_of_apples = w1 * temperature + w2 * rainfall + w3 * humidity 

We're expressing the yield as a weighted sum of the temperature, rainfall and humidity. 
Obviously, this is an approximation, since the actual relationship[ may not necessarily 
be linear. But simple linear model like this often works well in practice.
"""

w1, w2, w3 = 0.3, 0.2, 0.5 

"""Given some climatic data for a region, we can now predict the yield of apples in 
a region might look like.""" 
kanto_temp = 73 
kanto_rainfall = 67 
kanto_humidty = 43 

"""These variables can now be substituted into the linear equation to predict 
the yield of apples in that region."""

kanto_yield_apples = kanto_temp * w1 + kanto_rainfall * w2 + kanto_humidty * w3 

#print(f"The expected yield of apples in Kanto region is {kanto_yield_apples} tons per hectare")

"""To make it slightly easier to perform the above computation for multiple 
regions, we can represent the climatic data for each region as a vector. i.e a list of numbers"""
kanto = [73, 67, 43] 
johto = [91, 88, 64]
hoenn = [87, 134, 58] 
sinnoh = [102, 43, 37]
unova = [69, 96, 70] 

"""The three numbers in each vector represent the temperature, rainfall and humdity data 
respectively. The set of weights to be used in the formula can also be represented as a vector
"""  
weights = [w1, w2, w3] 

"""We can now write a function crop_yield to calculate the yield of apples (or any other crop)
given the climatic data and the respective weights
""" 
def crop_yield(region, weights): 
    result = 0 
    for x, w in zip(region, weights): 
        result += x * w 
    return result  

#print(crop_yield(kanto, weights))
#print(crop_yield(johto, weights))
#print(crop_yield(sinnoh, weights)) 

"""Going from Python Lists to Numpy Arrays 
The calculation performed by the crop_yield (element-wise multiplication of two vectors, and 
taking a sum of the results) is called the dot product of the two vectors. 

The nbumpy library provides a built-in function to perform the dot product of 
two vectors. However, the lists must be converted to numpy arrays before we can 
perform the operation. To begin, let's import the numpy module. It is common 
practice to import numpy with the alias np. 
""" 
import numpy as np

"""Numpy arrays can be created using the np.array function.1
"""
kanto = np.array([73, 67, 43])
weights = np.array([w1, w2, w3]) 

#print(type(kanto)) 
#print(type(weights)) 

"""Just like lists, Numpy arrays support the indexing notation []""" 
#print(weights[0])

"""Operating on Numpy Arrays 
We can compute the dot product of the two vectors using the np.dot function
"""
#help(np.dot) 
kanto_yield_apples = np.dot(kanto, weights)
#print(kanto_yield_apples) 

"""We can achieve the same result with lower level operations supported by 
Numpy arrays; performing an element-wise multiplication and calculating the sum 
of the resulting numbers.""" 
kanto_yield_apples = (kanto * weights).sum() 
#print(kanto_yield_apples)

"""The * operator performs an element-wise multiplication of the two 
arrays (assuming they have the same size), and the sum method calculates the 
sum of the numbers in an array.""" 
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6]) 

#print(arr1 * arr2)
#print(arr2.sum()) 

"""Benefits of using Numpy arrays 
There are a couple of important benefits of using Numpy arrays instead 
of Python lists for operating on numerical data. 

* Ease of use: You can write small, concise and intuitive mathematical expressions 
like (kanto * weights).sum() rather than using loops & custom functions like crop_yield. 
* Performance: Numpy operatons and functions are implemented internally in C++, which 
makes them much faster using Python statements & loops which are interpreted at the runtime.

Here's a quick comparison of dot products done of vectors with a million elements
using Python loops vs. Numpy arrays.""" 
from timeit import default_timer as timer 
def print_duration(start_time, end_time): 
    duration = end_time - start_time 
    print(f"\33[33mCompleted in {duration} minutes")
# Python lists
arr1 = list(range(1_000_000)) 
arr2 = list(range(1_000_000, 2_000_000)) 

# Numpy arrays 
arr1_np = np.array(arr1)
arr2_np = np.array(arr2) 

result = 0 
start_time = timer()
for x1, x2 in zip(arr1, arr2):
    result += x1*x2 
end_time = timer() 
#print(result)
#print_duration(start_time, end_time) 

start_time = timer()
result = np.dot(arr1_np, arr2_np)
end_time = timer() 
#print(result)
#print_duration(start_time, end_time) 

"""As you can see, using np.dot is 100 times faster than using for a for loop.
This makes Numpy especially useful while working with really large datasets with 
tens of thousands or millions of data points""" 


"""Multi-dimensional Numpy arrays
We can now go one step further, and represent the climatic data for all the regions
together using a single 2-dimensional Numpy array
"""
climatic_data = np.array([[73, 67, 43], 
                          [91, 88, 64], 
                          [87, 134, 58], 
                          [102, 43, 37], 
                          [69, 96, 70]]) 

"""Numpy arrays can have a number of dimensions, and different lengths along 
each dimension using the .shape property of an array
"""
#print(climatic_data.shape) 
#print(weights.shape) 

arr3 = np.array([ 
    [[11, 12, 13], 
     [14, 15, 16]], 

     [[15, 16, 17], 
      [18, 19, 20]]
])
#print(arr3.shape) 

"""
All elements in a numpy array have the same datatype. You can check the type of "
an array using the .dtype property.
"""
#print(climatic_data.dtype)
#print(weights.dtype) 

"""If an array contains a single floating point number, all the 
elements are also coverted to floats.
""" 


""""
We can now compute the predicted yields of apples in all the regions, using 
a  single matrix multiplication between climatic_data (a 5x3 matrix) and weights (a vector of length 3). 

We can use the np.matmul function from Numpy, or simply use the @ operator to 
perform the matrix multiplication
"""
all_apple_yields = np.matmul(climatic_data, weights) 
#print(all_apple_yields)
all_apple_yields = climatic_data @ weights 
#print(all_apple_yields) 

"""Numpy also provides helper functions for reading & writing to files. 
Let's download climatic.txt which contains 10, 000 climatic data (temp., rainfall & humidity) 
in the the following format: 

temperature, rainfall, humidity
25.00, 76.00, 99.00
39.00, 65.00, 70.00
59.00, 45.00, 77.00 
...

This format of storing data is known as comma seperated values or CSV
"""
from  urllib import request
import os 

def download_dataset():
    if os.path.exists("data/climate.txt"):
        print("Already exists. Skipping download.") 
    else: 
        request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', "data/climate.txt")

download_dataset() 

climate_data = np.genfromtxt("data/climate.txt", delimiter=",", skip_header=1) 
#print(climate_data.shape)
#print(climate_data[0])

"""We can now use a matrix multiplication operator @ to predict the yield 
of apples for the entire dataset using a given set of weights.
"""
weights = np.array([0.3, 0.2, 0.5]) 
yields = climate_data @ weights 
#print(yields.shape)

"""
We can now add the yields back to the climate_data as a fourth column 
using the np.concatenate function
"""
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
#print(climate_results)

"""
Let's write the final results from our computation above back to 
a file using the np.savetxt function""" 
np.savetxt("data/climate_results.txt", 
           climate_results, 
           fmt="%.2f", 
           header="temperature,rainfall,humidity,yield_apples", 
           comments="") 

"""Numpy provides hundreds of functions for performing operations on 
arrays. Here are some common functions: 
* Mathematics: np.sum, np.exp, np.round, arithmetic operations 
* Array manipulation: np.reshape, np.stack, np.concatenate, np.split
* Linear Algebra: np.matmul, np.dot, np.transpose, np.eigvals, 
* Statistics: np.mean, np.median, np.std, np.max 
"""


"""Arithmetic Operations and Broadcasting
Numpy arrays support arithmetic operators like +, -, *. You 
can perform an arithmetic operation with a single number (also called a scalar), 
or with another array of the same shape. This makes it really easy to 
write mathematical expressions with multi-dimensional arrays. 
"""
arr2 = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 1, 2, 3]
]) 

arr3 = np.array([
    [11, 12, 13, 14], 
    [15, 16, 17, 18], 
    [19, 11, 12, 13]
]) 

"""Adding a scalar"""
res = arr2 + 3 

"""Element-wise subtraction""" 
res = arr3 - arr2 

"""Modulus with a scalar"""
res = arr2 % 4

"""Numpy arrays also support broadcasting, which allows arithmetic 
operations between two arrays having a different number of dimensions,
but compatible shapes. Let's look at an example to see how it works.
"""
arr2 = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8], 
    [9, 1, 2, 3]
]) 

arr4 = np.array([4, 5, 6, 7]) 
res = arr2 + arr4 

"""
Comparism Operators
Numpy also supports comparism operations like ==, !=, > etc. 
The result is an array of booleans.
"""
arr1 = np.array([[1, 2, 3], [3, 4, 5]]) 
arr2 = np.array([[2, 2, 3], [1, 2, 5]])

res = arr1 == arr2 
res = arr1 != arr2 
res = arr1 >= arr2 
res = arr1 < arr2 

"""A common use case is to count the number of equal elements in two 
arrays using sum method. Remember that True evaluates to 1 and False 
evalautes to 0 when booleans are used in arithmetic operations.
"""
res = (arr1 == arr2).sum()

"""
Numpy extends Python's list indexing notation using [] to multiple 
dimensions in a fairly intuitive fasion. You can provide a comma seperated list of indices or ranges to 
select a specific element or subarray (also called slice) from a numpy array. 
"""
arr3 = np.array([
    [
        [11, 12, 13, 14], 
        [13, 14, 15, 19]
    ],

    [
        [15, 16, 17, 18], 
        [63, 92, 36, 18], 
    ], 

    [
        [98, 32, 81, 23], 
        [17, 18, 19.5, 43]
    ]
])

"Single element" 
res = arr3[1, 1, 2] 

"""Subarray using ranges"""
res = arr3[1:, 0:1, :2]

"""Mixing indices and ranges""" 
res = arr3[1:, 1, 3] 

"""Mixing indices and ranges""" 
res = arr3[1:, 1, :3] 

"""Using fewer indices""" 
res = arr3[1]

"""Other ways of creating creating Numpy arrays 
Numpy also provides some handy functions to create arrays 
of a desired shape with fixed or random values.
"""

"""All zeros"""
res = np.zeros((3, 2)) 

"""All ones"""
res = np.ones((2, 2, 3)) 

"""Indentity matrix"""
res = np.eye(3) 

"""Random vector"""
res = np.random.rand(5) 

"""Random matrix"""
res = np.random.randn(2, 3)

"""Fixed value"""
res = np.full([2, 3], 42)

"""Range with start, end and step """
res1 = np.arange(10, 90, 3).reshape(3, 3, -1)

"""Equally spaced numbers in a range"""
res = np.linspace(3, 27, 9)
print(res1)  