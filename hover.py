from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('https://www.google.com')

time.sleep(2)

enlace_privacidad = driver.find_element(By.XPATH, '//a[@href="https://policies.google.com/privacy?hl=es-419&fg=1"]')

action = ActionChains(driver)

action.move_to_element(enlace_privacidad).perform()

time.sleep(5)

driver.quit()