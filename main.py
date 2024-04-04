import requests
from constants import *


#TODO: USANDO LA DOCUMENTACION DE LA API PARA ACCEDER A LAS ESTADISTICAS DEL EJERCICIO COMO CALORIAS QUEMADAS


# https://trackapi.nutritionix.com 
api_endpoint="https://trackapi.nutritionix.com/v2/natural/exercise"


#informacion sacada de la documentacion de la api https://trackapi.nutritionix.com 
nutritionix_headers={
    'Content-Type': 'application/json',
    "x-app-id":APPLICATION_ID,
    "x-app-key":API_KEY,
}


#parametros que recibe nuestro post
nutritionix_parameters={
    'query':input('Introduce the exercise you did today and how long you did it: '),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


# Making a POST request
response = requests.post(api_endpoint, headers=nutritionix_headers, json=nutritionix_parameters)
 
 
# check status code for response received
# success code - 200
print(response)
 
 
# print content of request
print(response.json())