from bs4 import BeautifulSoup
import requests
import random

class thenextweb:
    def __init__(self, topics):
        self.topics = topics
        self.homepage = 'http://thenextweb.com'
        self.article_titles = []
        self.article_hrefs = []

    def parse(self):
        tag = random.choice(self.topics)
        
        #print (tag)
        response = requests.get('https://thenextweb.com/?q=' + tag)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.findAll("div", {"class": "search"})
        print (soup)
        for tag in soup.findAll("li", {"class": "search-result"}):
            print ('Hi')
            tag_header = tag.find("h4", {"class": "search-result-title"})
            print (tag_header)
            article_title = tag_header.text
            article_href = tag_header["href"]

            self.article_titles.append(article_title)
            self.article_hrefs.append(article_href)

        print (self.article_titles[0])
        print (self.article_hrefs[0])
        length = len(self.article_titles)
        
        #return None, None
        return self.article_titles[random.randrange(length)], self.homepage + self.article_hrefs[random.randrange(length)]