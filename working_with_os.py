"""Interacting with the OS and filesystem 
The os module in Python provides many functions for interacting with the 
OS and the filesystem. 
Let's import it and try out some examples
"""
import os 

"""Check the current working directory"""
cur_dir = os.getcwd() 

"""Tp get the list of files in a directory, us os.listdir. You can 
pass an absolute or relative path of a directory as te argument to the function. 
"""
lst_dir = os.listdir(".") 
lst_dir = os.listdir("/data") 

"""An new direcory can be created using os.mkdirs."""
os.makedirs("./loans", exist_ok=True) 
created = "loans" in os.listdir(".") 

"""Let us download some files into the data directory using the urllib module"""
from urllib import request 
def download_data(url, save_dir):
    if os.path.exists(save_dir): 
        print("File already exists. Skipping download.") 
    else: 
        request.urlretrieve(url, save_dir)
url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'
download_data(url1, "./loans/loans1.txt")
download_data(url2, "./loans/loans2.txt")
download_data(url3, "./loans/loans3.txt")

"""Reading from a File
To read the contents of a file, we first need to open the file using the built-in 
open function. The open function returns a file object, provides several 
methods for interacting with the contents of a file. It also accepts a mode 
argument"""
file1 = open("./loans/loans1.txt", mode="r") 

"""The open function also accepts a mode argument to specify how to interact 
with the file. The following are supported: 
"r" -> open for reading
"w" -> open for writing, truncating the file first 
"x" -> creating a new file and open it for writing 
"a" -> open for writing, appending to the end of the file if it exists
"""

"""To get the content of the file, we use the read method of the file object."""
file1_contents = file1.read() 
#print(file1_contents) 
file1.close() 
# file1.read() #ValueError: I/O operation on closed file. 

"""Closing files automatically using with
To make it easy to automatically close a file once you are done, processing it, 
you can open it using the with statement. 
"""

with open("./loans/loans2.txt", "r") as file2: 
    file2_contents = file2.read() 
    #print(file2_contents)

"""Once the statement within the with block is executed, the .close method on 
file2 is automatically invoked. Let's verify this by trying to read from the file 
object again.
"""
# file2.read() #ValueError: I/O operation on closed file. 

"""Reading a file line by line
File objects provide a readlines method to read a file line-by-line""" 

with open("./loans/loans3.txt", "r") as file3: 
    file3_lines = file3.readlines() 
    #print(file3_lines[0].strip()) 

"""Processing data from files 
Before performing any operations on the data stored in a file, we 
need to convert the contents of the file from one large string into Python data types. 
For the file loans1.txt containing information about loans in a CSV format, 
we can do the following: 
* read the file line by line
* Parse the first line to get list of column names or headers
* Split each remaining line and convert each value into a float 
* Create a dictionary for each loan using the headers as keys 
* Create a list of dictionaries to keep track of all the loans

Since we will perform the same operations for multiple files, it would be 
useful to define a function read_csv to do this. We'll also define some helper 
functions to build up the functionalities step by step.

Let's start by defining a function parse_header which takes a line as input and 
returns a list of columns headers
""" 

def parse_header(header_line: str): 
    return header_line.strip().split(",") 

"""The strip method removes anny extra spaces and new_line character \n, and 
the split method breaks a string into a list using the given (, in this case)
"""
with open("./loans/loans3.txt", "r") as file3: 
    file3_lines = file3.readlines() 

headers = parse_header(file3_lines[0])

"""Next, we define a function parse_values which takes a line containing some 
data, and returns a list of floating point numbers
"""
def parse_values(data_line: str): 
    values = []
    for item in data_line.strip().split("," ): 
        if item == "": 
            values.append(0.0) 
        else:
            values.append(float(item)) 
    return values 

values = parse_values(file3_lines[2]) 


"""The values were parsed and converted into floating pount numbers, as expected. 
Let's try it for another line from the file, which does not contain a value 
for the down payment."""

"""Next, let's define a function create_item_dict which takes a list of values
and a list of headers as inputs, and return a dictionary with the values 
associated with their respective headers as keys.
"""

def create_item_dict(values, headers): 
    result = {} 
    for value, header in zip(values, headers):
        result[header] = value 
    return result 

values1 = parse_values(file3_lines[1]) 
dict1 = create_item_dict(values1, headers) 


"""As expected, the values & headers are combined to create a dictionary with the 
appropriate key value pairs. 

We are now ready to put everything together and define the read_csv function
""" 

def read_csv(path): 
    result = [] 
    # Open file in read mode 
    with open(path, "r") as f: 
        # Get a list of lines 
        lines = f.readlines()
        # Parse the header 
        headers = parse_header(lines[0]) 
        
        #Loop over the remaining lines 
        for data_line in lines[1:]: 
            # parse values 
            values = parse_values(data_line) 
            # Create a dictionary using the values & headers 
            item_dict = create_item_dict(values, headers)
            # Add the dictionary to the result 
            result.append(item_dict)
    return result 

"""Let's try it out"""
data = read_csv("./loans/loans2.txt") 

import  math

def loan_emi(amount, duration, rate, down_payment=0): 
    """Calculate the equal monthly installment (EMI) for a loan.
    
    Arguments: 
    amount - Total amount to be spent (loan + down payment) 
    duration - Duration of the laon (in months) 
    rate - Rate of interest (monthly) 
    down_payment - (optional) - Optional initial payment (deducted from the amount)
    """ 
    loan_amount = amount - down_payment 
    try: 
        emi = loan_amount * rate * ((1 + rate) ** duration) / (((1+rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount/ duration 
    
    emi = math.ceil(emi) 
    return emi 

"""We can use the function to calculate the EMIs for all the loans in a file"""
loans2 = read_csv("./loans/loans2.txt") 

    
def compute_emis(loans):
    for loan in loans: 
        loan["emi"] = loan_emi(loan["amount"], 
                           loan["duration"], 
                           loan["rate"] / 12, 
                           loan["down_payment"])  
    return loans 

loans2 = compute_emis(loans2)
print(loans2)