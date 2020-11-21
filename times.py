

firstLesson = ('8:00')
secondLesson =	('8:40')
thirdLesson = ('9:20')
fourthLesson = ('10:00')
fifthLesson = ('10:40')
sixthLesson = ('11:20')
seventhLesson = ('12:00')



with open('lessons.txt', 'r') as filez:
	readen = filez.read().splitlines()


dichn = {
	"math": {'link': 'https://us04web.zoom.us/j/6584312438?pwd=Z2lKQ0s2VXFJVUh1aXhkK2lHM2NvQT09', 'naming': 'Математика'},
	"english": {'link': 'https://us04web.zoom.us/j/75349066373?pwd=c1ZST3QxdVlUMytGMm9FYjdVZzJDdz09', 'naming': 'Английский язык 1 группа' },
	'physics': {'link': 'https://us04web.zoom.us/j/3012455496?pwd=VTlRdWd6SzlWZVEwVi9tZjFSa3hGdz09', 'naming': 'Физика'},
	'klass': {'link':'https://us04web.zoom.us/j/3012455496?pwd=VTlRdWd6SzlWZVEwVi9tZjFSa3hGdz09', 'naming': 'Классный час'},
	'chemistry': {'link': 'https://us04web.zoom.us/j/9413247309?pwd=aFpoN2Z2ODBEclFuK243YnJ6NnVrdz09', 'naming': 'Химия'},
	'biolog': {'link': 'https://us04web.zoom.us/j/9413247309?pwd=aFpoN2Z2ODBEclFuK243YnJ6NnVrdz09', 'naming': 'Биология'},
	'economics': {'link': 'https://us04web.zoom.us/j/3210102043?pwd=TEZkSkJrMUsrMVBmU0FrcmZKNklqdz09', 'naming': 'Введение в экономику'},
	'epm': {'link': 'https://us04web.zoom.us/j/3210102043?pwd=TEZkSkJrMUsrMVBmU0FrcmZKNklqdz09', 'naming': 'Экономико-правовой-менеджмент'},
	'kyrgyz_til': {'link': 'https://us04web.zoom.us/j/7259398136?pwd=c2Q2Q3ZHTWpsRmhUeDdzcXg2VENYZz09', 'naming':'Кыргыз тили 1 группа'},
	'kyrgyz_ad': {'link': 'https://us04web.zoom.us/j/79312105403?pwd=NXJLYmFWcmJidUNSWWUxWUR0eWJHQT09', 'naming': 'Кыргыз адабият'},
	'russian': {'link': 'https://us04web.zoom.us/j/6241874180?pwd=Z25odjhrYzJhNEN3TlJTYWZ0Rnp6Zz09', 'naming': 'Русский язык'},
	'litra': {'link':'https://us04web.zoom.us/j/6241874180?pwd=Z25odjhrYzJhNEN3TlJTYWZ0Rnp6Zz09','naming':'Русская литература'},
	'dpm': {'link': 'https://us05web.zoom.us/j/86177695536?pwd=dUc1ejVQa2FzdVRSRCtoSC80TTh5dz09', 'naming':'ДПМ'},
	'phizra': {'link': 'https://us04web.zoom.us/j/4186169699?pwd=S2toY0xzckRTK3F1RFFXc1RzY3NBUT09','naming':'Физкультура'},
	'chio': {'link': 'https://us04web.zoom.us/j/6744019620?pwd=bXphbDNkSmdqOVRyT0pGTDZ0Rkovdz09','naming':'Человек и Общество'},
	'mip': {'link': 'https://us04web.zoom.us/j/9518472092?pwd=ZXlBTDA2NjhXRDh5RUNCZjZDQlViUT09','naming':'Мы и право'},
	'history': {'link':'https://us04web.zoom.us/j/8165509094?pwd=dWgvclF1Vjh2SVQxY0ZDaWhhd1Rodz09', 'naming': 'История'},
	'geograph': {'link': 'https://us04web.zoom.us/j/76838676878?pwd=SGh5UUhScEx2emN1cGRhNCtOb1VMQT09', 'naming': 'География'}
}

def keyz(dic, value):
	for k, v in dic.items():
		if v == value:
			return k

spis = []
for keyz in dichn:
	spis.append(keyz)

#for names in spis:
	#print(dichn[names]['naming'])




def getLess(numba):
	numba -= 1
	urr = readen[numba]
	for key, val in dichn.items():
		if val['naming'] == urr:
			print('Current lesson:',urr)
			return val['link']

