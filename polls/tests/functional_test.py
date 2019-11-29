from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from urllib import response, request
from urllib.error import URLError, HTTPError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Chrome(executable_path='/Users/pawariswongsalung/Downloads/chromedriver')
    browser.get(url)

    links = []
    element = browser.find_elements_by_tag_name('a')
    for url in element:
        links.append(url.get_attribute('href'))

    browser.close()
    return links

def invalid_urls(urllist):
    invalid_links = []
    for url in urllist:
        try:
            rq = request.urlopen(url)
            print(f"{url} is OKAY")
        except URLError:
            invalid_links.append(url)
            print(f"{url} is Invalid !!!")
    return invalid_links


def main():
    links = get_links('https://cpske.github.io/ISP/')
    for link in links:
        print(link)
    print(" ")
    print("Now with Invalid Links: ")
    print(invalid_urls(links))

main()
