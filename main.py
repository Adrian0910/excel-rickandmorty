import requests  # Importamos la librería requests
from openpyxl import Workbook

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....")
URL = 'https://rickandmortyapi.com/api/character'  # configuramos la url
# solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL)

#data = data.json()  # convertimos la respuesta en dict
dataConvert = data.json()  # convertimos la respuesta en dict

#print(data)
newData = dataConvert.get('results')

# =============================================================================
# creamos el objeto Workbook
wb = Workbook()

# ruta de nuestro archivo
filesheet = "./rickAndMorty.xlsx"

# seleccionaos el archivo
sheet = wb.active



# recorremos las columnas y escribimos los datos
for i in newData:
    sheet.append(
        (
            i.get('id'),
            i.get('name'),
            i.get('status')
        )
    )	

# guardamos los cambios
wb.save(filesheet)
