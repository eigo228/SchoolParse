import requests
from bs4 import BeautifulSoup as BS 
import fake_useragent
import datetime


def parse():
	rNow = datetime.datetime.now()
	den = rNow.strftime('%a')
	if den == 'Sat' or den == 'Sun':
		print('Its a weekend.')
		return
	session = requests.Session()

	auth = 'https://new-cabinet.elmektep.kg/'

	user = fake_useragent.UserAgent().random

	header = {
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	    'Content-Type': 'application/json;charset=utf-8',
	    'Argus-App-Type': 'cabinet',
	    'Origin': 'https://new-cabinet.elmektep.kg',
	    'Connection': 'keep-alive',
	    'Referer': 'https://new-cabinet.elmektep.kg/children/2020-11-11',
	    'Pragma': 'no-cache',
	    'Cache-Control': 'no-cache',
	}



	datas = '{"login":"+996755898801","password":"Ukt,fcz2004"}'

	temp = datetime.datetime.now()
	nowdate = temp.strftime('%Y-%m-%d')

	response = session.post('https://api.elmektep.kg/rest/auth', data=datas, headers=header).text
	souped = eval(response)
	token = souped['token']
	tokenok = {'Argus-Auth-Token': token}

	heads = {
	    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	    'Argus-App-Type': 'cabinet',
	    'Argus-Auth-Token': '6oP9iJlHxJ-CIKdEK7_T0g',
	    'Origin': 'https://new-cabinet.elmektep.kg',
	    'Connection': 'keep-alive',
	    'Referer': 'https://new-cabinet.elmektep.kg/children/{}'.format(nowdate),
	    'If-None-Match': '"d6edbbde1c57dd0f4fafa2aba19d61ad"',
	}

	responsible = requests.get('https://api.elmektep.kg/rest/account', headers=heads).text

	#information = 'https://new-cabinet.elmektep.kg/apps/356725/dnevnik/home/2020-11-11'
	#get_info = session.get(information, headers=heads, data=tokenok).text
	#html = BS(get_info,'html.parser')
	html = BS(responsible,'html.parser')

	headeros = { 
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0',
	    'Accept': 'application/json, text/plain, */*',
	    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
	    'Argus-App-Type': 'cabinet',
	    'Argus-Auth-Token': '6oP9iJlHxJ-CIKdEK7_T0g',
	    'Origin': 'https://new-cabinet.elmektep.kg',
	    'Connection': 'keep-alive',
	    'Referer': 'https://new-cabinet.elmektep.kg/apps/356725/dnevnik/home/{}'.format(nowdate),
	}

	params = (
	    ('date', str(nowdate)),
	    ('student_id', '356725'),
	)

	responsed = requests.get('https://api.elmektep.kg/rest/cabinet/dnevnik/week', headers=headeros, params=params).text

	finishedData = eval(responsed)

	idshik = finishedData['356725']
	date = idshik[str(nowdate)]
	number = []
	for lesson in date:
		discip = date[lesson]
		number.append(discip['discipline'])

	listLessons = []
	for i in date:
		listLessons.append(i)
	#print(listLessons)	
	with open('lessons.txt', 'w') as files:
		readen = 0
		for num in number:
			files.write(num + '\n')
			readen += 1
	print(idshik)
parse()




