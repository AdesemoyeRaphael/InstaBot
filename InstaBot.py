#This code will scrape a given instagram username followers and stores it in an csv file

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

#Before we continue make sure you have GoogleChrome install on your PC and also to it GoogleChrome dirve for the version of your Chrome

#First we create a class. Since we can't access most of instagrame data without logging we have to create a class that will request our instagram username and password so it can login into our acctount so it can have access to the instagrame datas. And also a function that will takes in the arguement of the username of the person we want to scrape his username

class InstagramBot():
	def __init__(self,email,password):
		self.browserProfile = webdriver.ChromeOptions()
		self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
		self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
		self.email = email
		self.password = password

	def signIn(self,username):
		self.browser.get('https://www.instagram.com/accounts/login/')
		time.sleep(5)
		emailInput = self.browser.find_elements_by_css_selector('form input')[0]
		passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

		emailInput.send_keys(self.email)
		passwordInput.send_keys(self.password)
		passwordInput.send_keys(Keys.ENTER)
		time.sleep(6)
		self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(4)
		self.browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

		self.browser.get('https://www.instagram.com/' + username)
		time.sleep(5)
		followersLink = self.browser.find_element_by_css_selector('ul li a')
		followersLink.click()
		time.sleep(4)
		followersList = self.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
		followersList.click()
		time.sleep(5)
		actionChain = webdriver.ActionChains(self.browser)
		numberOfFollowersInList = 0

		
		time.sleep(2)
		scroll_box = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
		last_ht, ht = 0, 1
		while last_ht != ht:
			last_ht = ht
			time.sleep(3)
			ht = self.browser.execute_script("""
				arguments[0].scrollTo(0, arguments[0].scrollHeight);
				return arguments[0].scrollHeight;
				""", scroll_box)
		links = scroll_box.find_elements_by_tag_name('a')
		names = [name.text for name in links if name.text != '']

		self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

		print(names)
		return names
		time.sleep(10)

		def closeBrowser(self):
			self.browser.close()

		def __exit__(self,exc_type,exc_value,traceback):
			self.closeBrowser()



user = InstagramBot('input your user name','input your password')

f=user.signIn('the username of person you want to scrape his followers')

df = pd.DataFrame(f,columns = ['User name'])
print(df)
df.to_csv('instaUsernames.csv',index=False)
