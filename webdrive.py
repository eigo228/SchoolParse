from selenium import webdriver
import os.path
fp = webdriver.FirefoxProfile('/home/gleb/.mozilla/firefox/vpx9y2nj.default-release')
driver = webdriver.Firefox(executable_path='/home/gleb/Documents/pyscripts/learninPython/geckodriver', firefox_profile=fp)