from bs4 import BeautifulSoup
import urllib3
import urllib3.contrib.pyopenssl
# import openanything, httplib
import tldextract
import re
import certifi
import config as c
import createPath as cp

aHrefList = []
imgsrcList = []
imgsrcsetList = []
iframesrcList = []
scriptsrcList = []
spansrcList = []


def init_PoolManager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

def check_link_contains(soup, tag):
    if '#' in str(soup.get(tag)) or \
            'none' in str(soup.get(tag)).lower() or \
            not soup.has_attr(tag):
        return False
    return True

def append_list(list,soup, tag):
    if str(soup.get(tag)).startswith('//'):
        list.append('https:' + soup.get(tag))
    elif str(soup.get(tag)).startswith('/'):
        list.append(c.defaultURL + soup.get(tag))
    else:
        list.append(soup.get(tag))

def find_div(soup):
    for div in soup.find_all(c.DIV):
        insert_a(div)
        insert_img(div)
        find_iframe(div)

def find_script(soup):
    for script in soup.find_all(c.SCRIPT):
        if check_link_contains(script,c.SRC):
            if not script.get(c.SRC) in scriptsrcList:
                append_list(scriptsrcList,script,c.SRC)
def find_iframe(soup):
    for iframe in soup.find_all(c.IFRAME):
        if check_link_contains(iframe,c.SRC):
            if not iframe.get(c.SRC) in iframesrcList:
                append_list(iframesrcList, iframe,c.SRC)

def find_span(soup):
    for span in soup.find_all(c.SPAN):
        if check_link_contains(span, c.SRC):
            if not span.get(c.SRC) in spansrcList:
                append_list(spansrcList,span,c.SRC)

def insert_a(soup):
    for a in soup.find_all(c.HYPERLINK_A):
        if check_link_contains(a, c.HREF):
            if not (str(a.get(c.HREF)) in aHrefList):
                append_list(aHrefList,a,c.HREF)

def insert_img(soup):
    for img in soup.find_all(c.IMG):
       if check_link_contains(img,c.SRC):
           if not (img.get(c.SRC) in imgsrcList):
               append_list(imgsrcList,img,c.SRC)
       if check_link_contains(img,c.SRCSET):
           if not (img.get(c.SRCSET) in imgsrcsetList):
               append_list(imgsrcsetList,img,c.SRCSET)


                # print (script.get('src'))

def queryPage(con, url):
    print(url)
    page = con.request('GET',url,headers={'User-agent':c.WINDOWS_CHROME}, redirect=True)
    # opener = urllib3.request.build_opener()
    # f = opener.open(request)
    if page.status in c.GOOD_STATUS_LIST:
        print(page.status)
        soup = BeautifulSoup(page.data, features='lxml')
        cp.createFile('miniclip', str(str(url).split("/")[2].split(".")[1]+".html"), str(soup.prettify))
        find_script(soup)
        find_div(soup)
        find_iframe(soup)
        print("Div Href:")
        for line in aHrefList:
            print(line)
        #
        print("IMG Src: ")
        for line1 in imgsrcList:
            print(line1)
        #
        print("IMG Srcset: ")
        for line2 in imgsrcsetList:
            print(line2)
        # print(page.url)
        print("Script: ")
        for line3 in scriptsrcList:
            print(line3)
        print("IFRAME: ")
        for line4 in iframesrcList:
            print(line4)

    elif page.status in c.REDIRECT_STATUS_LIST:
        print(page.status)
        # print(page.url)
    elif page.status in c.BAD_STATUS_LIST:
        print(page.status)
        # print(page.url)
    elif page.status in c.SERVER_ERROR_STATUS_LIST:
        print (page.status)

def extractDomain():
    ext = tldextract.extract(c.defaultURL)
    c.defaultPath = ext.domain
    print ("Default Path: ",c.defaultPath)
    # print(c.defaultURL)
    # print("Something: ",ext.subdomain,ext.domain,ext.suffix)
    # url_parts = (u.subdomain, u.domain, u.suffix, rest)


    # print("Default Path:", ext.domain)

con = init_PoolManager()
# c.defaultpath = tldextract.extract('http://forums.bbc.co.uk/')

c.defaultURL = "https://www.miniclip.com"
extractDomain()
queryPage(con, "https://www.miniclip.com/games/en/")