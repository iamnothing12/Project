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

urlList = []
pathdict = {}
tempsoup =""


def init_PoolManager():
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    return urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


def check_link_contains(soup, tag):
    if '#' in str(soup.get(tag)) or \
            'none' in str(soup.get(tag)).lower() or \
                not soup.has_attr(tag):
        return False
    return True


def append_list(list, soup, tag):
    if len(soup.get(tag)) > 1:
        if str(soup.get(tag)).startswith('//'):
            list.append('https:' + soup.get(tag))
            # pathdict[soup.get(tag)] = \
            extract_path(str(soup.get(tag)).replace("//","",1))
        elif str(soup.get(tag)).startswith('/'):
            list.append(c.defaultURL + soup.get(tag))
            extract_path(str(soup.get(tag)).replace("/","",1))
        elif str(soup.get(tag)).startswith('http://'):
            list.append(c.defaultURL + soup.get(tag))
            extract_path(str(soup.get(tag)).replace("http://","",1))
        elif str(soup.get(tag)).startswith('https://'):
            list.append(c.defaultURL + soup.get(tag))
            extract_path(str(soup.get(tag)).replace("https://","",1))
        else:
            list.append(soup.get(tag))
            extract_path(str(soup.get(tag)))

def extract_path(url):
    extractlink = tldextract.extract(url)
    print("URL: " +str(url))
    print("Extracted Link: " + str(extractlink))
    domainPath= str(str(extractlink.subdomain) + "/" + str(extractlink.registered_domain).replace(".", "/"))
    print("Domain: [ " + domainPath + " ] ")
    striplink = str(url).lstrip(str(extractlink.subdomain))
    striplink = str(striplink).lstrip(".")
    striplink = str(striplink).lstrip(str(extractlink.registered_domain))
    print("Clean Stripped: "+str(striplink))
    if len(striplink) > 1:
        print("Status: " + str(str(striplink).endswith("/")))
        url_list = striplink.split("/")
        if str(striplink).endswith("/"):
            value = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(url_list[len(url_list) - 2]))
            print("File name: %s" % value)
        else:
            value = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(url_list[len(url_list) - 1]))
            print("File name: %s" % value)
        pathstrip = re.sub(r'[^\w!@#$%^&_+=,.;\'()/{}[\]\-]', '', str(striplink))
        fullstrip = pathstrip.strip(value)
        if str(fullstrip).startswith("/"):
            fullpath = str(c.defaultPath + fullstrip)
        else:
            fullpath = str(c.defaultPath +"/"+ fullstrip)
        print("Full Path: %s" % fullpath)
        if not str(url) in pathdict:
            pathdict[str(url)] = {}
        if "." in value:
            pathdict[str(url)][str(fullpath)] = value
        else:
            pathdict[str(url)][str(fullpath)] = str(value+".html")


def find_div(soup):
    for div in soup.find_all(c.DIV):
        insert_a(div)
        insert_img(div)
        find_iframe(div)

def find_link(soup):
    for link in soup.find_all(c.LINK):
        if check_link_contains(link, c.HREF):
            if not (str(link.get(c.HREF)) in urlList):
                append_list(urlList, link, c.HREF)
def find_script(soup):
    for script in soup.find_all(c.SCRIPT):
        if check_link_contains(script, c.SRC):
            if not script.get(c.SRC) in urlList:
                append_list(urlList, script, c.SRC)


def find_iframe(soup):
    for iframe in soup.find_all(c.IFRAME):
        if check_link_contains(iframe, c.SRC):
            if not iframe.get(c.SRC) in urlList:
                append_list(urlList, iframe, c.SRC)


def find_span(soup):
    for span in soup.find_all(c.SPAN):
        if check_link_contains(span, c.SRC):
            if not span.get(c.SRC) in urlList:
                append_list(urlList, span, c.SRC)


def insert_a(soup):
    for a in soup.find_all(c.HYPERLINK_A):
        if check_link_contains(a, c.HREF):
            if not (str(a.get(c.HREF)) in urlList):
                append_list(urlList, a, c.HREF)


def insert_img(soup):
    for img in soup.find_all(c.IMG):
        if check_link_contains(img, c.SRC):
            if not (img.get(c.SRC) in urlList):
                append_list(urlList, img, c.SRC)
        if check_link_contains(img, c.SRCSET):
            if not (img.get(c.SRCSET) in urlList):
                append_list(urlList, img, c.SRCSET)


