from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/aphrodite"
url2 = "http://olympus.realpython.org/profiles/poseidon"
url3 = "http://olympus.realpython.org/profiles/dionysus"
url4 = ''

Scrape_this_page = url3


page = urlopen(Scrape_this_page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

def get_title_string_method(html): #use string methods to get title
    title_index = html.find("<title>")
    start_index = title_index + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    return title 

# print (get_title_string_method(html))

def get_title_regex_method(html): #use regex to get title
    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    return title

def get_with_bs4(html):
    soup = BeautifulSoup(html, "html.parser")
    
    print(soup.get_text()) # automatically remove any HTML tags
    
    print(soup.findAll('img')) # automatically show all img tags, returns a list of all <img> tags in the HTML document.
    image1, image2 = soup.find_all("img") # This returns <img> tags in the HTML document as variables.
    print(image1.name) # This returns first <img> tag name in the HTML document.
    print(image1['src']) # This returns first <img> tag src in the HTML document.
    print(soup.title) # Returns title (with tags)
    print(soup.title.string) # Returns title as string (without tags)
    
    
    
get_with_bs4(html)
