from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd




class InstagramBot():
	def __init__(self,email,password):
		self.browserProfile = webdriver.ChromeOptions()
		self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
		self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
		self.email = email
		self.password = password

	def signIn(self,username,max):
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


	# def getUserFollowers(self,username,max):
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



user = InstagramBot('akinfoyekup@gmail.com','tuesday..')
f=user.signIn('elmagnificooriginality',30)

df = pd.DataFrame(f,columns = ['User name'])
print(df)
