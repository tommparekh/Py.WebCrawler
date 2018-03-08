#Create a web crawler

import requests
from bs4 import BeautifulSoup
import time

#Open an article

start_url = "https://en.wikipedia.org/wiki/The_Lumberjack_Song"
end_url = "https://en.wikipedia.org/wiki/Philosophy"


article_chain = []


#while title of page istn't 'Philosophy' and we have not discovered a cycle:
#	append page to article_chain
#	download the page content
#	find the first link in  the content
#	page = that link
#	pause for a second






def continue_crawl(search_history, target_url, max_step=25):
	#if the most recent article in the search_history is the target article the search should stop and the function should return False
	#If the list is more than 25 urls long, the function should return False
	#If the list has a cycle in it, the function should return False
	#otherwise the search should continue and the function should return True.

	if search_history[-1] == target_url:
		print("We've found the target article!")
		return False
	elif len(search_history) > max_step:
		print("The search has gone on suspiciously long, aborting search!")
		return False
	elif search_history[-1] in search_history[:-1]:
		print("We've arrived at an article we've already seen, aborting search!")
		return False
	else:
		return True


#Find the first link in the article
def find_first_link(url):
	# get the HTML from "url", use the requests library
	resonse = requests.get(url)
	html = response.text

    # feed the HTML into Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # find the first link in the article
    #soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a['href']

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
	
	for element in content_div.find_all("p", recursive=False):
    if element.a:
        first_relative_link = element.a.get('href')
        break

    first_link = "a url or None"

    # return the first link as a string, or return None if there is no link
    if first_link:
    	return first_link



while continue_crawl(article_chain, end_url):
	# download html of last article in article_chain
    # find the first link in that html

    first_link = find_first_link(article_chain[-1])

    # add the first link to article_chain
    article_chain.append(first_link)

    # delay for about two seconds
    time.sleep(2)



#Follow the link


#Record the link in the article_chain data structure.



#Repeat this process until we reach the Philosophy article, or get stuck in an article cycle.