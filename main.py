import requests
from constants import *
from datetime import datetime


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
json_response=response.json()
print(json_response)
print()


#en nuestro data json response, guardamos los datos almacenados en una lista que corresponsen a la clave 'exercises'
exercises_list=json_response['exercises']


#TODO:USANDO LA DOCUMENTACION DE LA API, GENERAREMOS UNA NUEVA LINEA DE INFORMACION EN EL GOOGLE SHEET 'My Workouts  with python'

#Sheety api endpoint
sheety_api_endpoint=SHEETY_API_ENDPOINT




#informacion sacada de la documentacion de la api https://sheety.co 
sheety_headers={
    'Content-Type': 'application/json',
    
}


date=datetime.today().strftime('%Y/%m/%d')


time=datetime.today().strftime('%I:%M:%S%p')


#podemos haber ingresado mas de 1 ejercicio por lo que itirenamos en nuestra 'exercise_list' que es una lista de diccionarios
for dic in exercises_list:
    
    
    #parametros que recibe nuestro post, de acuerdo a nuestro sheet ' My Workouts  with python' 
    sheety_parameters={
        'workout':{
            'date':date,
            'time':time,
            'exercise':dic['user_input'],
            'duration':dic['duration_min'],
            'calories':dic['nf_calories'],
        }
    }
    

    # Making a POST request para cada sheety_parameters
    sheety_response = requests.post(sheety_api_endpoint, headers=sheety_headers, json=sheety_parameters)
    
 
    # check status code for response received
    # success code - 200
    print(sheety_response)
    
    
    # # print content of request
    print(sheety_response.json())