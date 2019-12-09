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
    c.defaultFile = ext.domain+".html"
    c.domainName = str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix)
    print("Default Path: ", c.defaultPath)
    print("Domain name: ", c.domainName)
    print("File name: ", c.defaultFile)


def extract_domain(url):
    ext = tldextract.extract(url)
    # print("Domain: [" +str(str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix))+ " ] ")
    return ext  # str(str(ext.subdomain) + "." + str(ext.domain) + "." + str(ext.suffix))


def link_converter(link):
    templink = ""
    if str(link).startswith('//'):
        templink = "https:" + str(link)
    elif str(link).startswith('/'):
        templink = c.defaultURL + str(link)
    else:  # http:// or https:// will faill into this category
        templink = str(link)
    c.pathdict[link][templink] = {}
    return templink

def path_converter(link,templink, tempsoup):
    #extract domain from templink
    domain = templink.split("//")[-1].split("/")[0].split('?')[0]
    # domain = extract_domain(templink)
    # linkDomain = domain.subdomain+"."+domain.domain+"."+domain.suffix
    # subDomain = domain.subdomain+"/"+domain.domain+"/"+domain.suffix
    #Strip link from http://domain/something to  /something
    temp_link = templink
    strip_link = temp_link.replace("https://", "", 1)
    # strip_link = strip_link.replace(domain.subdomain+"."+domain.domain+"."+domain.suffix, "", 1)
    #Check for different domain
    if domain in c.domainName:
        strip_link = strip_link.replace(domain, "", 1)

    folderpath=""
    path =""
    filename =""
    tempquery =""
    if len(strip_link) > 1:
        filename = str(strip_link).split("/")
        if strip_link.endswith("/"):
            filename = filename[len(filename)-2]
        else:
            filename = filename[len(filename) - 1]
        if "?" in filename:
            tempquery = str(filename).split("?")[-1]
            print("Temp Query:" +tempquery)
            filename = str(filename).strip(tempquery)
            tempquery = "?"+tempquery
        filename = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', filename)

        path = strip_link.strip(filename+tempquery)
        path = re.sub(r'[^\w!@#$%^&_+=/,.;\'(){}[\]\-]', '', str(path))
        
        path = path.replace("//","/")
        if len(path) >1:
            if not path.startswith("/"):
                folderpath = "/"+path
            folderpath = c.defaultPath+folderpath
        else:
            folderpath = c.defaultPath

        if not str(folderpath) in  c.pathdict[link][templink]:
            c.pathdict[link][templink][folderpath] = {}
        if not str(path) in c.pathdict[link][templink][folderpath]:
            c.pathdict[link][templink][folderpath][path] = []
        

        if "." in filename:
            c.pathdict[link][templink][folderpath][path].append(filename)
        else:
            c.pathdict[link][templink][folderpath][path].append(filename+".html")
        
    else:
        print("very bad")
    print("Path: "+path)
    print("Filename: "+filename)
    tempsoup = tempsoup.replace("\""+link+"\"","\""+path+filename+tempquery+"\"",1)
    return tempsoup
    # if len(strip_link) > 1:
    #     if strip_link.endswith("/"):
    #         filename = str(strip_link).split("/")
    #         filename = filename[len(filename)-2]
    #         path = re.sub(r'[^\w!@#$%^&_+=/,.;\'(){}[\]\-]', '',str(strip_link).strip(filename))
    #         if not str(path).startswith("/"):
    #             path = "/"+path
    #         if len(path) > 1:
    #             print("Path1.0: [ " + c.defaultPath + path + " ]")
    #             if not str(c.defaultPath+str(path)) in  c.pathdict[link][templink]:
    #                 c.pathdict[link][templink][c.defaultPath+str(path)] = []
    #             if "." in filename:
    #                 c.pathdict[link][templink][c.defaultPath+str(path)].append(filename)
    #             else:
    #                 c.pathdict[link][templink][c.defaultPath+str(path)].append(filename+".html")
    #         else:
    #             print("Path1.1: [ " + c.defaultPath + path + " ]")
    #             c.pathdict[link][templink][c.defaultPath] = filename+".html"
    #     else:
    #         filename = str(strip_link).split("/")
    #         # path = str(strip_link).strip(str(filename[len(filename) - 1]))
    #         path = re.sub(r'[^\w!@#$%^&_+=/,.;\'(){}[\]\-]', '', str(strip_link).strip(str(filename[len(filename) - 1])))
    #         if not str(path).startswith("/"):
    #             path = "/"+path
    #         filename = re.sub(r'[^\w!@#$%^&_+=,.;\'(){}[\]\-]', '', str(filename[len(filename) - 1]))
    #         # print("Filename: [ " + filename + " ] ")
    #         print("Path2: [ " + c.defaultPath + str(path) + " ]")
    #         if not str(c.defaultPath +str(path)) in c.pathdict[link][templink]:
    #             c.pathdict[link][templink][c.defaultPath + str(path)] = []
    #         if "." in filename:
    #             c.pathdict[link][templink][c.defaultPath + str(path)].append(filename)
    #         else:
    #             c.pathdict[link][templink][c.defaultPath + str(path)].append(filename + ".html")
    # else:
    #     print("nandey")
    #     strip_link = temp_link.replace("https://", "", 1)
    #     path = str("/"+str(domain.subdomain) + "/" + str(domain.domain) + "/")
    #     print("Path3: [ " + c.defaultPath + str(path) + " ]")
    #     if not str(c.defaultPath + str(path)) in c.pathdict[link][templink]:
    #         c.pathdict[link][templink][c.defaultPath + str(path)] = []
    #     c.pathdict[link][templink][c.defaultPath + str(path)].append(str(domain.suffix))

