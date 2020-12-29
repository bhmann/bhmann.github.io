import bs4
from bs4 import BeautifulSoup
import requests
import urllib3

decurl = "https://decsearch.usaid.gov/search?client=dec_pdfs&site=default_collection&emdstyle=true&output=xml_no_dtd&proxystylesheet=dec_pdfs&ie=UTF-8&oe=UTF-8&getfields=*&ulang=en&filter=0&proxyreload=1&as_q=quarterly&num=100&btnG=Google+Search&as_epq=&as_oq=&as_eq=&lr=&as_ft=i&as_filetype=&as_occt=any&ip=172.16.1.4&access=p&entqr=3&entqrm=0&entsp=a__dec_results_biasing&wc=200&wc_mc=1&ud=1&sort=date%3AD%3AS%3Ad1&start="
i=100
urls=[]
while i<10001:
    decurlappend=decurl+str(i)
    resp = requests.get(decurlappend)
    txt=resp.text
    soup=BeautifulSoup(txt,"html.parser")

    for h in soup.findAll('p'):
        try:
            urls.append(h.find('a').attrs['href'])
        except:
            pass
    #print (urls)
    for url in urls:
        if url.find('href='):
            fileName= url.rsplit('/', 1)[1]

        r = requests.get(url)
        with open(fileName, "wb") as code:
            code.write(r.content)
    i=i+100
