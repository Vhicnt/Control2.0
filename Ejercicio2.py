import requests
import json

#Cree la función"georeference"que,reciba como parámetro un número,yque devuelva un
#arreglo donde el primer elemento sea el nombre,el segundo elemento sea la latitudyel
#tercer elemento sea su longitud.


response = requests.get('https://jsonplaceholder.typicode.com/users')

consulta = json.loads(response.text)


def georeference(n):
    lista=[]
    print("ingrese num: ")
    n=(input())
    nombre=(consulta[int(n)]['name'])
    lat=(consulta[int(n)]['address']['geo']['lat'])
    lng=(consulta[int(n)]['address']['geo']['lng'])
    lista.append([nombre,lat,lng])
    print(lista)

n=0
georeference(n)