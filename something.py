import requests as rq
from bs4 import BeautifulSoup as bs
import time
url = "https://apod.nasa.gov/apod/astropix.html"
page = rq.get(url).content
soup = bs(page, 'html.parser')
response = soup.find('img')
if response == None:
	imglink = soup.find('iframe')['src']
else:
	imglink = 'https://apod.nasa.gov/apod/' + response['src']
def work():
	sess = rq.Session()
	cid='@testchaneling'
	turl = 'https://api.telegram.org/bot1157710197:AAGzLcuOqieGigo_Bo3UafXL3LKjLsrfL5Q/'
	if response == None:
		imglink = soup.find('iframe')['src']
		params = {'chat_id':cid,'text':imglink}
		sess.post(turl + 'sendMessage', data=params)
	else:
		imglink = 'https://apod.nasa.gov/apod/' + response['src']
		title = soup.find('b').get_text()
		params = {'chat_id':cid,'photo':imglink,'caption':title}
		sess.post(turl + 'sendPhoto', data=params)
	time.sleep(30)
while True :
	work()
