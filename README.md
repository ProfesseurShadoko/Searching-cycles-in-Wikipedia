# Searching cycles in Wikipedia

## Introduction

This project comes from a game I play with friends. Thus, in this project, I used the french version of Wikipedia. The rules are simple.
- you are given two wikipedia pages
- you start from the first page, and you want to navigate to the second page
- you are only allowed to navigate through Wikipedia by following the urls on the page

Finding an optimal solution to this problem would be easy using the objects of this problem. But the goal here was different. A clever technique in this game is
to always follow the first link of the page. Doing this, you are certain to land on the "philosophy" page (still in french). Once you reach this page, you begin your search.
The question is the following: do you always land on the philosphy page with this strategy?

## Structure of the code

You can read wikipedia pages using BeautifulSoup and Requests. 
...
