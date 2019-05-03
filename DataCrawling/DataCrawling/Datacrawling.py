from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
import requests  
from selenium.webdriver.common.by import By
import selenium as se
import sys 

def simple_get(url):
	"""
	Attempts to get the content at `url` by making an HTTP GET request.
	If the content-type of response is some kind of HTML/XML, return the
	text content, otherwise return None.
	"""
	try:
		with closing(get(url, stream=True)) as resp:
			if is_good_response(resp):
				return resp.content
			else:
				return None

	except RequestException as e:
		log_error('Error during requests to {0} : {1}'.format(url, str(e)))
		return None
		
def is_good_response(resp):
	""" 
    Returns True if the response seems to be HTML, False otherwise.
    """
	content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200 
			and content_type is not None 
			and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def learnpython():
	raw_html = simple_get('https://www.w3schools.com/python/python_getstarted.asp')
	soup  = BeautifulSoup(raw_html, 'html.parser') 
	flag = '0'
	result = []
	for a in soup.select('a'):
		if a.text == 'Python HOME':
			flag = '1'
		if flag == '1':
			result.append(a.text);
		if a.text == 'Python Try...Except':
			break
			
	print('Python Tag')
	for tag in result:
		print(tag)

def sel():
	#driver = webdriver.Chrome()
	driver = webdriver.PhantomJS()
	url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=zh-CN&text=aaaaaaa'
	driver.get(url)
	element = driver.find_element(By.XPATH,'//span[@class="tlid-translation translation"]')
	print (element.text) 

def sel2(str):
	options = se.webdriver.ChromeOptions()
	options.add_argument('headless') 
	driver = se.webdriver.Chrome(chrome_options=options)
	url = 'https://translate.google.com/#view=home&op=translate&sl=en&tl=zh-CN&text='+str
	print(url)
	driver.get(url)
	element = driver.find_element(By.XPATH,'//span[@class="tlid-translation translation"]') 
	element2 = driver.find_elements(By.XPATH,'//div[@class="tlid-transliteration-content transliteration-content full"]')
	print (element.text)  

def sel3():
	options = se.webdriver.ChromeOptions()
	options.add_argument('headless') 
	driver = se.webdriver.Chrome(chrome_options=options)
	url = 'https://github.com/YuanGao0702?tab=repositories'
	print(url)
	driver.get(url)
	elements = driver.find_elements(By.XPATH,'//a[@itemprop="name codeRepository"]') 
	print("total repositories: " + str(len(elements)))
	for e in elements:
		print (e.text) 

#sel2(sys.argv[1])
sel3()