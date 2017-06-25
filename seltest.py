from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time



driver = webdriver.Firefox()

driver.get('http://www.google.com')
elem=driver.find_element_by_link_text('Gmail') # finds the Gmail text on the Google Home Web Page
elem.click()

elem=driver.find_element_by_xpath("/html/body/nav/div/a[2]") # Chooses the second option in the html format , which is sign in
elem.click()

######Create New Login #####
elem=driver.find_element_by_class_name('bdf4dc')
elem = driver.find_element_by_class_name('fImV7')
elem=driver.find_element_by_class_name('IMH1vc.lUHSR')
elem.click()
elem=driver.find_element_by_class_name('JPdR6b')
elem=driver.find_element_by_class_name('XvhY1d')
elem=driver.find_element_by_class_name('JAPqpe')
elem=driver.find_element_by_class_name('z80M1')

#elem = driver.find_element_by_link_text("More Options")
#elem = driver.find_element_by_css_selector("div.jO7h3c")

elem.click()
elem.send_keys(Keys.RETURN)
time.sleep(2)

# Seems to be a long cut

# elem=driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div')
# #elem=driver.find_element_by_class_name('signuponepage.main.content.clearfix')
# elem=driver.find_element_by_class_name('clearfix')

# elem=driver.find_element_by_class_name('sign-up')
# elem=driver.find_element_by_class_name('signup-box')
# elem=driver.find_element_by_class_name('form-element.multi-field.name')

# Long cut

nameFirst= driver.find_element_by_name("FirstName")

nameFirst.send_keys("J")
nameLast = driver.find_element_by_name("LastName")

nameLast.send_keys("342")

email= driver.find_element_by_name("GmailAddress")

email.send_keys("abc123selniumtest")

password=driver.find_element_by_name("Passwd")

password.send_keys("ABCDEFGH")


confirmPassword = driver.find_element_by_name("PasswdAgain")
confirmPassword.send_keys("ABCDEFGH")


#month of Birth
birthmonth = driver.find_element_by_class_name("goog-inline-block.goog-flat-menu-button.jfk-select")
birthmonth.send_keys("Feb")

#Date of Birth
dayofmonth= driver.find_element_by_id("BirthDay")
dayofmonth.send_keys("19")

#Birthyear
birthyear= driver.find_element_by_id("BirthYear")
birthyear.send_keys("1993")

#Gender
gender= driver.find_element_by_id(":d")
gender.click()
gender.send_keys("Male")
gender.send_keys(Keys.RETURN)

# Area code
mobile= driver.find_element_by_class_name("goog-inline-block.i18n-phone-select-country-dropdown")
mobile.click()
time.sleep(5)
mobile.send_keys("India")			# Yet to resolve the changes in the Country Code
mobile.send_keys(Keys.RETURN)



recovemail = driver.find_element_by_id("RecoveryEmailAddress")
recovemail.send_keys("amoljoshi1993@gmail.com")
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")
# firstname= soup.find_all('FirstName')

# elem.send_keys(i)
# elem.send_keys(Keys.RETURN)





#elem=driver.find_element_by_tag_name('FirstName')
# elem.click()
# elem.send_keys('A')
# ###create new login complete


# elem.send_keys(Keys.RETURN)


