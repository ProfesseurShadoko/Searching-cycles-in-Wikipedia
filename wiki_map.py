
from page import Page,Book
from wiki import Wiki,EmptySearch

class WikiMap(Book):
    
    show=True
    
    def __init__(self):
        self.promised = set()
        super().__init__()
        
    
    def append(self,page:Page): 
        try:
            self.promised=set()
            self.append_rec(page)
        except EmptySearch as e:
            print(e)
        
    def append_rec(self,page:Page)->Page: #returns root
        if WikiMap.show:
            print(page)
        if page in self.keys():
            return self[page]
        else:
            if page in self.promised:
                self.add(page,page)
                return page
            self.promised.add(page)
            next_page = Wiki(page.url).get_page(0)
            root = self.append_rec(next_page)
            self.add(page,root)
            return root
    
    def append_rd(self):
        print("\nWiki -> RANDOM")
        try:
            self.append(Wiki.random_page())
        except EmptySearch as e:
            print("During the search of a random page, the following error has occured:")
            print(e)
    
    def add_philo(self):
        page = Page("philosophie","/wiki/Philosophie")
        self.append(page)
    
    def roots(self)->list:
        out=set()
        for root in self.values():
            out.add(root)
        return list(out)
    
    def __repr__(self)->str:
        return f"<Map : size={len(self)}> -> \n"+"\n".join(page.__repr__() for page in self.roots())
        
    

if __name__=="__main__":
    map = WikiMap()
    map.add_philo()
    
    for i in range(100):
        map.append_rd()
        if i%10==0:
            print(map)
            print(map.__repr__())
    
    print("\nFINAL RESULTS :")
    print(map)
    
    print()
    
    print(repr(map))
    
    
    