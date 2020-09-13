from bs4 import BeautifulSoup
import requests
import random

class robotics:
    def __init__(self):
        self.homepage = 'http://robotics.org/'
        self.article_titles = []
        self.article_hrefs = []

    def parse(self):       
        #print (tag)
        response = requests.get(self.homepage)
        soup = BeautifulSoup(response.text, 'html.parser')
        articlesList = soup.findAll("ul", {"class": "ArticleList"})

        for articleList in articlesList:
            for tag in articleList.findAll("li", {"class": "group"}):
                article = tag.find("strong")
                article_title = article.find("a").text
                article_href = article.find("a")["href"]

                self.article_titles.append(article_title)
                self.article_hrefs.append(article_href)

        length = len(self.article_titles)
        length = random.randrange(length)
        #return None, None
        return self.article_titles[length], self.homepage + self.article_hrefs[length]