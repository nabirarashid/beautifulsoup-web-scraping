from bs4 import BeautifulSoup

# open the file in read mode
with open("index.html", "r") as f:
    # using the html parser
    doc = BeautifulSoup(f, "html.parser")

# print (doc.prettify())

# to access specific tags; only gives the first
tag = doc.title
tag.string = "this is the title!"

# to only access contents in the tag
# print (doc.string)

# to access all tags
tags = doc.find_all("p")[0]
print (tags.find_all("b"))

