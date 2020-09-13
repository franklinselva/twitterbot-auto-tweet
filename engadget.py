from bs4 import BeautifulSoup
import requests
import random

class engadget:
    def __init__(self, topics):
        self.topics = topics
        self.homepage = 'http://www.engadget.com'
        self.article_titles = []
        self.article_contents = []
        self.article_hrefs = []

    def parse(self):
        tag = random.choice(self.topics)
        
        print (tag)
        response = requests.get('https://search.engadget.com/search;_ylc=X3IDMgRncHJpZANCRjhPTUp5WlRpdVQ1dkoyWHlfRXFBBG5fc3VnZwM4BHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMyBHF1ZXJ5A2FpBHRfc3RtcAMxNTc3MzEwOTI5?p=' + tag + '&fr=engadget')
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.findAll("li", {"class": "ov-a  mt-0 pt-26 pb-26 bt-dbdbdb"}):
            tag = tag.find("div", {"class": "d-tc"})
            print (tag)
            tag_header = tag.find("h4", {"class": "pb-10"})
            tag_header = tag_header.find("a", {"class": "fz-20 lh-22 fw-b"})
            tag_content = tag.find("p", {"class": "fz-14 lh-17"})
            print (tag_header)
            print (tag_content)
            #return None, None
            
        '''
            article_title = tag_header.get_text().strip()
            article_href = tag_header["href"]
            self.article_content = tag_content.get_text().strip()
            self.article_titles.append(article_title)
            self.article_contents.append(self.article_content)
            self.article_hrefs.append(article_href)

        length = len(self.article_titles)

        return self.article_titles[random.randrange(length)], self.article_hrefs[random.randrange(length)]'''