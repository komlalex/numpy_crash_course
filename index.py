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

print(f"The expected yield of apples in Kanto region is {kanto_yield_apples} tons per hectare")

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
print(weights[0])

"""Operating on Numpy Arrays 
We can compute the dot product of the two vectors using the np.dot function
"""
#help(np.dot) 
kanto_yield_apples = np.dot(kanto, weights)
print(kanto_yield_apples) 

"""We can achieve the same result with lower level operations supported by 
Numpy arrays; performing an element-wise multiplication and calculating the sum 
of the resulting numbers.""" 
kanto_yield_apples = (kanto * weights).sum() 
print(kanto_yield_apples)

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
print(result)
end_time = timer() 
print_duration(start_time, end_time) 

start_time = timer()
result = np.dot(arr1_np, arr2_np)
end_time = timer() 
print_duration(start_time, end_time)