from bs4 import BeautifulSoup
import requests
import random

class robotiq:
    def __init__(self):
        self.homepage = 'https://blog.robotiq.com/'
        self.article_titles = []
        self.article_hrefs = []

    def parse(self):       
        #print (tag)
        response = requests.get(self.homepage)
        soup = BeautifulSoup(response.text, 'html.parser')

        for articleList in soup.findAll("div", {"class": "bloglisting-box"}):
            article = articleList.find("bloglisting-bcontent")
            print (articleList)
            article_title = article.find("a").text
            article_href = article.find("a")["href"]

            self.article_titles.append(article_title)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)
        print (length)
        length = random.randrange(length)
        #return None, None
        return self.article_titles[length], self.homepage + self.article_hrefs[length]