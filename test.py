from bs4 import BeautifulSoup
import urllib3
import urllib3.contrib.pyopenssl
# import openanything, httplib
import tldextract
import re
import certifi
import config as c
import createPath as cp
import robot as r
import find as f

#initialize ssl connection
def init_PoolManager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

#Extract domain name
def extractDomain():
    ext = tldextract.extract(c.defaultURL)
    c.defaultPath = ext.domain
    c.domainName = str(ext.subdomain)+"."+str(ext.domain)+"."+str(ext.suffix)
    print("Default Path: ", c.defaultPath)
    print("Domain name: ", c.domainName)

#Connect Main Page
def queryMain(con):
    # c.defaultURL
    request_page = con.request('GET', str(c.defaultURL), headers={'User-agent': c.WINDOWS_CHROME}, redirect=True)
    if request_page.status in c.GOOD_STATUS_LIST:
        print("Status: ["+str(request_page.status)+"]")
        soup = BeautifulSoup(request_page.data, features='lxml')
        f.find_all_link(soup)
        f.display_link()



#Main call
con = init_PoolManager()
c.defaultURL = "https://www.miniclip.com"
extractDomain()
queryMain(con)
# queryPage(con, "https://www.miniclip.com/games/en/")