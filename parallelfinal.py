import pygame
from pygame import display,draw,event
import os
import os.path
from os import path
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import mimetypes
from time import time as timer
from multiprocessing.pool import ThreadPool
import matplotlib.pyplot as plt
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK= (  0,   0,  0)
box = (1000, 50)

tm=[]
cm=[]
def fetch_url(entry):
    x=(1200/cnt)/20
    inc=(1200/cnt)/20
    path, uri = entry
    if not os.path.exists(path):
        r = requests.get(uri, stream=True)
        if r.status_code == 200:
            with open(path, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
                    pygame.draw.rect(screen, GREEN, pygame.Rect(0, 0,x , 50))
                    pygame.display.update()
                    x=x+inc
                tm.append(timer()-start)
    return path
def get_links(seed):
    try:
        html = urlopen(seed)
        bsObj = BeautifulSoup(html, "lxml")
        temp = []
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                l = link.attrs['href']
            
                if re.match("^/wiki*" , l):
                    l = "https://en.wikipedia.org"+l
                    temp.append(l)
                
                elif (re.match("^https:*",l) or re.match("^http:*",l) or re.match("^www*" , l)):
                    temp.append(l)
    except:
        temp = []
    return temp
print('###################### MULTITHREADED DOWNLOAD MANAGER ######################')
print('____________________________________________________________________________\n')
file = open("C:/Users/Hrithik/Desktop/urls.txt") 
line = file.read(1)
l=file.readlines()
n=l[1]
urls=[]
if line=='0':
    print('---------------------------- DOWNLOADING URLS ----------------------------')
    for i in range(int(n)):
        pygame.init()
        screen = pygame.display.set_mode(box)
        pygame.display.set_caption("Downloader Progress")
        screen.fill(WHITE)
        k=l[i+2].rstrip()
        str1="C:/Users/Hrithik/Desktop/temp/"
        response = requests.get(k)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type.partition(';')[0].strip())
        str1+=str(i+1)
        str1+=extension
        urls.append((str1,k))
elif line=='1':
    print('---------------------- WEB CRAWLING & DOWNLOADING URLS ---------------------')
    for i in range(int(n)):
        pygame.init()
        screen = pygame.display.set_mode(box)
        pygame.display.set_caption("Crawler Progress")
        screen.fill(WHITE)
        k=l[i+2].rstrip()
        response = requests.get(k)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type.partition(';')[0].strip())
        if(extension=='.htm'):
            seed = k
            frontier = [seed]
            hops = 1
            start = 0
            end = 1
            while hops>0:
                count = start
                for z in range(start,end):
                    g=get_links(frontier[z])
                    if g not in frontier:
                        frontier+=g
                    count+=1
                end = len(frontier)
                start = count
                hops-=1
            for c in range(len(frontier)):
                str1="C:/Users/Hrithik/Desktop/temp/"
                str1+=str(c+1)
                str1+=extension
                urls.append((str1,frontier[c]))
        else:
            print('INCORRECT WEB PAGE URL!!!!!')

global cnt
cnt=len(urls)        
    
"""urls = [
    ("C:/Users/Hrithik/Desktop/temp/1.html", "https://markhneedham.com/blog/2018/07/10/neo4j-grouping-datetimes/"),
    ("C:/Users/Hrithik/Desktop/temp/2.html", "https://markhneedham.com/blog/2018/07/09/neo4j-text-cannot-be-parsed-to-duration/"),
    ("C:/Users/Hrithik/Desktop/temp/3.html", "https://markhneedham.com/blog/2018/06/15/neo4j-querying-strava-graph-py2neo/"),
    ("C:/Users/Hrithik/Desktop/temp/4.html", "https://markhneedham.com/blog/2018/06/12/neo4j-building-strava-graph/"),
    ("C:/Users/Hrithik/Desktop/temp/5.html", "https://markhneedham.com/blog/2018/06/05/neo4j-apoc-loading-data-strava-paginated-json-api/"),
    ("C:/Users/Hrithik/Desktop/temp/6.html", "https://markhneedham.com/blog/2018/06/03/neo4j-3.4-gotchas-working-with-durations/"),
    ("C:/Users/Hrithik/Desktop/temp/7.html", "https://markhneedham.com/blog/2018/06/03/neo4j-3.4-formatting-instances-durations-dates/"),
    ("C:/Users/Hrithik/Desktop/temp/8.html", "https://markhneedham.com/blog/2018/06/02/neo4j-3.4-comparing-durations/"),
    ("C:/Users/Hrithik/Desktop/temp/9.html", "https://markhneedham.com/blog/2018/05/19/interpreting-word2vec-glove-embeddings-sklearn-neo4j-graph-algorithms/"),
    ("C:/Users/Hrithik/Desktop/temp/10.html", "https://markhneedham.com/blog/2018/05/11/node2vec-tensorflow/")
]"""

start = timer()
results = ThreadPool(20).imap_unordered(fetch_url, urls)
for path1 in results:
    if(path.exists(path1)):
        print(path1,"  SIZE OF FILE : ",(os.path.getsize(path1))/1024,"KB")
        cm.append(str((os.path.getsize(path1))/1024)+"KB")
    else:
        print(path1,"   The file does not exist!!!")
print('____________________________________________________________________________')
print(f"Elapsed Time: {timer() - start}")
plt.plot(tm, cm, color='g')
plt.xlabel('Time')
plt.ylabel('Size of Files')
plt.title('Time VS Size of files')
plt.show()
pygame.quit()