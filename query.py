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

def init_PoolManager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

def check_link_contains(soup, tag):
    if '#' in str(soup.get(tag)) or \
        'none' in str(soup.get(tag).lower()):
            return False
    return False

def append_list(list,soup, tag):
    if str(soup.get(tag)).startswith('//'):
        list.append('https:' + soup.get(tag))
    elif str(soup.get(tag)).startswith('/'):
        list.append(c.defaulturl + soup.get(tag))
    else:
        list.append(soup.get(tag))

def find_div(soup):
    for div in soup.find_all(c.DIV):
        insertA(div)
        insertImg(div)

def insertA(soup):
    for a in soup.find_all(c.HYPERLINK_A):
        if check_link_contains(a, c.HREF):
            if not (str(a.get(c.HREF)) in aHrefList):
                append_list(aHrefList,a,c.HREF)
                # if str(a.get(c.HREF)).startswith('//'):
                #     aHrefList.append('https:'+a.get(c.HREF))
                # elif str(a.get(c.HREF)).startswith('/'):
                #         aHrefList.append(c.defaulturl+a.get(c.HREF))
                # else:
                #     aHrefList.append(a.get(c.HREF))
                    # print(a.get('href'))
                    # aHrefList.append(a.get(c.HREF))

def insertImg(soup):
    for img in soup.find_all(c.IMG):
        if not( '#' in str(img.get(c.SRC))) :
            if  not ('none' in str(img.get(c.SRC)).lower()):
                if not (img.get(c.SRC) in imgsrcList):
                    if str(img.get(c.SRC)).startswith('//'):
                        imgsrcList.append('https:'+img.get(c.SRC))
                    elif str(img.get(c.SRC)).startswith('/'):
                            imgsrcList.append(c.defaulturl+img.get(c.SRC))
                    else:
                        imgsrcList.append(img.get(c.SRC))
            if  not ('none' in str(img.get(c.SRCSET)).lower()):
                if img.has_attr(c.SRCSET):
                    if not (img.get(c.SRCSET) in imgsrcList):
                        if str(img.get(c.SRCSET)).startswith('//'):
                            imgsrcsetList.append('https:'+img.get(c.SRCSET))
                        elif str(img.get(c.SRCSET)).startswith('/'):
                            imgsrcsetList.append(c.defaulturl+img.get(c.SRCSET))
                        else:
                            imgsrcsetList.append(img.get(c.SRCSET))



def queryPage(con, url):
    print(url)
    page = con.request('GET',url,headers={'User-agent':c.WINDOWS_CHROME}, redirect=True)
    # opener = urllib3.request.build_opener()
    # f = opener.open(request)
    if page.status in c.GOOD_STATUS_LIST:
        print(page.status)
        soup = BeautifulSoup(page.data, features='lxml')
        cp.createFile('miniclip', str(str(url).split("/")[2].split(".")[1]+".html"), str(soup.prettify))
        findDiv(soup)
        for line in aHrefList:
            # print("Href List:")
            print(line)

        for line1 in imgsrcList:
            # print("Image List:")
            print(line1)

        for line2 in imgsrcsetList:
            # print("Src Set List:")
            print(line2)
        # print(page.url)
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
    print("Default Path:", ext.domain)

con = init_PoolManager()
# c.defaultpath = tldextract.extract('http://forums.bbc.co.uk/')

c.defaulturl = "https://www.miniclip.com"
extractDomain()
queryPage(con, "https://www.miniclip.com/games/en/")