import os.path
import datetime
import schedule
from selenium import webdriver
from webdrive import driver
import times #file times.py
import time
import parser #file parser.py 




rightNow = datetime.datetime.now()
print(rightNow)


day = (rightNow.strftime('%a'))
print(day)


def gotoMeet(links):
	print('Joining.')
	driver.get(links)
	time.sleep(1800) #30 min
	driver.quit()

def monday():
	parser.parse()
	schedule.every().monday.at(firstLesson).do(gotoMeet, times.getLess(1))
	schedule.every().monday.at(secondLesson).do(gotoMeet, times.getLess(2))
	schedule.every().monday.at(thirdLesson).do(gotoMeet, times.getLess(3))
	schedule.every().monday.at(fourthLesson).do(gotoMeet, times.getLess(4))
	schedule.every().monday.at(fifthLesson).do(gotoMeet, times.getLess(5))
	schedule.every().monday.at(sixthLesson).do(gotoMeet, times.getLess(6))
	schedule.every().monday.at(seventhLesson).do(gotoMeet, times.getLess(7))

def tuesday():
	parser.parse()
	schedule.every().tuesday.at(times.firstLesson).do(gotoMeet, times.getLess(1))
	schedule.every().tuesday.at(times.secondLesson).do(gotoMeet, times.getLess(2))
	schedule.every().tuesday.at(times.thirdLesson).do(gotoMeet, times.getLess(3))
	schedule.every().tuesday.at(times.fourthLesson).do(gotoMeet, times.getLess(4))
	schedule.every().tuesday.at(times.fifthLesson).do(gotoMeet, times.getLess(5))
	schedule.every().tuesday.at(times.sixthLesson).do(gotoMeet, times.getLess(6))
	schedule.every().tuesday.at(times.seventhLesson).do(gotoMeet, times.getLess(7))

def wednesday():
	parser.parse()
	schedule.every().wednesday.at(times.firstLesson).do(gotoMeet, times.getLess(1))
	schedule.every().wednesday.at(times.secondLesson).do(gotoMeet, times.getLess(2))
	schedule.every().wednesday.at(times.thirdLesson).do(gotoMeet, times.getLess(3))
	schedule.every().wednesday.at(times.fourthLesson).do(gotoMeet, times.getLess(4))
	schedule.every().wednesday.at(times.fifthLesson).do(gotoMeet, times.getLess(5))
	schedule.every().wednesday.at(times.sixthLesson).do(gotoMeet, times.dichn['math']['link'])
	schedule.every().wednesday.at(times.seventhLesson).do(gotoMeet, times.getLess(7))

def thursday():
	
	parser.parse()
	schedule.every().thursday.at(times.firstLesson).do(gotoMeet, times.getLess(1))
	schedule.every().thursday.at(times.secondLesson).do(gotoMeet, times.getLess(2))
	schedule.every().thursday.at(times.thirdLesson).do(gotoMeet, times.getLess(3))
	schedule.every().thursday.at(times.fourthLesson).do(gotoMeet, times.getLess(4))
	schedule.every().thursday.at(times.fifthLesson).do(gotoMeet, times.getLess(5))
	schedule.every().thursday.at(times.sixthLesson).do(gotoMeet, times.getLess(6))
	schedule.every().thursday.at(times.seventhLesson).do(gotoMeet, times.getLess(7))

def friday():
	
	parser.parse()
	schedule.every().friday.at('7:50').do(gotoMeet, times.dichn['russian']['link'])
	schedule.every().friday.at(secondLesson).do(gotoMeet, times.getLess(2))
	schedule.every().friday.at(thirdLesson).do(gotoMeet, times.getLess(3))
	schedule.every().friday.at(fourthLesson).do(gotoMeet, times.getLess(4))
	schedule.every().friday.at(fifthLesson).do(gotoMeet, times.getLess(5))
	schedule.every().friday.at(sixthLesson).do(gotoMeet, times.getLess(6))
	schedule.every().friday.at(seventhLesson).do(gotoMeet, times.getLess(7))

if day == 'Mon':
	monday()
elif day == "Tue":
	print('Calling tuesday.')
	tuesday()
elif day == "Wed":
	print('wednesday now.')
	wednesday()
elif day == 'Thu':
	thursday()
elif day == 'Fri':
	friday()
else:
	print('________')

while True:
	rightNow = datetime.datetime.now()
	day = (rightNow.strftime('%a'))
	schedule.run_pending()

	time.sleep(5)#sec