import requests
from bs4 import BeautifulSoup
import xlsxwriter
url = "http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&sortid=164&searchoption[3004][value]=6&searchoption[3004][type]=radio&searchoption[3005][value]=1&searchoption[3005][type]=radio&searchoption[3001][value]=25&searchoption[3001][type]=radio&filter=sortid&sortid=164&page=2"
r = requests.get(url)
#r.content #resulting in large amount of html, can't read.


soup = BeautifulSoup(r.content)
#print(soup.prettify()) #showed pretty clean html
'''links = soup.find_all("a") #find tags with "a"
for link in links:
	if "http" in link.get("href"):
		print("<a href='%s'>%s</a>" %(link.get("href"), link.text)
'''
tag = ['EnrollTime', 'OfferType', 'ProgramName', 'University', 'ReportTime', 'TofelScore', 'GreScore',
    'FormerUniversity'] 

g_data = soup.find_all("th",{"class":"new"})

'''for item in g_data:
	print(item)

for item in g_data:
	print(item.text)'''

info_list = []
for item in g_data:
	Title = item.contents[4].text
	for time in item.find_all('font',{"color":"#666"}):
		ET = time.text[1:]
	EnrollTime = ET
	for offer in item.find_all('font',{"color":"black"}):
		OT = offer.text[:-1]
	OfferType = OT
	for subject in item.find_all('font',{"color":"#F60"}):
		PN = subject.text
	ProgramName = PN
	for university in item.find_all('font',{"color":"#00B2E8"}):
		UN = university.text
	University = UN
	for rep_time in item.find_all('font',{"color":"brown"}):
		RT = rep_time.text
		GS = rep_time.text
	ReportTime = RT
	GreScore = GS
	for tofel in item.find_all('font',{"color":"cornflowerblue"}):
		TS = tofel.text
	TofelScore  = TS
	for b_uni in item.find_all('font',{"color":"purple"}):
		FU = b_uni.text
	FormerUniversity = FU
	info = [Title,EnrollTime, OfferType, ProgramName, University, ReportTime, TofelScore, GreScore,
    	FormerUniversity] 
	info_list.append(info)

with open('info.csv', 'w') as csvfile:
    w = csv.writer(csvfile)
    for row in info_list:
        w.writerow(row)

        
for item in g_data:
    for rep_time in item.find_all('font',{"color":"brown"}):
    	try:
    		print(rep_time.contents[3].text)
    	except:
    		pass