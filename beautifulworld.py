from bs4 import BeautifulSoup
import urllib3
import re

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

def querySite(url):
    if matchurlPattern(url):
        print("Correct URL Format: [ %s ]" % url)
    else:
        print("Wrong URL Format: [ %s ]" % url)

querySite("www.google.com")
querySite("https://www.google.com/")