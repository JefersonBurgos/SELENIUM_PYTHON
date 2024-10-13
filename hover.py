from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicializar el navegador (Chrome)
driver = webdriver.Chrome()

# Navegar a la página donde está el enlace
driver.get('https://www.google.com')  # Reemplaza con la URL correcta de tu caso

# Esperar a que cargue la página
time.sleep(2)

# Localizar el elemento "Privacidad" usando su texto o cualquier otro atributo relevante
enlace_privacidad = driver.find_element(By.XPATH, '//a[@href="https://policies.google.com/privacy?hl=es-419&fg=1"]')

# Crear una instancia de ActionChains para simular la acción de pasar el mouse sobre el enlace
action = ActionChains(driver)

# Realizar la acción hover sobre el elemento
action.move_to_element(enlace_privacidad).perform()

# Esperar un momento para que puedas visualizar la acción
time.sleep(5)

# Cerrar el navegador
driver.quit()