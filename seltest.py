from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys




driver = webdriver.Firefox()

driver.get('http://www.google.com')
elem=driver.find_element_by_link_text('Gmail') # finds the Gmail text on the Google Home Web Page
elem.click()

elem=driver.find_element_by_xpath("/html/body/nav/div/a[2]") # Chooses the second option in te=ge html format , which is sign in
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

#lem = driver.find_element_by_link_text("More Options")
#elem = driver.find_element_by_css_selector("div.jO7h3c")
elem.click()
###create new login complete


elem.send_keys(Keys.RETURN)


