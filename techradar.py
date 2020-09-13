from bs4 import BeautifulSoup
import requests
import random

class techradar:
    def __init__(self, topics):
        self.topics = topics
        self.homepage = 'http://techradar.com'
        self.article_titles = []
        self.article_hrefs = []

    def parse(self):
        tag = random.choice(self.topics)
        
        #print (tag)
        response = requests.get('https://www.techradar.com/search?searchTerm=' + tag)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.findAll("div", {"class": "listingResult small result" + str(random.randrange(20))}):
            tag_header = tag.find("a", {"class": "article-link"})
            article_title = tag_header.find("h3", {"class": "article-name"}).text
            article_href = tag_header["href"]

            self.article_titles.append(article_title)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)
        
        #return None, None
        return self.article_titles[random.randrange(length)], self.article_hrefs[random.randrange(length)]