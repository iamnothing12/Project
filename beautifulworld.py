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
        if page.status == 200:
            soup = BeautifulSoup(page.data, features='lxml')
            # print(soup.prettify)
            logging.debug(str(url).split("/")[2].split(".")[1])
            cp.createFile(str(url).split("/")[2].split(".")[1],filename, str(soup.prettify))
            
        else:
            logging.info("This page [ %s ] cannot be crawled." % url)
            return False
        return True
    else:
        logging.error("Wrong URL Format: [ %s ]" % url)
        return False

def querySite(con,url):
    if matchurlPattern(url):
        logging.info("Correct URL Format: [ %s ]" % url)
        # Disable retries to prevent flooding the site
        page = con.request('GET',url,headers={'User-agent':c.ANDROID_FIREFOX}, retries=False)
        if page.status == 200:
            soup = BeautifulSoup(page.data, features='lxml')
            # print(soup.prettify)
            logging.debug(str(url).split("/")[2].split(".")[1])
            cp.createFile(str(url).split("/")[2].split(".")[1], str(str(url).split("/")[2].split(".")[1]+".html"), str(soup.prettify))
            for link in soup.find_all('script'):
                logging.debug(link.get('src'))
                if not (str(link.get('src')).startswith("None")):
                    if not (str(link.get('src')).startswith("http")):
                        logging.info("Checking in progress"+str(link.get('src')[-1]))
                        if not (str(link.get('src')[-1] == "/")):
                            ext = tldextract.extract(c.defaultURL)
                            logging.info("https://" + str(ext.registered_domain)+ str(link.get('src')))
                            queryAdditionalSite(con,"https://"+ str(ext.registered_domain)+ str(link.get('src')),str(link.get('src').strip('/')))
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

    c.defaultURL="https://www.google.com/qwertyuiop"
    querySite(con, "www.google.com")
    querySite(con, "https://www.google.com/")
    


if __name__ == "__main__":
    main()