from bs4 import BeautifulSoup
import requests
import random

class techcrunch:
    def __init__(self, topics):
        self.topics = topics
        self.homepage = 'http://techcrunch.com/tag/'
        self.article_titles = []
        self.article_contents = []
        self.article_hrefs = []

    def parse(self):
        tag = random.choice(self.topics)
        
        #print (tag)
        response = requests.get(self.homepage + tag)
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.findAll("div", {"class": "post-block post-block--image post-block--unread"}):
            tag_header = tag.find("a", {"class": "post-block__title__link"})
            tag_content = tag.find("div", {"class": "post-block__content"})
            
            article_title = tag_header.get_text().strip()
            article_href = tag_header["href"]
            self.article_content = tag_content.get_text().strip()
            self.article_titles.append(article_title)
            self.article_contents.append(self.article_content)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)

        return self.article_titles[random.randrange(length)], self.article_hrefs[random.randrange(length)]