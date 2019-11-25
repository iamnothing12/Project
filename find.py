from bs4 import BeautifulSoup
import config as c
import tldextract
import re
count = 0
local_count = 0
total_count = 0
#Error Url Checking
def check_link_contains(soup, tag):
    if '#' in str(soup.get(tag)) or \
            'none' in str(soup.get(tag)).lower() or \
                not soup.has_attr(tag):
        return False
    return True

# Add url to list (Not needed actually)
def append_list(soup, tag):
    if len(soup.get(tag)) > 1:
        if str(soup.get(tag)).startswith('//'):
            c.urlList.append('https:' + soup.get(tag))
            print("[//]: [ " +str(soup.get(tag))+ " ]")
        elif str(soup.get(tag)).startswith('/'):
            c.urlList.append(c.defaultURL + soup.get(tag))
            print("[/]: [ " + str(soup.get(tag)) + " ]")
        elif str(soup.get(tag)).startswith('http://'):
            c.urlList.append(soup.get(tag))
            print("[http://]: [ " + str(soup.get(tag)) + " ]")
        elif str(soup.get(tag)).startswith('https://'):
            c.urlList.append(soup.get(tag))
            print("[https://]: [ " + str(soup.get(tag)) + " ]")
        else:
            c.urlList.append(soup.get(tag))
            print("[everything else]: [ " + str(soup.get(tag)) + " ]")
        print("SRC: [ %s ]" % soup.get(tag))
        local_path(soup.get(tag))
        global count
        count += 1

#Format Link Path to local
def local_path(url):
    tempurl = url
    if url.startswith("//"):
        tempurl = tempurl.replace("//","https://",1)
    elif url.startswith("/"):
        tempurl = tempurl.replace("/", c.defaultURL+"/",1)
    else:
        tempurl = tempurl
    c.pathdict[url] = {}
    c.pathdict[url][tempurl] = {}
    extract_path(url,tempurl)

    # filename = extract_filename(url)
    # c.pathdict[tempurl][path] = filename

#Extract path
def extract_path(url,tempurl):
    filterurl = tempurl
    # print("Clean Url: [ "+ url + " ]")
    # print("Extracting Url: [ "+ tempurl+" ]")
    ext = tldextract.extract(url)
    # print("Ext sub-Domain.Domain.suffix: [ "+ str(ext.subdomain)+"."+str(ext.domain)+"."+ str(ext.suffix) +" ]")
    if str(filterurl).startswith("https://"): #Stripping url headers
        filterurl = str(filterurl).replace("https://","",1)
    else:
        filterurl = str(filterurl).replace("http://", "", 1)
    filterurl = str(filterurl).replace(str(str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix)), "", 1)
    # print("Filtered url: [ "+str(filterurl)+" ]")

    # Special case: for example only http://www.miniclip.com
    if len(filterurl) < 1:
        if not tempurl in c.pathdict[url]:
            c.pathDict[url][tempurl] ={}
            c.pathdict[url][tempurl][c.defaultPath+"/"+str(ext.subdomain)+"/"+str(str(ext.domain).replace(".","/"))] = str(ext.suffix)+".html"

    else:
        if not tempurl in c.pathdict[url]: # Check if url path created
            c.pathdict[url][tempurl] = {}

        if str(filterurl).endswith("/") and str(filterurl).count("/") == 2: #Determine start and end only contain /something/ will be converted to filename in the default folder
            # print("Count 2: [ " +str(filterurl) + " ] ")
            extract_filename(url, tempurl, filterurl, 0)
        elif str(filterurl).endswith("/") :
            extract_filename(url, tempurl, filterurl, 1)
        else:
            extract_filename(url, tempurl, filterurl, 2)


def extract_filename(url,tempurl,filterurl, type):
    global local_count
    local_count += 1
    if type == 0:
        # print("Type0: [ " +str(type)+" ] Path: [ "+ c.defaultPath+ " ] Filename: [ "+str(filterurl).strip("/")+" ]")
        c.pathdict[url][tempurl][c.defaultPath] = str(str(filterurl).strip("/"))+".html"
    elif type == 1:
        templist = str(filterurl).split("/")
        filename = str(templist[len(templist)-2])
        # print("Type1: [ " + str(type) + " ] Path: [ "+ c.defaultPath+str(filterurl).strip(filename)+ " ] Filename: [ "+filename+".html"+" ]")
        c.pathdict[url][tempurl][c.defaultPath+str(filterurl).strip(filename)] = filename+".html"
    else:
        templist = str(filterurl).split("/")
        filename = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(templist[len(templist) - 1]))
        # print("Type2: [ " + str(type) + " ] Path: [ "+ c.defaultPath+str(filterurl).strip(filename) + " ]  Filename: [ " + filename+ ".html" + " ]")
        if "." in filename:
            c.pathdict[url][tempurl][c.defaultPath + str(str(filterurl).strip(filename))] = filename
        else:
            c.pathdict[url][tempurl][c.defaultPath + str(str(filterurl).strip(filename))] = filename+".html"
        # return value+".html"
        # return str(filterurl).strip("/")

def find_div(soup):
    for div in soup.find_all(c.DIV):
        insert_a(div)
        insert_img(div)
        find_iframe(div)

def find_link(soup):
    for link in soup.find_all(c.LINK):
        if check_link_contains(link, c.HREF):
            if not (str(link.get(c.HREF)) in c.urlList):
                append_list(link, c.HREF)
def find_script(soup):
    for script in soup.find_all(c.SCRIPT):
        if check_link_contains(script, c.SRC):
            if not script.get(c.SRC) in c.urlList:
                append_list(script, c.SRC)


def find_iframe(soup):
    for iframe in soup.find_all(c.IFRAME):
        if check_link_contains(iframe, c.SRC):
            if not iframe.get(c.SRC) in c.urlList:
                append_list(iframe, c.SRC)


def find_span(soup):
    for span in soup.find_all(c.SPAN):
        if check_link_contains(span, c.SRC):
            if not span.get(c.SRC) in c.urlList:
                append_list(span, c.SRC)


def insert_a(soup):
    for a in soup.find_all(c.HYPERLINK_A):
        if check_link_contains(a, c.HREF):
            if not (str(a.get(c.HREF)) in c.urlList):
                append_list(a, c.HREF)

def insert_img(soup):
    for img in soup.find_all(c.IMG):
        if check_link_contains(img, c.SRC):
            if not (img.get(c.SRC) in c.urlList):
                append_list(img, c.SRC)
        if check_link_contains(img, c.SRCSET):
            if not (img.get(c.SRCSET) in c.urlList):
                append_list(img, c.SRCSET)



def find_all_link(soup):
    #Find Head Link
    find_script(soup.head)
    find_link(soup.head)
    find_div(soup.head)
    find_iframe(soup.head)
    find_span(soup.head)
    insert_a(soup.head)
    find_script(soup)
    find_link(soup)
    find_div(soup)
    find_iframe(soup)
    find_span((soup))
    insert_a(soup)

def display_link():
    global total_count
    global local_count
    global count
    for clean in c.pathdict:
        for temp in c.pathdict[clean]:
            for path in c.pathdict[clean][temp]:
                print("Link: [ "+str(c.pathdict[clean][temp][path])+" ]")
                total_count+=1
    print("Total Count Link: [ "+str(total_count)+" ]")
    print("Local Count Link: [ " +str(local_count)+ " ] ")
    print("Count Link: [ " + str(count) + " ] ")
    # for link in c.urlList:
    #     print("Link: [ "+str(link)+" ]")
    print("Total Link: [ "+str(len(c.urlList))+" ]")