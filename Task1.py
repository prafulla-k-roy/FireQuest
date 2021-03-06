'''
Team name: Peace
Team members: 
-> Prafulla Kumar Roy (Prafulla Kumar Roy#4108)
-> Utkarsh Saurav (utkarsh_saurav#5287)
-> Vaibhav Mani (demon_28f#2042)
'''

import requests

# Accessing Data form API
response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")

# Converting the data in string form to Dictionary
w_data = response.json()

# The data we actually need lies in this list
lst = w_data['list']

# Getting user's choice
ch = int(input("1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit\n"))

if ch == 1:
    date = input("Enter date (YYYY-MM-DD): ")
    for i in range(0, len(lst)):
        weather_data = lst[i]
        date_time = weather_data['dt_txt'].split(' ')   # Getting date and time
        if date == date_time[0]:
            w = weather_data['weather']
            weather = w[0]
            print("Date: ", date, "\tTime: ", date_time[1], "\tWeather status: ", weather['main'], "\tDescription: ", weather['description'])
        else:
            print("Data for the given date is not available.")
elif ch == 2:
    date = input("Enter date (YYYY-MM-DD): ")
    for i in range(0, len(lst)):
        weather_data = lst[i]
        date_time = weather_data['dt_txt'].split(' ')   # Getting date and time
        if date == date_time[0]:
            wind = weather_data['wind']
            print("Wind Speed on ", date, " at time ", date_time[1], " is ", wind['speed'], " miles per hour.")
        else:
            print("Data for the given date is not available.")
elif ch == 3:
    date = input("Enter date (YYYY-MM-DD): ")
    for i in range(0, len(lst)):
        weather_data = lst[i]
        date_time = weather_data['dt_txt'].split(' ')   # Getting date and time
        if date == date_time[0]:
            t_p = weather_data['main']
            print("Air pressure on ", date, " at time ", date_time[1], " is ", t_p['pressure'], " Pascal.")
        else:
            print("Data for the given date is not available.")
elif ch == 0:
    exit()
else:
    print("Wrong input, you dummy!!!")
