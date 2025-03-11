from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-gv-n4060eagle-oc-8gd-nvidia-geforce-rtx-4060-8gb-gddr6/p/N82E16814932629?Item=N82E16814932629"

# we want to find the price of the GPU

# sending a request to the url; http get request

result = requests.get(url)

# only printing the result gives an object of type response
# print (result.text)

# using the html parser
doc = BeautifulSoup(result.text, "html.parser")

# finding the price using the $ symbol
# not using tags this time
prices = doc.find_all(string="$")

# using the parent of the symbol to get the price
parent = prices[0].parent
print (parent.text)