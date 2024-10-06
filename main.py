from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
import time

def initialize_driver():
	driver = webdriver.Chrome()
	return driver

def main():
	driver = initialize_driver()
	driver.get("https://www.google.com/?hl=es")
	time.sleep(4)


if __name__ == '__main__':
	main()