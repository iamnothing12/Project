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

def browser_options(bs_type, device, argument){
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
}
def main():
    content = ""
    domain_stripper("https://www.miniclip.com/games/en")
    con = init_pool_manager()
    #WebDriver code here...
    opts = Options()
    opts.add_argument("user-agent=["+str(c.WINDOWS_CHROME)+"]")
    prefs = {'download.default_directory' : './webpage'}
    opts.add_experimental_option('prefs', prefs)
    # opts.add_argument("download.default_directory=D:/FYP/Project/webpage")
    # chrome = webdriver.Chrome(chrome_options=opts, executable_path=c.CHROME_WINDOWS)
    chrome = webdriver.Chrome(options=opts, executable_path=c.CHROME_WINDOWS)
    try:
        
        chrome.get("https://www.miniclip.com/games/en/")
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

        # with open("webpage/miniclip.html", "w+", encoding='utf-8') as f:
        #     f.write(content)
        # print(chrome.page_source)
        # parse html
        h = html.fromstring(content)
        list = []
        for hr in h.xpath('//@href'):
            if "#" != hr and len(hr) >1:
                # print("HR [%s]"%hr)
                page = con.request('GET',hr,headers={'User-agent':c.WINDOWS_CHROME,'Content-Type': 'application/json','Cache-Control':'max-age=0',"Referer": "https://www.miniclip.com/"}, retries=False)
                if page.status in c.GOOD_STATUS_LIST:
                    soup = BeautifulSoup(page.data, features='lxml')
                    cp.createFile("webpage","miniclip.html", str(soup.prettify))
                    print("meh")
                else:
                    print("dey")
                list.append(hr)
        print("Total Links Found [%i]" % len(list))
        for src in h.xpath('//@src'):
            if "#" != hr and len(hr) >1:
                # print("SRC [%s]" % src)
                page = con.request('GET',hr,headers={'User-agent':c.WINDOWS_CHROME,'Content-Type': 'application/json','Cache-Control':'max-age=0',"Referer": "https://www.miniclip.com/"}, retries=False)
                if page.status in c.GOOD_STATUS_LIST:
                    soup = BeautifulSoup(page.data, features='lxml')
                    cp.createFile("webpage","miniclip.html", str(soup.prettify))
                    print("meh2")
                else:
                    print("dey2")
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

    finally:
        print("QUITTED")
        chrome.quit()

    # soup0 = BeautifulSoup(content, features='lxml')
    # result0 = hashlib.md5(str(soup0).encode()) 
    # # # Create connection pool to use
    # con = init_pool_manager()
    # result1 = ""
    # page0 = con.request('GET', "https://example.com/",headers={'User-agent':c.WINDOWS_CHROME,'Content-Type': 'application/json','Cache-Control':'max-age=0'}, retries=False)
    # if page0.status in c.GOOD_STATUS_LIST:
    #     soup = BeautifulSoup(page0.data, features='lxml')
    #     result1 = hashlib.md5(str(soup).encode()) 
    # else:
    #     print("Page Status",page0.status)
    # print("Results Crawl & JS %s" % [str(result0.hexdigest()), str(result1.hexdigest())])

#     # profile = webdriver.FirefoxProfile()
#     # firefox = webdriver.Firefox(profile,executable_path=c.FIREFOX_WINDOWS)
#     # firefox.get("https://www.miniclip.com/games/en/")
#     # profile.set_preference("general.useragent.override", "[user-agent string]")
#     #Below is tested line
#     #profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")
    
    ## Testing save page
    # dl_path = "webpage/"
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("browser.download.folderList", 0)
    # profile.set_preference("browser.download.manager.showWhenStarting", False)
    # profile.set_preference("browser.download.dir", dl_path)
    # profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
    #                       "text/plain,text/x-csv,text/csv,application/vnd.ms-excel,application/csv,application/x-csv,text/csv,text/comma-separated-values,text/x-comma-separated-values,text/tab-separated-values,application/pdf")
    # firefox = webdriver.Firefox(firefox_profile=profile,executable_path=c.FIREFOX_WINDOWS)
    # firefox.get("https://www.miniclip.com/games/en/")



    
if __name__ == "__main__":
    main()