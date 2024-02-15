# If we want to scrape a website, there are 2 ways to perform this:
#     1.  Use the API
#     2.  HTML Web Scraping using some tool like bs4

# STEP 0 => install  all the requirements:
    #   1.  pip install requests
    #   2.  pip install bs4
    #   3.  pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# STEP 1 => Get the HTML:
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# STEP 2 => Parse the HTML:
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# STEP 3 =>  HTML Tree Traversal:

# Commonly used types of objects:
#   1. Tag -             print(type(title))
#   2. NavigableString - print(type(title.string))
#   3. BeautifulSoup -   print(type(soup))
#   4. Comment -         print(type(soup.p.string))

# Get the title of the HTML page
title = soup.title
print(type(soup))  # it will print = <class 'bs4.BeautifulSoup'>
print(type(title))  # it will print = <class 'bs4.element.Tag'>
print(type(title.string)) # it will print = <class 'bs4.element.NavigableString'>

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p) # it will print =  <p><!-- this is a comment --></p>
print(soup2.p.string) # it will print =   this is a comment
print(type(soup2.p.string)) # it will print = <class 'bs4.element.Comment'>

# If we want to data of div, where we only have div id with us
navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
print(navbarSupportedContent.contents) # a tag's children are available as a list | all stored in memory | slow becaz takes memory
print(navbarSupportedContent.children) # a tag's children are available as a generator | not stored in the memory but can be accessed any time | fast
print(navbarSupportedContent.strings) # will give all the strings present in it | eg = login, signup ,videos.... | sb k bichme kai lines ka gap hoga
print(navbarSupportedContent.stripped_strings) # will  beautify it then will give | sbke bich m kuch gap nai hoga, but ek line m ek hi hoga
print(navbarSupportedContent.parent) # will provide us with all the parent of this id and all the  contents present inside those parents | as it is in the code

for item in navbarSupportedContent.parents:
    print(item) # it will provide only parent , not its content | eg = nav body html... (each in new line) 
print(navbarSupportedContent.next_sibling) # will give next content under the same parent | for imagining it search HTML document Tree
print(navbarSupportedContent.next_sibling.next_sibling) # next ka bhi next
print(navbarSupportedContent.previous_sibling.previous_sibling) # agr akela haito parent ka sibling dega but vo lene k lie so br likhn apadega becaz it treats new line and spaces also as siblings
print(navbarSupportedContent.previous_sibling) # current k phle wla return krdega

# How to get all the paragraphs from the page:
paras = soup.find_all('p')
print(paras)

# How to get all archor tags from the page:
anchors = soup.find_all('a')
print(anchors)

# --------------
# Get all links present in the html:   ********IMP
anchors = soup.find_all("a")
all_links = set()

for link in anchors:
    if (link!="#"):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)


# ------------------


print(soup.find('p')) # get first element
print(soup.find('p')['class']) # by adding class we can retrieve everything that class have.
 
# Finds all the elements with class name as lead:
print(soup.find_all("p",class_="lead"))

# Get the text from the tags/soup:
print(soup.find("p").get_text())
print(soup.get_text())   # will give all text present in the html

# CSS Selectors
elem = soup.select('#loginModel')
print(elem) # will print whole element whose CSS class name is loginModel

elem = soup.select('.loginModel')
print(elem) # will return a class whose class name is loginModel