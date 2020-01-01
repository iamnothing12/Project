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
import os
os.environ['DISPLAY'] = ':0'
#Remove not working
import pyautogui

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

# def main():
#     domain_stripper("https://www.miniclip.com/games/en/")

#     opts = Options()
#     opts.add_argument("User-agent=["+str(c.WINDOWS_CHROME)+"]")
#     opts.add_argument('--ignore-certificate-errors')
#     options.add_argument('--ignore-ssl-errors')
#     chrome = webdriver.Chrome(chrome_options=opts,executable_path=c.CHROME_WINDOWS)
#     try:
#         chrome.get("https://www.miniclip.com/games/en/")
#     finally:
#         chrome.quit()

def main():
    domain_stripper("https://www.miniclip.com/games/en")
    #WebDriver code here...
    opts = Options()
    opts.add_argument("user-agent=["+str(c.WINDOWS_CHROME)+"]")

    chrome = webdriver.Chrome(chrome_options=opts, executable_path=c.CHROME_WINDOWS)
    try:
        
        chrome.get("https://www.miniclip.com/games/en")
        SCROLL_PAUSE_TIME = 0.5
        count =0
        while count < 5:
            # Get scroll height
            last_height = chrome.execute_script("return document.body.scrollHeight")
            # Scroll down to bottom
            chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = chrome.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # try again (can be removed)
                chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)
                # Calculate new scroll height and compare with last scroll height
                new_height = chrome.execute_script("return document.body.scrollHeight")
                # check if the page height has remained the same
                if new_height == last_height:
                    break
                else:
                    last_height = new_height
                    continue
        
        # print("Cookies: [ %s ]" % request_cookies_browser)
        content = chrome.page_source
        with open("miniclip.html", "w+", encoding='utf-8') as f:
            f.write(content)
        # print(chrome.page_source)
        # parse html
        h = html.fromstring(content)
        list = []
        for hr in h.xpath('//@href'):
            if "#" != hr and len(hr) >1:
                # print("HR [%s]"%hr)
                list.append(hr)
        print("Total Links Found [%i]" % len(list))
        for src in h.xpath('//@src'):
            if "#" != hr and len(hr) >1:
                # print("SRC [%s]" % src)
                list.append(src)
        
        print("Total Links Found [%i]" % len(list))
            # if not hr.startswith('http'):
            #     local_path = 'page/' + hr
            #     hr = base + hr
            # res = sess.get(hr)
            # if not os.path.exists(os.path.dirname(local_path)):
            #     os.makedirs(os.path.dirname(local_path))
            # with open(local_path, 'wb') as fp:
            #     fp.write(res.content)
    
        # open 'Save as...' to save html and assets
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.typewrite('test/mehmeh.html')
        pyautogui.hotkey('enter')
    finally:
        chrome.quit()
#     # profile = webdriver.FirefoxProfile()
#     # firefox = webdriver.Firefox(profile,executable_path=c.FIREFOX_WINDOWS)
#     # firefox.get("https://www.miniclip.com/games/en/")
#     # profile.set_preference("general.useragent.override", "[user-agent string]")
#     #Below is tested line
#     #profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")




    
if __name__ == "__main__":
    main()




    # # Create connection pool to use
    # con = init_pool_manager()

    # page0 = con.request('GET',c.defaultURL,headers={'User-agent':c.WINDOWS_CHROME,'Content-Type': 'application/json','Cache-Control':'max-age=0'}, retries=False)
    # page1 = con.request('GET',requestJS,headers={'User-agent':c.WINDOWS_CHROME}, retries=False)
    # result0 = ""
    # result1 = ""
    # if page0.status in c.GOOD_STATUS_LIST:
    #     soup = BeautifulSoup(page0.data, features='lxml')
    #     result0 = hashlib.md5(str(soup).encode()) 
    #     cp.createFile("miniclip","miniclip.html", str(soup.prettify))
    # else:
    #     print("page 0 failed"+str(page0.status))

    # if page1.status in c.GOOD_STATUS_LIST:
    #     soup = BeautifulSoup(page1.data, features='lxml')
    #     result1 = hashlib.md5(str(soup.data).encode()) 
    #     cp.createFile("miniclip","miniclipjs.html", str(soup.prettify))
    
    
    # print("Results Crawl & JS %s" % [str(result0.hexdigest()), str(result1.hexdigest())])