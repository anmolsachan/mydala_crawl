from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import json

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.think
online=db.online

def parse_sitemap(url):
	resp = requests.get(url)
	if 200 != resp.status_code:
		return False
	soup = BeautifulSoup(resp.content)
	urls = soup.findAll('loc')
	if not urls:
		return False
	urls=[url.string for url in urls]
	urls.remove("http://www.mydala.com/online-coupons/all")
	for link in urls:
		print link
		data={"link":link,"status":"incomlete"}
		online.insert(data)
if __name__ == '__main__':
	maplink="http://www.mydala.com/sitemap-online-coupons.xml"
	parse_sitemap(maplink)