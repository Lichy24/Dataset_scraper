import requests # GET requets to scrap a url/website
from bs4 import BeautifulSoup # parsing response content and HTML tags.
import re

class Straoshpereips:

    def __init__(self, save_dir):
        self.save_dir = save_dir


    def straoshpereips_extract(self,exetsion):
        domain_url = 'https://www.stratosphereips.org'
        exercises_page_url = domain_url +'/'+ exetsion
        pcaps_urls = get_pcaps_urls(exercises_page_url)

        for pcaps_url_name in pcaps_urls:
            # Note: hrefs are relative links to the domain and not absolute.
            pcap_file_urls = get_pcap_file_hrefs(pcaps_urls[pcaps_url_name])
            print(pcap_file_urls)
            for pcap_file_url in pcap_file_urls:
                download_pcap_zip_file( pcaps_urls[pcaps_url_name]+'/'+ pcap_file_url,
                                    self.save_dir+'/'+pcaps_url_name+'+'+pcap_file_url,chunk_size=8192)




def get_pcaps_urls(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    pcaps_container = soup.find('div', class_='sqs-block-content')
    a_elements_with_href = pcaps_container.find_all('a',href=True)
    a_elements_with_href.pop(0)
    exercises_urls = dict()
    for a_element in a_elements_with_href:
        exercises_urls[a_element.get_text()] = a_element['href']
        
    return exercises_urls

def get_pcap_file_hrefs(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    a_elements_with_href = soup.find_all('a',href=True,text=re.compile(r'.pcap$'))
    pcap_file_urls = list()
    for a_element in a_elements_with_href:
            pcap_file_urls.append(a_element['href'])
            
    return pcap_file_urls

def download_pcap_zip_file(url: str, save_path: str, chunk_size=128):
    try:
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=chunk_size):
                fd.write(chunk)
    except:
        # do not crash the program, but notify the user.
        print('Error: Couldnt download or save pcap_zip file with url of', url, 'in filepath of', save_path)



