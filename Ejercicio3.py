import requests
import json

#Cree la función"coment"que recibe como parámetro un número,y devuelve como diccionario el comentario que tenga como atributo"id"el número que se agregó como parámetro:

def comment(n):
    response= requests.get('https://jsonplaceholder.typicode.com/comments')
    consulta = json.loads(response.text)
    n=(input("ingrese el numero del comentario:"))
    diccionario = {"comentario" : consulta[int(n)]['body']}
    return diccionario

n=0
print(comment(n))