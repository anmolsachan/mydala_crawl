from argparse import ArgumentParser
import requests
from bs4 import BeautifulSoup
import json

def parse_sitemap(url):
	resp = requests.get(url)
	if 200 != resp.status_code:
		return False
	soup = BeautifulSoup(resp.content)
	urls = soup.findAll('loc')
	if not urls:
		return False
	urls=[url.string for url in urls]
	urls.remove("http://www.mydala.com/sitemap-online-coupons.xml")
	urls.remove("http://www.mydala.com/sitemaps/all-merchant.xml")
	with open("sitemap_links","w") as sl:
		sl.write(json.dumps(urls))
	sl.close()
	print "done !!"
if __name__ == '__main__':
	maplink="http://www.mydala.com/sitemap.xml"
	parse_sitemap(maplink)