import urllib3

robotDict = {"Sitemap":[]}
http = urllib3.PoolManager()


def get_robot(url):
    r =  http.request('GET',url)
    currentUserAgent=""
    # print(r.data)
    for line in str(r.data)[2:-1].split('\\n'):
        if "User-agent" in line:
            print(line.split(' ')[0])
            print (line.split(' ')[-1])
            robotDict[str(line)]= {"Allow":[],"Disallow":[],"Crawl-Delay":[]}
            currentUserAgent=line
        elif "Allow" in line:
            robotDict[currentUserAgent]["Allow"].append(line.split(' ')[-1])
        elif "Disallow" in line:
            robotDict[currentUserAgent]["Disallow"].append(line.split(' ')[-1])
        elif "Crawl-Delay" in line:
            robotDict[currentUserAgent]["Crawl-Delay"].append(line.split(' ')[-1])
        elif "Sitemap" in line:
            robotDict["Sitemap"].append((line.split(' ')[-1]))
            
    
    print(robotDict["User-agent: *"])
    print(" ")
    print(robotDict["User-agent: AdsBot-Google"])
    print(" ")
    print(robotDict["User-agent: Twitterbot"])
    print(" ")
    print(robotDict["User-agent: facebookexternalhit"])
    print(" ")
    print(robotDict["Sitemap"])



get_robot("http://www.google.com/robots.txt")