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
os.makedirs("./loans_dir", exist_ok=True) 
created = "loans_dir" in os.listdir(".") 

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
download_data(url1, "./data_dir/loans1.txt")
download_data(url2, "./data_dir/loans2.txt")
download_data(url3, "./data_dir/loans3.txt")



