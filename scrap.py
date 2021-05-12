
import requests # GET requets to scrap a url/website
from bs4 import BeautifulSoup # parsing response content and HTML tags.
import os

def is_has_pcap_zip_suffix(string: str):
    return string.endswith('.pcap.zip')

def get_traffic_analysis_exercises_urls(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    a_elements_with_href = soup.find_all('a', class_='list_header', href=True)
    exercises_urls = list()
    for a_element in a_elements_with_href:
        exercises_urls.append(a_element['href'])
        
    return exercises_urls

def get_pcap_zip_hrefs(url: str):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    a_elements_with_href = soup.find_all('a', class_='menu_link', href=True)
    pcap_zip_file_urls = list()
    for a_element in a_elements_with_href:
        if is_has_pcap_zip_suffix(a_element['href']):
            pcap_zip_file_urls.append(a_element['href'])
            
    return pcap_zip_file_urls

def download_pcap_zip_file(url: str, save_path: str, chunk_size=128):
    try:
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in response.iter_content(chunk_size=chunk_size):
                fd.write(chunk)
    except:
        # do not crash the program, but notify the user.
        print('Error: Couldnt download or save pcap_zip file with url of', url, 'in filepath of', save_path)

def trim_page_url_to_directory_url(url: str):
    '''
    Example:
        Input: https://www.malware-traffic-analysis.net/2021/01/21/index.html
        Output: https://www.malware-traffic-analysis.net/2021/01/21
    '''
    return os.path.split(url)[0]



