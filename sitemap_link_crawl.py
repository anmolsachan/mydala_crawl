from json_reader import reader
import requests
from bs4 import BeautifulSoup
import json

links=[]

def read_file(filename):
	with open(filename,"r") as fil:
		content = fil.read().splitlines()
		for dat in content:
			try:
				dat=json.loads(dat)
				for link in dat:
					links.append(link)
			except Exception as e :
				print e
def parse_page(link):
	


if __name__ == '__main__':
	filename="all_sitemap_links"
	read_file(filename)
	print len(links)
	