from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = "https://www.pythonforbeginners.com"
content = http.request('GET',url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
soup = BeautifulSoup(content.data, features='lxml')

# print(soup.prettify)

for link in soup.find_all('link'):
    print(link.get('href'))

for link in soup.find_all('a'):
    print(link.get('href'))

for link in soup.find_all('img'):
    print(link.get('src'))