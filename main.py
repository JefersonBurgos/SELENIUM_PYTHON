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