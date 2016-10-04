from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import json

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.think
merchant=db.merchant

def parse_sitemap(url):
	resp = requests.get(url)
	if 200 != resp.status_code:
		return False
	soup = BeautifulSoup(resp.content)
	urls = soup.findAll('loc')
	if not urls:
		return False
	urls=[url.string for url in urls]
	for link in urls:
		print link
		data={"link":link,"status":"incomlete"}
		merchant.insert(data)
	print "done !!"
if __name__ == '__main__':
	maplink="http://www.mydala.com/sitemaps/all-merchant.xml"
	parse_sitemap(maplink)