#import openpyxl

## Cargar el archivo Excel (asegúrate de colocar la ruta correcta si está en tu escritorio)
#ruta_archivo = 'C:\\Users\\USER\\Desktop\\archivo1.xlsx'  # Reemplaza 'TuUsuario' por tu nombre de usuario
#wb = openpyxl.load_workbook(ruta_archivo)

## Seleccionar la hoja activa (si hay más de una hoja, podrías especificar el nombre)
#hoja = wb['Hoja2']

## Escribir "PRACTICA" en la celda A1
#hoja['B1'] = 1
#hoja['B2'] = 3

#wb.save(ruta_archivo)
#wb = openpyxl.load_workbook(ruta_archivo, data_only=True)
#hoja = wb['Hoja2']
### Leer el valor de la celda A2
#valor_a2 = hoja['B3'].value

### Imprimir el valor de A2 en pantalla
#print(f"La suma es: {valor_a2}")
import xlwings as xw

# Cargar el archivo Excel
ruta_archivo = 'C:\\Users\\USER\\Desktop\\archivo1.xlsx'

# Abrir el archivo Excel con xlwings
wb = xw.Book(ruta_archivo)

# Seleccionar la hoja específica (por nombre)
hoja = wb.sheets['Hoja2']

# Escribir valores en las celdas B1 y B2
hoja['B1'].value = 1
hoja['B2'].value = 3

# Excel recalculará automáticamente la fórmula en B3
# Leer el valor calculado en B3 (suponiendo que ya tiene la fórmula B1 + B2)
valor_b3 = hoja['B3'].value

# Imprimir el valor calculado en B3
print(f"La suma es: {valor_b3}")

# Guardar y cerrar el archivo
wb.save(ruta_archivo)
wb.close()