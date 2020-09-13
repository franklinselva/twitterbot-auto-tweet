from bs4 import BeautifulSoup
import requests
import random

class robohub:
    def __init__(self):
        self.homepage = 'http://robohub.org'
        self.article_titles = []
        self.article_hrefs = []

    def parse(self):       
        #print (tag)
        response = requests.get(self.homepage)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.findAll("div", {"class": "roundedge cpxframex"}):
            tag_header = tag.find("div", {"class": " cpxtitlex"})
            print (tag_header)
            article = tag_header.find("h3")
            article_title = article.find("a").text
            article_href = article.find("a")["href"]

            self.article_titles.append(article_title)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)
        
        #return None, None
        return self.article_titles[random.randrange(length)], self.article_hrefs[random.randrange(length)]