def createPage(url, path):
    updateurl = url
    if not str(updateurl).startswith("http"):
        if str(updateurl).startswith("//"):
            updateurl = "https:"+str(url)
        elif str(updateurl).startswith("/"):
            updateurl = str(c.defaultURL)+str(updateurl)
        else:
            updateurl = str(c.defaultURL) +"/" +str(updateurl)
    print(updateurl)
    page_con = con.request('GET', updateurl, headers={'User-agent':c.WINDOWS_CHROME}, redirect=True)
    if page_con.status in c.GOOD_STATUS_LIST:
        souplink = BeautifulSoup(page_con.data, features='lxml')
        cp.createFile(path, pathdict[url][path], str(souplink.prettify()))
        # if "." in pathdict[url][path]:
        #     cp.createFile(path, pathdict[url][path], str(souplink.prettify()))
        # else:
        #     cp.createFile(path, str(pathdict[url][path]+ ".html"), str(souplink.prettify()))
    # pagelinks = con.request('GET', line, headers={'User-agent': c.WINDOWS_CHROME}, redirect=True)
    # if pagelinks.status in c.GOOD_STATUS_LIST:
    #     extractlink = tldextract.extract(line)
    #     print("Extract link: %s" % extractlink.registered_domain)
    #     print("Suffix: %s" % str(extractlink.suffix))
    #     if str(line).startswith("http://"):
    #         striplink = str(line).lstrip("http://")
    #         striplink = str(striplink).lstrip(str(extractlink.subdomain))
    #         striplink = str(striplink).lstrip(".")
    #         striplink = str(striplink).lstrip(str(extractlink.registered_domain))
    #         if striplink.startswith(extractlink.suffix):
    #             striplink = str(striplink).lstrip(".")
    #             striplink = str(striplink).lstrip(str(extractlink.suffix))
    #     else:
    #         striplink = str(line).lstrip("https://")
    #         striplink = str(striplink).lstrip(str(extractlink.subdomain))
    #         striplink = str(striplink).lstrip(".")
    #         striplink = str(striplink).lstrip((str(extractlink.registered_domain)))
    #         if striplink.startswith(extractlink.suffix):
    #             striplink = str(striplink).lstrip(".")
    #             striplink = str(striplink).lstrip(str(extractlink.suffix))
    #         # if not striplink.endswith('/'):
    #         #     print ("Ends With [/]: %s" %striplink.rsplit('/'))
    #         # striplink = str(line).lstrip(str("https://" + str(extractlink.subdomain) + str(extractlink.registered_domain) + str(extractlink.suffix)))
    #     print("Strip Link: %s" % striplink)
    #     print("Default Path: %s" % c.defaultPath)
    #
    #     url_list = striplink.split("/")
    #     value = ""
    #     if len(striplink) > 1:
    #         souplink = BeautifulSoup(pagelinks.data, features='lxml')
    #         print("Status: " + str(str(striplink).endswith("/")))
    #         if str(striplink).endswith("/"):
    #             value = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(url_list[len(url_list) - 2]))
    #             print("File name: %s" % value)
    #         else:
    #             value = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(url_list[len(url_list) - 1]))
    #             print("File names: %s" % value)
    #         pathstrip = re.sub(r'[^\w!@#$%^&_+=,.;\'()/{}[\]\-]', '', str(striplink))
    #         fullstrip = pathstrip.strip(value)
    #         fullpath = str(c.defaultPath + fullstrip)
    #         print("Full Path: %s" % fullpath)
    #         print("Line: %s " % line)
    #         if "." in value:
    #             cp.createFile(fullpath, str(value), str(souplink.prettify()))
    #             pathdict[line]= str(fullpath + value)
    #         else:
    #             cp.createFile(fullpath, str(str(value) + ".html"), str(souplink.prettify()))
    #             pathdict[line] = str(fullpath + value+".html")


def queryPage(con, url):

    print(url)
    page = con.request('GET', url, headers={'User-agent': c.WINDOWS_CHROME}, redirect=True)

    # opener = urllib3.request.build_opener()
    # f = opener.open(request)
    if page.status in c.GOOD_STATUS_LIST:
        print(page.status)
        soup = BeautifulSoup(page.data, features='lxml')
        tempsoup = soup.prettify
        find_script(soup)
        find_link(soup)
        find_div(soup)
        find_iframe(soup)
        find_span((soup))
        insert_a(soup)
        # find_script(soup.head)
        # find_link(soup.head)
        print("Url Link: %i" % len(urlList))
        for urlLine in pathdict:
            print(urlLine)
            for path in pathdict[str(urlLine)]:
                print("Path: " + path)
                print("FileName: " + pathdict[str(urlLine)][str(path)])
                createPage(urlLine,path)
                if str(urlLine) in str(tempsoup):
                    tempsoup = str(tempsoup).replace(urlLine,str(str(path)+str(pathdict[str(urlLine)][str(path)])))
            print("Url Link: %i" % len(urlList))
            print("Replace Link: %s" %urlLine,str(str(path)+str(pathdict[str(urlLine)][str(path)])))
        # print("TEMPSOUP: "+str(tempsoup))
        # for urlLine in urlList:
        #     print("LINK : "+ urlLine)
        #     createPage(urlLine)
        # tempsoup = soup.prettify()
        # for link,path in pathdict.items():
        #     tempsoup = tempsoup.replace(str(link), str(path))
        print("Default Filename: "+str(str(url).split("/")[2].split(".")[1] + ".html"))
        cp.createFile(c.defaultPath, str(str(url).split("/")[2].split(".")[1] + ".html"), str(tempsoup))


    elif page.status in c.REDIRECT_STATUS_LIST:
        print(page.status)
    elif page.status in c.BAD_STATUS_LIST:
        print(page.status)
    elif page.status in c.SERVER_ERROR_STATUS_LIST:
        print(page.status)


def extractDomain():
    ext = tldextract.extract(c.defaultURL)
    c.defaultPath = ext.domain
    print("Default Path: ", c.defaultPath)
    # print(c.defaultURL)
    # print("Something: ",ext.subdomain,ext.domain,ext.suffix)
    # url_parts = (u.subdomain, u.domain, u.suffix, rest)

    # print("Default Path:", ext.domain)


con = init_PoolManager()
# c.defaultpath = tldextract.extract('http://forums.bbc.co.uk/')

c.defaultURL = "https://www.miniclip.com"
extractDomain()
queryPage(con, "https://www.miniclip.com/games/en/")
