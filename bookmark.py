#https://iamnothing12.github.io/Project/request.js

import urllib3
import urllib3.contrib.pyopenssl
import certifi
import hashlib 
from bs4 import BeautifulSoup
import config as c
import createPath as cp
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


def main():
    domain_stripper("https://www.miniclip.com/games/en")
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
    try:
        #WebDriver code here...
        opts = Options()
        opts.add_argument("user-agent=["+c.WINDOWS_CHROME+"]")
        chrome = webdriver.Chrome(chrome_options=opts, executable_path=c.CHROME_WINDOWS)
        chrome.get("https://www.miniclip.com/games/en")
        print(chrome.page_source)
    finally:
        chrome.quit()
    # profile = webdriver.FirefoxProfile()
    # firefox = webdriver.Firefox(profile,executable_path=c.FIREFOX_WINDOWS)
    # firefox.get("https://www.miniclip.com/games/en/")
    # profile.set_preference("general.useragent.override", "[user-agent string]")
    #Below is tested line
    #profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0")




    
if __name__ == "__main__":
    main()