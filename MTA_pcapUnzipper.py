# -*- coding: utf-8 -*-
"""
SOURCE: https://raw.githubusercontent.com/IvanLetteri/MTA-KDD-19/master/MTA-pcapUnzipper.py
Note: Modified a bit to fit our uses.
"""

import os, zipfile

def unzip_all_in_directory(dir_name: str = './', save_dir: str = './extracted', file_extension: str = 'zip', password: str = 'infected'):
  #original_directory = os.getcwd()
  os.chdir(dir_name) # change directory from working dir to dir with files
  for item in os.listdir('./'):
    print(item)
    if item.endswith(file_extension):
      try:
        file_name = os.path.abspath(item)
        print(file_name)
        zip_ref = zipfile.ZipFile(file_name)
        zip_ref.extractall(save_dir, pwd=bytes(password,'utf-8'))
        zip_ref.close() # close file
      except:
        # do not crash the program, but notify the user.
        print('Error: Couldnt open pcap_zip file with password of', password, 'in filepath of', file_name)
