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


# initialize ssl connection
def init_pool_manager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


# Extract domain name
def extract_base_domain():
    ext = tldextract.extract(c.defaultURL)
    c.defaultPath = ext.domain
    c.domainName = str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix)
    print("Default Path: ", c.defaultPath)
    print("Domain name: ", c.domainName)

def extract_domain(url):
    ext = tldextract.extract(url)
    print("Domain: [" +str(str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix))+ " ] ")
    return ext  # str(str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix))


def link_converter(link):
    templink = ""
    if str(link).startswith('//'):
        templink = "https:" + str(link)
        # c.urlList.append('https:' + soup.get(tag))
        # print("[//]: [ " +"https:"+str(link)+ " ]")
    elif str(link).startswith('/'):
        templink = c.defaultURL + str(link)
        # print("[/]: [ " + c.defaultURL +str(link) + " ]")
        # c.urlList.append(c.defaultURL + soup.get(tag))
        # print("[/]: [ " + str(soup.get(tag)) + " ]")
    else:  # http:// or https:// will faill into this category
        templink = str(link)
        # c.urlList.append(soup.get(tag))
        # print("[http://]: [ " + str(link) + " ]")
    c.pathdict[link][templink] = {}
    return templink

def path_converter(link,templink):
    domain = extract_domain(templink)
    temp_link = templink
    strip_link = temp_link.replace("https://", "", 1)
    strip_link = strip_link.replace(domain.subdomain+"."+domain.domain+"."+domain.suffix, "", 1)
    print("Temp Link: [ " +templink+" ]")
    print("Stripped: [ " +str(strip_link)+ " ] ")
    if len(strip_link) > 1:
        if strip_link.endswith("/"):
            filename = str(strip_link).split("/")
            filename = filename[len(filename)-2]
            print("Filename: [ " + filename + " ] ")
            path = str(strip_link).strip(filename)

            if len(path) > 1:
                print("Path: [ " + c.defaultPath + path + " ]")
                if not str(c.defaultPath+str(path)) in  c.pathdict[link][templink]:
                    c.pathdict[link][templink][c.defaultPath+str(path)] = []
                c.pathdict[link][templink][c.defaultPath+str(path)].append(filename+".html")
            else:
                print("Path: [ " + c.defaultPath + path + " ]")
                c.pathdict[link][templink][c.defaultPath] = filename+".html"
        else:
            filename = str(strip_link).split("/")
            path = str(strip_link).strip(str(filename[len(filename) - 1]))
            filename = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(filename[len(filename) - 1]))
            print("Filename: [ " + filename + " ] ")
            print("Path2: [ " + c.defaultPath + str(path) + " ]")
            if not str(c.defaultPath +str(path)) in c.pathdict[link][templink]:
                c.pathdict[link][templink][c.defaultPath + str(path)] = []
            c.pathdict[link][templink][c.defaultPath + str(path)].append(filename + ".html")
    else:
        print("nandey")
        strip_link = temp_link.replace("https://", "", 1)
        path = str("/"+str(domain.subdomain) + "/" + str(domain.domain) + "/")
        print("Path3: [ " + c.defaultPath + str(path) + " ]")
        if not str(c.defaultPath + str(path)) in c.pathdict[link][templink]:
            c.pathdict[link][templink][c.defaultPath + str(path)] = []
        c.pathdict[link][templink][c.defaultPath + str(path)].append(str(domain.suffix) + ".html")

# Connect Main Page
def query_main(con):
    # c.defaultURL
    request_page = con.request('GET', str(c.defaultURL), headers={'User-agent': c.WINDOWS_CHROME}, redirect=True)
    if request_page.status in c.GOOD_STATUS_LIST:
        c.urlList.append(c.defaultURL)
        print("Status: [" + str(request_page.status) + "]")
        soup = BeautifulSoup(request_page.data, features='lxml')
        f.find_all_link(soup)
        # f.display_link()
        for link in c.urlList:
            print("Link: [ " + link + " ]")
            c.pathdict[str(link)] = {}
            templink = link_converter(link)  # Create proper links
            path_converter(link, templink)

        print("Total Link: [ " + str(len(c.urlList)) + " ] ")
        count = 0
        for link in c.pathdict:
            for templink in c.pathdict[link]:
                for path in c.pathdict[link][templink]:
                    for file in c.pathdict[link][templink][path]:
                        request_page = con.request('GET', str(c.defaultURL), headers={'User-agent': c.WINDOWS_CHROME},
                                                   redirect=True)
                        if request_page.status in c.GOOD_STATUS_LIST:
                            souplink = BeautifulSoup(request_page.data, features='lxml')
                            cp.createFile(path, file, str(souplink.prettify()))
                            if link in tempsoup:
                            count+=1
        print("Total Link: [ " + str(count) + " ] ")
# Main call
con = init_pool_manager()
c.defaultURL = "https://www.miniclip.com/games/en"
extract_base_domain()
query_main(con)
# queryPage(con, "https://www.miniclip.com/games/en/")
