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

#Finds SIGN IN
elem=driver.find_element_by_xpath("/html/body/nav/div/a[2]") # Chooses the second option in the html format , which is sign in
elem.click()



# Do you have a gmail account??
ques= (raw_input('1-yes , 2- No \n'))
if ques =='1':
	#put in email address
	signIn=driver.find_element_by_id("identifierId")
	signIn.send_keys(raw_input("Enter your gmail address - "))

	#Click next button
	nextBSignIn= driver.find_element_by_class_name("ZFr60d.CeoRYc")
	nextBSignIn.click()
	#nextBSignIn.send_keys(Keys.RETURN)

	#print 'hi'
	#ENter password
	passwdLogin=driver.find_element_by_class_name("aXBtI")
	passwdLogin.click()
	passwdLogin= driver.find_element_by_class_name("whsOnd.zHQkBf")
	
	passwdLogin.send_keys(raw_input("Enter your password- "))
	#passwdLogin.send_keys(Keys.RETURN)
	#print 'hi'

	#click next after entering password
	nextFinal= driver.find_element_by_class_name("RveJvd.snByac")
	nextFinal.click()

	#Gmail Logged In 


else:

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

	nameFirst.send_keys(raw_input("Enter your first name( 3 charachters atleast) - "))
	nameLast = driver.find_element_by_name("LastName")

	nameLast.send_keys(raw_input("Enter your last Name (3 characters atleast) - "))

	email= driver.find_element_by_name("GmailAddress")

	email.send_keys(raw_input("Enter your desired email-address - "))

	password=driver.find_element_by_name("Passwd")

	password.send_keys(raw_input("Enter your password - "))


	confirmPassword = driver.find_element_by_name("PasswdAgain")
	confirmPassword.send_keys(raw_input("confirm your password - "))


	#month of Birth
	birthmonth = driver.find_element_by_class_name("goog-inline-block.goog-flat-menu-button.jfk-select")
	birthmonth.send_keys(raw_input("Enter your first first Three letters of Birth month - "))

	#Date of Birth
	dayofmonth= driver.find_element_by_id("BirthDay")
	dayofmonth.send_keys(raw_input("Enter your date of birth - "))

	#Birthyear
	birthyear= driver.find_element_by_id("BirthYear")
	birthyear.send_keys(raw_input("Enter your Year of Birth - "))

	#Gender
	gender= driver.find_element_by_id(":d")
	gender.click()
	gender.send_keys(raw_input("Enter your gender - "))
	gender.send_keys(Keys.RETURN)

	# Area code (BUG 1)
	mobile= driver.find_element_by_class_name("goog-inline-block.i18n-phone-select-country")
	mobile=driver.find_element_by_class_name("goog-inline-block.i18n-phone-select-country-caption")
	mobile.click()
	#time.sleep(7)
	#mobile=driver.find_element_by_id("ae")

	#mobile.send_keys("India")			# Yet to resolve the changes in the Country Code # BUG 1
	mobile.send_keys(Keys.RETURN)
	#######

	#Input mobile number
	mobilenumberinput= driver.find_element_by_class_name("i18n_phone_number_input-inner_input")
	mobilenumberinput.send_keys(raw_input("Enter your Phone number - "))

	#REcovery mail
	recovemail = driver.find_element_by_id("RecoveryEmailAddress")
	recovemail.send_keys(raw_input("Enter your recvery email address if any - "))


	#Location (BUG 2 ) - Sometimes selects the country you want, sometimes it does not.
	loc=driver.find_element_by_id(":i")
	loc.click()
	time.sleep(5)
	#loc.send_keys("India")
	loc.send_keys(Keys.RETURN)

	#Next Button

	nextB=driver.find_element_by_id("submitbutton")
	nextB.click()
	nextB.send_keys(Keys.RETURN)


	#privacy terms
	prvt= driver.find_element_by_class_name("tos-scroll-button-content")
	prvt.click()

	#Agree terms and conditions
	time.sleep(1)
	agre=driver.find_element_by_id("iagreebutton")
	agre.click()

	time.sleep(1)
	#continue to gmail - after creating a new gmail account
	contgm= driver.find_element_by_class_name("g-button.g-button-submit")
	contgm.click()

###
time.sleep(5)


# Now logging out of Gmail
logout=driver.find_element_by_class_name("gb_8a.gbii")
logout.click()
logout=driver.find_element_by_class_name("gb_Fa.gb_tf.gb_Af.gb_je.gb_xb")
logout.click()

#Logout successfull

#Now removing the email address, so that the device does not remember the login Id. ( Bug 3)
time.sleep(2)
forgetEmail= driver.find_element_by_class_name("hMxfuf")
#forgetEmail= driver.find_element_by_class_name("mUbCce.fKz7Od.YYBxpf.KEavsb.M9Bg4d")
forgetEmail.click()


#forgetEmail.send_keys(Keys.RETURN)
# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")
# firstname= soup.find_all('FirstName')

# elem.send_keys(i)
# elem.send_keys(Keys.RETURN)





