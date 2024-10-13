from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


# Iniciar el navegador
driver = webdriver.Chrome()

# Ir a la página web donde se realiza la descarga
driver.get('https://docs.google.com/spreadsheets/d/14lrWudL3gf6mXHeUJCgqRDUkhGrx2BAOfw1e4TxO-H8/edit?usp=sharing')
time.sleep(1)
driver.find_element(By.ID, "docs-file-menu").click()
time.sleep(5)
enlace_privacidad = driver.find_element(By.CSS_SELECTOR, 'div.apps-menuitem .goog-menuitem-label[aria-label="Descargar d"]')
action = ActionChains(driver)
action.move_to_element(enlace_privacidad).perform()
time.sleep(5)

# Cerrar el navegador
driver.quit()