from openpyxl import Workbook

# creamos el objeto Workbook
wb = Workbook()

# ruta de nuestro archivo
filesheet = "./rickAndMorty.xlsx"

# seleccionaos el archivo
sheet = wb.active

# escribirmos los datos con sus respectivas filas y columnas
datos = [('id', 'nombre', 'edad'),
   (0, "Rick", 70),
   (1, "Morty", 14),
   (2, "Summer", 24)]

# recorremos las columnas y escribimos los datos
for row in datos:
 sheet.append(row)

# guardamos los cambios
wb.save(filesheet)