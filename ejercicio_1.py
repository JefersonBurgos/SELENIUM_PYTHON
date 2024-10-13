from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def initialize_driver():
	driver = webdriver.Chrome()
	return driver

def login(driver):
	input_username=driver.find_element(By.ID, "user-name")
	#print(input_username)
	#/html/body/div[2]/div[2]/div/div[1]/text()[1]
	user_name_value = driver.find_element(By.XPATH,"//*[@id='login_credentials']")
	split_container_username = user_name_value.text.split("\n")
	user_name = split_container_username[1]
	#print(user_name)
	#By.XPATH,"//*[@id="login_credentials"]/text()[1]
	#/html//div[@id='login_credentials']
	input_username.send_keys(user_name)
	#time.sleep(1)
	input_password = driver.find_element(By.ID, "password")
	container_password = driver.find_element(By.CLASS_NAME, 'login_password')
	split_container_password = container_password.text.split("\n")
	password = split_container_password[1]
	input_password.send_keys(password)
	loggin_button = driver.find_element(By.ID, "login-button")
	loggin_button.click()
	time.sleep(2)
	return driver
	#/html/body/div[2]/div[2]/div/div[2]
	#/html/body/div[2]/div[2]/div/div[2]/text()

def main():
	driver = initialize_driver()
	driver.get("https://www.saucedemo.com/v1/")
	driver = login(driver)
	if driver.current_url == "https://www.saucedemo.com/v1/inventory.html":
		print("Login succesful")
	else:
		print("Login Failed")

if __name__ == '__main__':
	main()
	#http1s://www.saucedemo.com/v1/
	#https://www.youtube.com/watch?v=bMsQ0SfrM8U&ab_channel=CodexBothttps://www.youtube.com/watch?v=bMsQ0SfrM8U&ab_channel=CodexBot