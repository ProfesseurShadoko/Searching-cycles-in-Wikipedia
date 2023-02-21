from bs4 import BeautifulSoup as Soup
import requests
from page import Page, Book

class EmptySearch(Exception):
    def __init__(self):
        super().__init__("Scrapping has returned an empty page!")

class Wiki(Soup):
    
    root="https://fr.wikipedia.org/"
    show=True
    random_url="/wiki/Sp%C3%A9cial:Page_au_hasard"
    
    def __init__(self,url:str):
        
        if not Wiki.root in url:
            url = Wiki.root+url
        
        wiki = requests.get(url)
        super().__init__(wiki.text,"html.parser")
        self._url = url
        self._pages=None
        
    def get_url(self)->str:
        return self._url
    
    def get_pages(self)->list:
        if self._pages!=None:
            return self._pages
        body = self.find("main").find(id="mw-content-text")
        links = body.find_all('a')
        a:Soup
        self._pages = [Page(a.text,a['href']) for a in links if Wiki.is_valid_a(a)]
        return self._pages
        
    def get_page(self,index)->Page:
        if self._pages != None:
            if index>=len(self._pages):
                raise EmptySearch()
            return self._pages[index]
        else:
            body = self.find("main").find(id="mw-content-text")
            links = body.find_all('a')
            for a in links:
                if Wiki.is_valid_a(a):
                    if index==0:
                        return Page(a.text,a['href'])
                    index-=1  
            raise(EmptySearch())                 
        
    def next(self):
        page = self.get_page(0)
        if self.show:
            print(page)
        return Wiki(page.url)
        
    def find_root(self):
        links = set()
        page=self
        while page.get_url() not in links:
            links.add(page.get_url())
            page = page.next()
        print("ROOT FOUND")
    
    @staticmethod
    def is_valid_a(a:Soup)->bool:
        if not a.parent.name=="p":
            return False
        if a.parent.has_attr("class"):
            return False
        
        if a.parent.parent.name=="center":
            return False
        
        if a.parent.parent.has_attr("class") and a.parent.parent['class'][0]=="bandeau-cell":
            return False
        
        if a.has_attr("class") and a['class'][0] != 'mw-redirect':
            return False
        return True
    
    @staticmethod
    def random():
        return Wiki(Wiki.random_page().url) #random page has a wrong 'url' because random_url isn't it's real url !
    
    @staticmethod
    def random_page()->Page:
        return Wiki(Wiki.random_url).get_page(0)
    
if __name__=="__main__":
    
    wiki = Wiki.random()
    wiki.find_root()


                    
        