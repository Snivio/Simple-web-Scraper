from bs4 import BeautifulSoup
import operator
import requests

def crawler(url):
    words=[]
    source=requests.get(url).text
    a=BeautifulSoup(source,"html.parser")
    for i in a.find_all('a', {'class': 'user-name'}):
        s=(i.string).lower().split()
        for j in s:
            words.append(j)
    clean(words)

def clean(words):
    cleanwords=[]
    for i in words:
        symbols="!@#$%^&*()_+{}|:\"<>?''"
        for j in range(0,len(symbols)):
            i=i.replace(symbols[j], "")
        if i>0:
            cleanwords.append(i)
    creatdictionary(cleanwords)

def creatdictionary(cleanwords):
    finalwordcount={}
    for i in cleanwords:
        if i in finalwordcount:
            finalwordcount[i]+=1
        else:
            finalwordcount[i]=1
    ssorting(finalwordcount)


def ssorting(finalwordcount):
    for key,value in sorted(finalwordcount.items(),key=operator.itemgetter(0)):
        print (key,value)



crawler(url= r'https://thenewboston.com/search.php?type=0&sort=reputation&page==1')