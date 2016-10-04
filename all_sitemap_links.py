from json_reader import reader
import requests
from bs4 import BeautifulSoup
import json

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.think
sitemap=db.sitemap


def parse_xml_link(url):
	resp = requests.get(url)
	if 200 != resp.status_code:
		return False
	soup = BeautifulSoup(resp.content)
	urls = soup.findAll('loc')
	if not urls:
		return False
	urls=[url.string for url in urls]
	return urls

def site_crawl(data):
	for xml_link in data:
		links=parse_xml_link(xml_link)
		try:
			for link in links:
				data={"link":link,"status":"incomlete"}
				sitemap.insert(data)
		except Exception as e:
			pass

if __name__ == '__main__':
	filename="sitemap_links"
	data=reader(filename)
	site_crawl(data)