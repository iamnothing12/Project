from bs4 import BeautifulSoup
import urllib3
import urllib3.contrib.pyopenssl
import re
import config as c
import createPath as cp
import certifi
import logging
from datetime import datetime
import lxml.html
import tldextract
import robot as r

try:
    from bs4 import UnicodeDammit             # BeautifulSoup 4

    def decode_html(html_string):
        converted = UnicodeDammit(html_string)
        if not converted.unicode_markup:
            raise UnicodeDecodeError(
                "Failed to detect encoding, tried [%s]",
                ', '.join(converted.tried_encodings))
        # print converted.original_encoding
        return converted.unicode_markup

except ImportError:
    from BeautifulSoup import UnicodeDammit   # BeautifulSoup 3

    def decode_html(html_string):
        converted = UnicodeDammit(html_string, isHTML=True)
        if not converted.unicode:
            raise UnicodeDecodeError(
                "Failed to detect encoding, tried [%s]",
                ', '.join(converted.triedEncodings))
        # print converted.originalEncoding
        return converted.unicode

aHrefList = []

# http = urllib3.PoolManager()

# url = "https://www.pythonforbeginners.com"
# content = http.request('GET',url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
# soup = BeautifulSoup(content.data, features='lxml')

# # print(soup.prettify)

# for link in soup.find_all('link'):
#     print(link.get('href'))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for link in soup.find_all('img'):
#     print(link.get('src'))

urlPattern = re.compile(r'^((http:\/\/|https:\/\/)(([a-zA-Z0-9\-\%])*\.)*([a-zA-Z0-9\-])*([a-zA-Z0-9\/\-\.\?\=\%\&\,])*)')
def matchurlPattern(url):
    if urlPattern.fullmatch(url):
        return True
    else:
        return False

def queryAdditionalSite(con,url,filename):
    if matchurlPattern(url):
        logging.info("Correct URL Format: [ %s ]" % url)
        # Disable retries to prevent flooding the site
        page = con.request('GET',url,headers={'User-agent':c.ANDROID_FIREFOX}, retries=False)
        # while page.status in c.REDIRECT_STATUS_LIST:
        #     pageURL = page.geturl()
        #     page = con.request('GET',pageURL,headers={'User-agent':c.ANDROID_FIREFOX}, retries=False)
        
        if page.status in c.GOOD_STATUS_LIST:
            soup = BeautifulSoup(page.data, features='lxml')
            # print(soup.prettify)
            logging.info("Creating Additional Site: [ "+str(url).split("/")[2].split(".")[1]+" ]")
            print("Path: [ %s ]" % str(c.defaultPath+filename.rsplit('/', 1)[0]))
            print("Filename: [ %s ]" % filename.split('/')[1])
            cp.createFile(c.defaultPath+filename.rsplit('/', 1)[0],filename, str(soup.prettify))
            
        else:
            logging.info("This page [ %s ] cannot be crawled." % url)
            return False
        return True
    else:
        logging.error("Wrong URL Format: [ %s ]" % url)
        return False

def divDiver(soup):
    for div in soup.find_all('div'):
        divDiver(div)
        insertA(div)

def insertA(soup):
    for a in soup.find_all('a'):
        if not( '#' in str(a.get('href'))):
            if not (str(a.get('href')) in aHrefList):
                print(a.get('href'))
                aHrefList.append(a.get('href'))

def querySite(con,url):
    if matchurlPattern(url):
        logging.info("Correct URL Format: [ %s ]" % url)
        # Disable retries to prevent flooding the site
        
        page = con.request('GET',url,headers={'User-agent':c.ANDROID_FIREFOX}, retries=False)
        # while page.status in c.REDIRECT_STATUS_LIST:
        #     pageURL = page.geturl()
        #     print("URL "+str(pageURL))
        #     page = con.request('GET',pageURL,headers={'User-agent':c.ANDROID_FIREFOX}, retries=False)
        print("Page Status"+str(page.status))
        if page.status in c.GOOD_STATUS_LIST:
            soup = BeautifulSoup(page.data, features='lxml')
            # print(soup.prettify)
            logging.debug(str(url).split("/")[2].split(".")[1])
            c.defaultPath=str(url).split("/")[2].split(".")[1]
            cp.createFile(c.defaultPath, str(str(url).split("/")[2].split(".")[1]+".html"), str(soup.prettify))
            divDiver(soup)
            for href in aHrefList:
                if not (r.check_robot(href,headers=c.ANDROID_CHROME)):
                    if not (str(href).startswith("None")):
                        if not (str(href).startswith("http")):
                            ext = tldextract.extract(c.defaultURL)
                            print("href1: [ %s ]" % str("https://"+str(ext.registered_domain)+str(href)))
                            queryAdditionalSite(con,"https://"+str(ext.registered_domain)+str(href), str(href))
                            # queryAdditionalSite(con,href, href)
                        else:
                            print("href2: [ %s ]" % str(href))
                            queryAdditionalSite(con,href, href)
            # for div in soup.find_all('div'):
            #     for a in div.find_all('a'):
            #         print(a.get('href'))

            # print('FML')
            # for link in soup.find_all('div'):
            #     print(str(link.find('a')['href']))
                # print(link.get('href'))
                # if not (r.check_robot(link.get('href'),headers=c.ANDROID_CHROME)):
                #     # print(link.get('href'))
                #     logging.debug(link.get('href'))
                #     if not (str(link.get('href')).startswith("None")):
                #         # print(link.get('href'))
                #         if not (str(link.get('href')).startswith("http")):
                #             # print(link.get('href'))
                #             print (str(link.get('href')))
                #             logging.info("Checking in progress"+str(link.get('href')))
                #             # if not (str(link.get('href')[-1] == "/")):
                #             print(link.get('href'))
                #             ext = tldextract.extract(c.defaultURL)
                #             logging.info("All if Condition works"+"https://" + str(ext.registered_domain)+ str(link.get('href')))
                            
                #             print("https://"+str(ext.registered_domain)+str(link.get('href')))
                #             queryAdditionalSite(con,"https://"+str(ext.registered_domain)+str(link.get('href')), str(link.get('href')))
                                # queryAdditionalSite(con,"https://"+ str(ext.registered_domain)+ str(link.get('href'),str(link.get('href'))))
                                # c.urlList.append("https://"+ str(ext.registered_domain)+ str(link.get('href')))
        else:
            logging.info("This page [ %s ] cannot be crawled." % url)
            return False
        return True
    else:
        logging.error("Wrong URL Format: [ %s ]" % url)
        return False



def init_PoolManager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

def main():
    logging.basicConfig(filename='logs/'+str(datetime.now().strftime("%d%m%Y")),level=logging.DEBUG)
    con = init_PoolManager()
    r.get_robot("https://www.google.com/robots.txt")
    # r.check_robot('http://www.google.com/js/',headers=c.ANDROID_CHROME)
    c.defaultURL="https://www.google.com/"
    # querySite(con, "www.google.com")
    querySite(con, "https://www.google.com/")

    # cp.deletePath("y8https")
    
# def get_module_logger(mod_name):
#   logger = logging.getLogger(mod_name)
#   handler = logging.StreamHandler()
#   formatter = logging.Formatter(
#         '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
#   handler.setFormatter(formatter)
#   logger.addHandler(handler)
#   logger.setLevel(logging.DEBUG)
#   return logger

if __name__ == "__main__":
    main()
