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

con = init_pool_manager()
c.defaultURL = "https://www.tp.edu.sg/"
extract_base_domain()

request_page = con.request('GET', str(c.defaultURL), headers={'User-agent': c.WINDOWS_CHROME,
                                                              'Accept': 'text / html, application / xhtml + xml,application / xml;q = 0.9, * / *;q = 0.8',
                                                            'Accept-Language' : 'en-US,en;q=0.5',
                                                              'Accept-Encoding': 'gzip, deflate, br',
                                                              'Connection': 'keep-alive',
                                                                'Cookie': 'top-smartphone=appleiphone; MCSESSION_PRODUCTION=226ce28ed4673abdea2c4d43c5bc0ed3; _country_code=SG; _mc_abc49=2; MCTOKEN_PRODUCTION=226ce28ed4673abdea2c4d43c5bc0ed3; _language_code=en; MCA_VID=ODJlZWEwYzAtMTlhMC0xMWVhLWJhOWItODkyYmU2MWVhNGJl; MCA_SID=ODJlZjE1ZjAtMTlhMC0xMWVhLWJhOWItODkyYmU2MWVhNGJl; _mc_ppv=1; _fbp=fb.1.1575798778242.554671643; __gads=ID=8cf817080fcb51d8:T=1575798776:S=ALNI_MbyxiHnQCnv3KRltEslO0GXaw5TNQ',
                                                            'Upgrade-Insecure-Requests': 1,
                                                            'TE': 'Trailers'
}, redirect=True)
if request_page.status in c.GOOD_STATUS_LIST:
    c.urlList.append(c.defaultURL)
    print("Status: [" + str(request_page.status) + "]")
    soup = BeautifulSoup(request_page.data, features='lxml')
    cp.createFile(c.defaultPath, c.defaultFile, str(soup))