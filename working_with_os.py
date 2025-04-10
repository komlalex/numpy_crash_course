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
print(file1_contents) 
file1.close() 
# file1.read() #ValueError: I/O operation on closed file. 

"""Closing files automatically using with
To make it easy to automatically close a file once you are done, processing it, 
you can open it using the with statement. 
"""

with open("./loans/loans2.txt", "r") as file2: 
    file2_contents = file2.read() 
    print(file2_contents)

"""Once the statement within the with block is executed, the .close method on 
file2 is automatically invoked. Let's verify this by trying to read from the file 
object again.
"""
# file2.read() #ValueError: I/O operation on closed file. 

"""Reading a file line by line
File objects provide a readlines method to read a file line-by-line""" 

with open("./loans/loans3.txt", "r") as file3: 
    file3_lines = file3.readlines() 
    print(file3_lines[0].strip())