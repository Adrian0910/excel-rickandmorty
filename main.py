import requests  #Importamos la librería requests



print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
URL = 'https://rickandmortyapi.com/api/character/1,2,3' #configuramos la url
#solicitamos la información y guardamos la respuesta en data.
data = requests.get(URL) 

data = data.json() #convertimos la respuesta en dict

print(data)




