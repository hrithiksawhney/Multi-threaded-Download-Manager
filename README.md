# Multi-threaded-Download-Manager

Downloading a file is a frequently worked domain where we use the default download managers of a given browser to download a file.

While most download managers download the file from the same source, some downloading managers can likewise increase the download speeds by downloading from different sources simultaneously. 

Despite the fact that browsers may have download administrators in built as an element, they are separated by the way that they don't organize exact, finish and unbroken downloads of data. 

While some download administrators are completely fledged projects devoted to downloading any data more than at least one convention (e.g. http), many are incorporated into installers or refresh directors and used to download parts of a particular program (or set of projects), e.g. contains Google and Adobe's update.

### Introduction

Download managers were among the top applications showing a flag promotion in the UI. 

Many download managers accompany the highlights like video and sound retrieving from well-known websites like YouTube etc. They additionally can pause and resume downloads, and force speed confinements too. This highlight come exceptionally helpful in locales where power failures is an issue. 

Furthermore, a large portion of the business download chiefs can download following client arranged timetables and download in like manner. A couple of download administrators claim to build the download speed by a factor of ordinarily. 

Download managers additionally have tight integration with engines. Download speeding up, otherwise called multipart download, is a term for the strategy utilized by programming, for example, download administrators to download a solitary record by part. 

### Features:

1. This multithreaded download manager achieves a speed up on running the download in comparison to using any other download managers. 

2. The performance is better than serial downloading.

3. In case of any disconnectivity of internet, the downloader resumes the download from the point of disconnectivity.

4. The download manager is also be able to function as a crawler, to crawl the web and download all the crawled pages.

5. The time taken for different download managers is compared and a conclusion was made that multi-threaded downloading is faster on average by a factor of 5 or greater.

6. The downloader inputs links from a text file.

7. It can run in two modes: Parallel Downloader for video, audio or any other type of file and a Web Crawler mode for html pages, which spans the web-pages based on a number of hops from the given seed pages in the text file.

8. A progress bar has been implemented using pygame.

9. Matplotlib is used to plot graphs for size of files against time taken for the file.

### System Requirements:
The basic system requirements/specifications are:
- 64-bit Operating system or 32-bit Operating system
-	Python Version 3 and above
- Python libraries:
    - os
    - requests
    - Time 
    - Multiprocessing
    -	Pygame
    -	Urllib.request
    - Bs4
    -	BeautifulSoup
    -	Re
    -	Mimetypes
    -	Matplotlib

### Working:
* For Downloading URLs (Mode 0):
  1. Create a text file named "urls.txt".
  2. Type the character '0' in the first line of the file indicating the mode of the method.
  3. Next, type the number of urls n, to be entered, in the next line.
  4. In the next n lines, type the urls line by line.

<p align="center">
  <img src="https://user-images.githubusercontent.com/44416769/88453116-f41f0c80-ce81-11ea-9af3-7b4354e956de.png" title="Input text file for Downloading URLs with mode input as 0 and 10 URLs">
</p>

* For Web Crawling and downloading URLs (Mode 1):
  1. Create a text file named "urls.txt".
  2. Type the character '1' in the first line of the file indicating the mode of the method.
  3. Next, type the number of hops n, to be entered, in the next line.
  4. Starting from the next line, type the urls line by line. 
  
* Create a temporary folder for downloading all the URLs in it.
* Replace the given paths for the file 'urls.txt' and 'temp' folder in the given codes.
* Run the 'serialfinal.py' file to download the urls in a serial manner.
* Then run the 'parallelfinal.py' file to download the urls in a parallel manner.
