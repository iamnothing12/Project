import urllib3
import urllib3.contrib.pyopenssl
import certifi
from beautifulworld import logging as logger
# from beautifulworld import get_module_logger
# logger = get_module_logger(__name__)

robotDict = {"Sitemap":[]}
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

def check_robot(url,headers):
    for robot in robotDict:
        # logger.info(str(robot))
        if 'User-agent' in robot and (headers in robot or '*' in robot):
            logger.info(str(robot))
            logger.info(str(url))
            for allow in robotDict[robot]['Disallow']:
                logger.info(str(allow))
                if allow in str(url):
                    logger.info('URl Scrappable')
                    return True
    return False

def get_robot(url):
    r =  http.request('GET',url)
    currentUserAgent=""
    # print(r.data)
    if not (url in robotDict):
        robotDict[str(url)] = {}
    for line in str(r.data)[2:-1].split('\\n'):
        if "user-agent" in line.lower():
            # print(line.split(' ')[0])
            # print (line.split(' ')[-1])
            # robotDict[str(line)]= {"Allow":[],"Disallow":[],"Crawl-Delay":[]}
            robotDict[str(line)]= {'Allow':[],'Disallow':[],'Crawl-Delay':[]}
            currentUserAgent=line
        elif "Allow" in line:
            robotDict[currentUserAgent]["Allow"].append(line.split(' ')[-1])
        elif "Disallow" in line:
            robotDict[currentUserAgent]["Disallow"].append(line.split(' ')[-1])
        elif "Crawl-Delay" in line:
            robotDict[currentUserAgent]["Crawl-Delay"].append(line.split(' ')[-1])
        elif "Sitemap" in line:
            robotDict["Sitemap"].append((line.split(' ')[-1]))
            
    
    # print(robotDict["User-agent: *"])
    # print(" ")
    # print(robotDict["User-agent: AdsBot-Google"])
    # print(" ")
    # print(robotDict["User-agent: Twitterbot"])
    # print(" ")
    # print(robotDict["User-agent: facebookexternalhit"])
    # print(" ")
    # print(robotDict["Sitemap"])



# get_robot("http://www.google.com/robots.txt")