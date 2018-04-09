from bs4 import BeautifulSoup
import requests

//urls yet to visit
queue=["https://ehealthforum.com"]

//list of all the visited urls
seen=[]

count=1;
domain="ehealthforum.com"
while queue:
    url=queue.pop(0)
    if url:
        if url in seen or domain not in url or 'javascript:' in url:
            continue

        seen.append(url)
                
        print(str(count)+ " "+url,end="\n")
        count+=1

        html=requests.get(url)
        htmlData=html.text
        soup = BeautifulSoup(htmlData,"html.parser")

        for link in soup.find_all('a'):
            href=link.get('href')
            queue.append(href)
        
        
