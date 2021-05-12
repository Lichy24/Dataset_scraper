##################################
''' 
Date:
    26/01/2021
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Author:
    Neyney10
    https://github.com/neyney10

Edited:
    Lichy24
    https://github.com/Lichy24
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Python version used: 
    Python 3.85 x64 bit
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
OS used:
    Windows 10
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Dependencies:
    requests
    bs4
    os (builtin)
    zipfile (builtin)
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Usage:
    py main.py
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Original source:
    https://devopscube.com/python-web-scrapping/
'''
##################################

from stratoshpereips_extractor import Straoshpereips
from MTA_extractor import MTA

save_dir = './pcap_zip'
extract_dir = './extracted'

print('The script was created by Neyney10 and edited by Lichy24 developed on 26/01/2021.')
print('////////////////////////////////////////////////////////////////////////////////')
print('The script support 2 datasets webpages:\n\t1) Malware Traffic Analysis\n\t2) Stratosphereips')
ans = input('Please selected the wanted dataset webpage to be pulled by inputing the number....')
if ans == '1':
    ans = input('Please Selected which page to extract:\n\t1) exercises\n\t2) blogs\n\t3) both....')
    mta = MTA(save_dir,extract_dir)
    if ans == '1':
        mta.MTA_exercises_or_blogs('exercises')
    elif ans == '2':
        mta.MTA_exercises_or_blogs('blogs')
    elif ans == '3':
        mta.MTA_exercises_or_blogs('blogs')
        mta.MTA_exercises_or_blogs('exercises')
elif ans == '2':
    print("The Stratosphereips download the malware page:(can also be used for the bengin page not been tested)")
    #ans = input("Please enter which page to extract:(Works for Malware and Bengin)....")
    Straoshpereips(extract_dir).straoshpereips_extract('datasets-malware')
    
    


