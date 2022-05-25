import requests
import json

response = requests.get('https://randomuser.me/api')

consulta = json.loads(response.text)


def show():
    if  (consulta['results'][0]['gender']) == "male":
        nombre=(consulta['results'][0]['name']['first'])
        apellido=(consulta['results'][0]['name']['last'])
        user=(consulta['results'][0]['login']['username'])
        passw=(consulta['results'][0]['login']['password'])
        print("\n░░░░░░░░░░░░░░░░░░","\n ▓▓  Hombre  ▓▓","\n\nNombre:",nombre,"\nApellido:",apellido,"\nUsuario:",user,"\nContraseña:",passw,"\n░░░░░░░░░░░░░░░░░░")
    else:
        nombre=(consulta['results'][0]['name']['first'])
        apellido=(consulta['results'][0]['name']['last'])
        numero=(consulta['results'][0]['location']['street']['number'])
        nombreC=(consulta['results'][0]['location']['street']['name'])
        ciudad=(consulta['results'][0]['location']['city'])
    
        print("\n░░░░░░░░░░░░░░░░░░","\n ▓▓  Mujer  ▓▓","\n\nNombre:",nombre,"\nApellido:",apellido,"\nNombre calle:",nombreC,"\nNumero:",numero,"\nCiudad:",ciudad,"\n░░░░░░░░░░░░░░░░░░")

show()