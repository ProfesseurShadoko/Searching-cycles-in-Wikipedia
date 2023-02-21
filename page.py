

class Page:
    
    def __init__(self,titre:str,url:str):
        self.titre = titre
        self.url = url
    
    @property
    def name(self):
        titre = self.titre if len(self.titre)<=30 else (self.titre[:27]+"...")
        return f"{titre:^40}"
    
    def __str__(self)->str:
        titre = self.titre if len(self.titre)<=30 else (self.titre[:27]+"...")
        return f"Wiki ->{self.name}->{self.url}"
    
    def __repr__(self)->str:
        return f"https://fr.wikipedia.org{self.url}"
    
    def __eq__(self,__o:object)->bool:
        if type(__o) == type(self):
            return __o.url == self.url
        else:
            return False
    
    def __hash__(self) -> int:
        return hash(self.url)
    
   
            

class Book(dict):
    """Inherits from dictionnary. Implements the UnionFind datastructure
    """

    def add(self,key:Page,next:Page):
        if next in self.keys():
            self[key]=self.root(next)
        else:
            self[key]=next
    
    def root(self,page:Page)->Page:
        if not page in self.keys():
            return None
        
        if page==self[page]:
            return page #it loops here !
        
        self[page] = self.root(self[page]) #contraction de chemin
        return self[page]
    
    def __str__(self)->str:
        return "BOOK {\n" + "\n".join([
            f"\tBook -> {key.name} => {page.name}" for key,page in self.items()
        ]) + "\n}"
        
    
            
    
if __name__=="__main__":
    print(Page("Python","/wiki/python"))
    print(Page("Python (le langage de programmation, pas l'aniamal)","/wiki/python_prog"))
    print(Page("PythonPythonPythonPythonPython","/wiki/pythonpython"))
    print("\n\n")
    
    book = Book()
    
    philo = Page("p","p")
    maths = Page("m","m")
    info = Page("i","i")
    wiki = Page("w","w")
    web = Page("web","web")
    japan = Page("j","j")
    nippon = Page("n","n")
    
    pages = {
        philo:philo,
        info:maths,
        wiki:web,
        maths:philo,
        web:info,
        nippon:japan,
        japan:japan,
    }
    
    for page,next_page in pages.items():
        book.add(page,next_page)
    
    print(book)
        