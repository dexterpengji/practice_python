# -- coding: utf-8 --
import urllib.request,os,re,codecs
from bs4 import BeautifulSoup

def read_txt(fileName):
	with open(fileName, 'r') as f:
		return f.read()

def write_txt(fileName,content):
	f = open(fileName, 'w')
	f.write(str(content))
	f.close()

def url_open(url,Referer):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
       'Referer': Referer}
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_chapters_index(textUrl):
	chapters_index = []
	soup = BeautifulSoup(textUrl, 'html.parser')
	layer1 = soup.find('select', class_='player-chapter' )
	layer2 = layer1.find_all('option',)
	for item in layer2:
		chapters_index.append(item.get_text()[2:])
	return chapters_index

def get_problems_index(textUrl):
	problems_index = []
	soup = BeautifulSoup(textUrl, 'html.parser')
	layer1 = soup.find('select', class_='player-problem' )
	layer2 = layer1.find_all('option',)
	for item in layer2:
		problems_index.append(item.get_text()[:])
	return problems_index

if __name__ == '__main__':
# prameters setting
	url = 'https://www.chegg.com/homework-help/Advanced-Engineering-Mathematics-2nd-edition-chapter-1.2-problem-solution-9780133214314'
	Referer = 'https://www.chegg.com'
	print('url='+url)
	print('Referer='+Referer)

# step1 - get the index of book
	# loading index file
	if os.path.exists('pageUrl.txt'):
		textUrl = read_txt('pageUrl.txt')
		print('Url file existed, loaded.')
	else:
		print('Url file does not exist, downloading...')
		write_txt('pageUrl.txt',url_open(url,Referer))
		textUrl = read_txt('pageUrl.txt')
		print('Loaded') ###

	# get the list of chapters
	chapters_index = get_chapters_index(textUrl);
	print(chapters_index)
	# get the list of problems
	problems_index = get_problems_index(textUrl);
	print(problems_index)

# step 2 - download problems

# step 3 - download solutions

# step 4 - write problems and solutions

# thanks
