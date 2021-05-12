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

# imports
from MTA_pcapUnzipper import unzip_all_in_directory
from scrap import get_traffic_analysis_exercises_urls, get_pcap_zip_hrefs, download_pcap_zip_file, trim_page_url_to_directory_url

## main entry ##
# configuration

class MTA:
    def __init__(self,save_dir,extract_dir):
        self.save_dir = save_dir
        self.extract_dir = extract_dir

    def extract(exetsion,ans):
        domain_url = 'https://www.malware-traffic-analysis.net'
        exercises_page_url = domain_url +'/'+ exetsion
        exercise_urls = get_traffic_analysis_exercises_urls(exercises_page_url)
        if ans == 'blogs':
            domain_url = exercises_page_url
        
        for exe_url in exercise_urls:
            # Note: hrefs are relative links to the domain and not absolute.
            pcap_zip_urls = get_pcap_zip_hrefs(domain_url +'/'+ exe_url)
            print(pcap_zip_urls)
            for pcap_zip_url in pcap_zip_urls:
                download_pcap_zip_file(trim_page_url_to_directory_url(domain_url +'/'+ exe_url) +'/'+ pcap_zip_url,
                                    save_dir+'/'+pcap_zip_url)



    def MTA_exercises_or_blogs(ans):
        if ans == 'blogs':
            years = ['2013','2014','2015','2016','2017','2018','2019','2020','2021']
            for year in years:
                extract(year,ans)
        elif ans == 'exercises':
            extract('training-exercises.html',ans)
        # unzip
        unzip_all_in_directory(save_dir, extract_dir)


