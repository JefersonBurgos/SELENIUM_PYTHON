# In this script im going to show a wikipedia finding from selenium
# first step: Import libraries
from selenium import webdriver
#the actual version include webdriver, then we dont have to install it
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#Inicialice to driver
driver = webdriver.Chrome()
#find the page and opend it
try:
		driver.get('https://www.wikipedia.org/')
		#click on the search field. looking for the path
		search_box = driver.find_element(By.ID, "searchInput")
		search_box.send_keys("Python (programming language)")
		search_box.send_keys(Keys.RETURN)  # Envía el formulario
		time.sleep(3)
		assert "Python (programming language)" in driver.title
		link = driver.find_element(By.LINK_TEXT, "Guido van Rossum")
		link.click()
		time.sleep(3)
		assert "Guido van Rossum" in driver.title
finally:
	driver.quit()