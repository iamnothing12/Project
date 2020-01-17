#https://iamnothing12.github.io/Project/request.js

import urllib3
import urllib3.contrib.pyopenssl
import certifi
import hashlib 
from bs4 import BeautifulSoup
import config as c
import createPath as cp
import webbrowser
from lxml import html
import requests
import time


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#For Chrome request headers
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary





requestJS = "https://iamnothing12.github.io/Project/request.html"
# requestJS = "request.html"
# initialize ssl connection
def init_pool_manager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

def domain_stripper(url):
    c.defaultURL = url
    urlsplit = str(url).replace("https://","").split("/")
    print(urlsplit)

def browser_options(bs_type, device, argument):
    if "firefox" in bs_type:
        print("Firefox Selected..")
        if "window" in device:
            print("Window Device Selected..")
            if not argument in "":
                print("Argument not provided exiting.")
            else:
                profile = webdriver.FirefoxProfile()
                return webdriver.Firefox(profile,executable_path=c.FIREFOX_WINDOWS)
    elif "chrome" in bs_type:
        print("Chrome Selected..")
    else:
        print("Incorrect or Missing Browser Type..")

def scroll_down(driver):
    SCROLL_PAUSE_TIME = 0.5
    count =0
    while count < 5:
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # try again (can be removed)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            # check if the page height has remained the same
            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue

def main():
    content = ""
    domain_stripper("https://www.miniclip.com/games/en")
    con = init_pool_manager()
    #WebDriver code here...
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", str(c.WINDOWS_FIREFOX))
    #Generate Driver Portfolio
    firefox = webdriver.Firefox(executable_path=c.FIREFOX_WINDOWS) #FIREFOX_LINUX
    
    list = []
    try:
        #Requesting Site
        firefox.get("https://www.miniclip.com/games/en/")
        # Scroll Down
        scroll_down(firefox)

        soup = BeautifulSoup(firefox.page_source, features='lxml')
        cp.createFile("webpage","miniclip.html", str(soup.prettify))

        h = html.fromstring(firefox.page_source)
        for hr in h.xpath('//@href'):
            if "#" != hr and len(hr) >1:
                list.append(hr)
        print("Total Links Found [%i]" % len(list))
        for src in h.xpath('//@src'):
            if "#" != hr and len(src) >1:
                list.append(src)
        
        print("Total Links Found [%i]" % len(list))


    finally:
        print("QUIT")
        firefox.quit()


    
if __name__ == "__main__":
    main()