# Connect Main Page
def query_main(con):
    # c.defaultURL
    request_page = con.request('GET', str(c.defaultURL), headers={'User-agent': c.WINDOWS_CHROME,"X-Requested-With": "XMLHttpRequest"}, redirect=True)
    if request_page.status in c.GOOD_STATUS_LIST:
        c.urlList.append(c.defaultURL)
        print("Status: [" + str(request_page.status) + "]")
        soup = BeautifulSoup(request_page.data, features='lxml')
        f.find_all_link(soup)
        # f.display_link()
        tempsoup = soup.prettify()
        for link in c.urlList:
            print("Link: [ " + link + " ]")
            c.pathdict[str(link)] = {}
            templink = link_converter(link)  # Create proper links
            tempsoup = path_converter(link, templink, tempsoup)
        cp.createFile(c.defaultPath, c.defaultFile, str(tempsoup))
        print("Total Link: [ " + str(len(c.urlList)) + " ] ")
        count = 0
        tempsoup = soup.prettify;
        for link in c.pathdict:
            for templink in c.pathdict[link]:
                for folderpath in c.pathdict[link][templink]:
                    for path in c.pathdict[link][templink][folderpath]:
                        for file in c.pathdict[link][templink][folderpath][path]:
                            request_page = con.request('GET', str(templink), headers={'User-agent': c.WINDOWS_CHROME,"X-Requested-With": "XMLHttpRequest"},
                                                    redirect=True)
                            if request_page.status in c.GOOD_STATUS_LIST:
                                souplink = BeautifulSoup(request_page.data, features='lxml')
                                cp.createFile(folderpath, file, str(souplink.prettify()))
                                if link in soup.prettify():
                                    print("Path: " +link)
                                    print("URL: " + templink)
                                    print("Dir Path: " + path)
                                    print("Filename: " + file)
                                    # tempsoup = str(tempsoup).replace(link, path+file)
                                    count+=1
        # cp.createFile(c.defaultPath, "miniclip.html", str(tempsoup))
        print("Total Link: [ " + str(count) + " ] ")
# Main call
con = init_pool_manager()
c.defaultURL = "https://www.google.com/"
extract_base_domain()
query_main(con)
# queryPage(con, "https://www.miniclip.com/games/en/")
