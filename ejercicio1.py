from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import xlwings as xw
import os
import glob
import time

# Iniciar el navegador
driver = webdriver.Chrome()

# Ir a la página web
driver.get('https://docs.google.com/spreadsheets/d/14lrWudL3gf6mXHeUJCgqRDUkhGrx2BAOfw1e4TxO-H8/edit?usp=sharing')
time.sleep(1)
driver.find_element(By.ID, "docs-file-menu").click()
time.sleep(5)
enlace_privacidad = driver.find_element(By.CSS_SELECTOR, 'div.apps-menuitem .goog-menuitem-label[aria-label="Descargar d"]')
action = ActionChains(driver)
action.move_to_element(enlace_privacidad).perform()
time.sleep(5)
elemento_excel = driver.find_element(By.CSS_SELECTOR, 'div.apps-menuitem span[aria-label="Microsoft Excel (.xlsx) x"]')
elemento_excel.click()
time.sleep(7)
# Cerrar el navegador
driver.quit()
#ruta_archivo = 'C:\\Users\\USER\\Desktop\\archivo1.xlsx'
# Ruta de la carpeta de descargas (ajústala según tu sistema)
carpeta_descargas = 'C:\\Users\\USER\\Downloads'

# Buscar el archivo Excel más reciente en la carpeta de descargas
lista_archivos = glob.glob(os.path.join(carpeta_descargas, '*.xlsx'))
archivo_reciente = max(lista_archivos, key=os.path.getctime)

print(f"El archivo más reciente es: {archivo_reciente}")

wb = xw.Book(archivo_reciente)
hoja = wb.sheets['Hoja 1']

hoja['B1'].value = 1
hoja['B2'].value = 1
hoja['B3'].value = 1

valor_b3 = hoja['B4'].value

print(f"La suma es: {valor_b3}")

wb.save(archivo_reciente)
wb.close()