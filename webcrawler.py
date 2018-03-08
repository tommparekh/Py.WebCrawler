#Create a web crawler example from Udacity course.

import requests
from bs4 import BeautifulSoup
import time
import urllib

#Open an article

start_url = "https://en.wikipedia.org/wiki/Special:Random"
end_url = "https://en.wikipedia.org/wiki/Philosophy"

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
	response = requests.get(url)
	html = response.text

    # feed the HTML into Beautiful Soup
	soup = BeautifulSoup(html, 'html.parser')

    # find the first link in the article
    #soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a['href']
	
	first_link = None
	content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
	
	# Find the first anchor tag that's a direct child of a paragraph.
    # It's important to only look at direct children, because other types
    # of link, e.g. footnotes and pronunciation, could come before the
    # first link to an article. Those other link types aren't direct
    # children though, they're in divs of various classes.

	for element in content_div.find_all("p", recursive=False):
		if element.find("a", recursive=False):
			first_link = element.find("a", recursive=False).get('href')
			break
   
    # return the first link as a string, or return None if there is no link
	if not first_link:
		return
	
	first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)
	return first_link

article_chain = [start_url]

while continue_crawl(article_chain, end_url):
	# download html of last article in article_chain
    # find the first link in that html

	first_link = find_first_link(article_chain[-1])
	print(first_link)
	if not first_link:
		# add the first link to article_chain
		print("We've arrived at an article with no links, aborting search!")
		break

	article_chain.append(first_link)

    # delay for about two seconds
	#btime.sleep(2)


