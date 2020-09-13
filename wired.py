from bs4 import BeautifulSoup
import requests
import random

class wired:
    def __init__(self, topics):
        self.topics = topics
        self.homepage = 'http://wired.com'
        self.article_titles = []
        self.article_contents = []
        self.article_hrefs = []

    def parse(self):
        tag = random.choice(self.topics)
        
        #print (tag)
        response = requests.get('https://www.wired.com/search/?q=' + tag + '&page=1&sort=score')
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.findAll("li", {"class": "archive-item-component"}):            
            tag_header = tag.find("h2", {"class": "archive-item-component__title"})
            tag_content = tag.find("p", {"class": "archive-item-component__desc"})
            
            article_title = tag_header.text
            article_href = tag.find("a", {"class": "archive-item-component__link"})["href"]
            article_content = tag_content.text

            self.article_titles.append(article_title)
            self.article_contents.append(article_content)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)
        length = random.randrange(length)
        
        #return None, None
        return self.article_titles[length], self.homepage + self.article_hrefs[length]