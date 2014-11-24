from bs4 import BeautifulSoup as bsoup
import requests as rq
import csv

url = "http://espn.go.com/mens-college-basketball/standings"
r = rq.get(url)
soup = bsoup(r.content)

trs = soup.find_all("table", class_=True)

with open("records.csv", "wb") as ofile:
	f = csv.writer(ofile)
	
	f.writerow(["Team","Record"])
	
	for tr in trs:
		tds = tr.find_all("td")[3:]
		i = 0
		check = "0-"
		while (i < len(tds)-2):
			record = tds[i+2].get_text().encode("utf-8")
			if record.find("0-") == -1:
				i = i + 3
			else:
				team = tds[i].get_text().encode("utf-8")
				f.writerow([team, record])
				i = i + 3