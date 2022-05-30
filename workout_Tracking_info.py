import requests
import datetime as dt
import os


ID =os.environ["APP_ID"]
API=os.environ["API_KEY"]
exercise_endpoint=" https://trackapi.nutritionix.com/v2/natural/exercise"
USERNAME =os.environ["username"]
PASSWORD =os.environ["password"]

exercise_text=input("what did you do today?: ")

headers={
    "x-app-id": ID,
    "x-app-key": API,

}
parameters= {
    "query":exercise_text,
    "age": "25",
    "gender": "Female",
    "weight_kg": "60.0"

}

response= requests.post(url=exercise_endpoint, json = parameters,headers=headers)
print(response.status_code)
result = response.json()
print(result)

#To get the current date and time
today = dt.datetime.now()
date=today.strftime("%d/%m/%Y")
time= today.strftime("%X")

#To post data to google sheet
sheety_endpoint= "https://api.sheety.co/686865192a864917c5033af7604e2f71/workoutTracking/workouts"

#get key values from nutriotionix result(code above)
for exercise in result["exercises"]:
    workouts_inputs= {
        "workout":{
        "date":date,
        "time":time,
        "exercise":exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
    }
}
    sheet_response= requests.post(url =sheety_endpoint,json= workouts_inputs)
    print(sheet_response.text)
#basi authetication
    sheet_auth=requests.get(sheety_endpoint, json= workouts_inputs, auth=(USERNAME, PASSWORD))