import requests

# URL de la API a la que deseas hacer la solicitud GET
# url = 'http://localhost:4000/get-user/alejo'
# url = 'http://localhost:4000/create-user'
# url = 'http://localhost:4000/update-user'
url = 'http://localhost:4000/delete-user'

# Realizar la solicitud GET
# `response` is storing the response object returned by the `requests.get()` function. This object
# contains information about the HTTP response, such as the status code, headers, and the response
# content.

# response = requests.get(url)
# response = requests.post(url, json={"username": "alejo"})
# response = requests.put(url, json={"username": "alejo"})
response = requests.delete(url, json={"username": "alejo"})


# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Acceder a los datos de la respuesta en formato JSON (si la respuesta es JSON)
    data = response.json()
    print(data)
else:
    # Si la solicitud no fue exitosa, mostrar el código de estado
    print(f"La solicitud falló con el código de estado {response.status_code}")