import requests  # Importamos la librería requests
import json

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....")
print('===================================')
URL = 'https://rickandmortyapi.com/api/character'  
data = requests.get(URL)

dataConvert = data.json()  # convertimos la respuesta en dict

newData = dataConvert.get('results')


for i in newData:
    print(i.get('id'))
    print(i.get('name'))
    print(i.get('status'))
    print('===================================')

    