# Searching cycles in Wikipedia

## Introduction

This project comes from a game I play with friends. Thus, in this project, I used the french version of Wikipedia. The rules are simple.
- you are given two wikipedia pages
- you start from the first page, and you want to navigate to the second page
- you are only allowed to navigate through Wikipedia by following the urls on the page

Finding an optimal solution to this problem would be easy using the objects of this problem. But the goal here was different. A clever technique in this game is
to always follow the first url of the page. Doing this, you are certain to land on the "philosophy" page (still in french). Once you reach this page, you begin your search.
The question is the following: do you always land on the philosphy page with this strategy?

## Structure of the code

The object Wiki uses BeautifulSoup and requests and allows you to load a wikipedia page and retrieve all urls. The goal here is to find the first one. Of course, there are a lot of urls on the page, and the filter that has been implemented to discared some of them may have some flaws. But overall, it works pretty well. This is how you can get a Wikipedia page and follow the first url :

```python
from wiki import Wiki
wiki = Wiki("/wiki/Python_(langage)") # Wiki.random() returns a random page, using the wikipedia url for a random page
page = wiki.get_page(0) #returns first url
next_wiki = Wiki(page.url)
```

Using this technique, you can follow the path of the first urls until a cycle appears:

```python
Wiki.random().find_root()
```
wich displays in the terminal:

```
Wiki ->     établissement public de coo...     ->/wiki/%C3%89tablissement_public_de_coop%C3%A9ration_intercommunale
Wiki ->               française                ->/wiki/France
Wiki ->                  État                  ->/wiki/%C3%89tat
Wiki ->              sociologique              ->/wiki/Sociologie
Wiki ->               discipline               ->/wiki/Discipline_scientifique
Wiki ->                science                 ->/wiki/Science
Wiki ->                 latin                  ->/wiki/Latin
Wiki ->            langue italique             ->/wiki/Langues_italiques
Wiki ->                famille                 ->/wiki/Famille_de_langues
Wiki ->                langues                 ->/wiki/Langue
Wiki ->                système                 ->/wiki/Syst%C3%A8me
Wiki ->                ensemble                ->/wiki/Ensemble
Wiki ->             mathématiques              ->/wiki/Math%C3%A9matiques
Wiki ->             connaissances              ->/wiki/Connaissance
Wiki ->                 notion                 ->/wiki/Notion
Wiki ->              connaissance              ->/wiki/Connaissance_(philosophie)
Wiki ->              philosophie               ->/wiki/Philosophie
ROOT FOUND
```

As we can see, the path reaches the page "philosophie"!

It is now time to explore Wikipedia, with a Union-Find data-structure with path compression in order to speed up the search. To each wikipedia page, we link the cycle it reaches.

```python
map = WikiMap() #union-find data-structure (it's a dictionnary {page:cycle})
for i in range(100):
  map.append(Wiki.random())

print(map)
print(repr(map)) #shows one link per cycle that was found!
```

This is what we get:

```
<Map : size=337> ->
https://fr.wikipedia.org/wiki/Philosophie
https://fr.wikipedia.org/wiki/1941_au_Maroc
https://fr.wikipedia.org/wiki/Tokyo
https://fr.wikipedia.org/wiki/Projet_(management)
https://fr.wikipedia.org/wiki/H%C3%A9breu
https://fr.wikipedia.org/wiki/Danois
https://fr.wikipedia.org/wiki/Pologne
https://fr.wikipedia.org/wiki/Arabe
```
