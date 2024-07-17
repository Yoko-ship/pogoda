import requests
import json
from tkinter import *
from tkinter import ttk



userInput = ""
def show_message():
    global userInput
    global result
    userInput = entry.get()
    return userInput


root = Tk()
root.title("Pogoda")
root.geometry("300x300")


label = ttk.Label(text="Введите город:")
label.pack(anchor=NW,padx=6,pady=6)

#* Аналог input только в tkinter
entry = ttk.Entry(font=("Arial",14))
entry.pack(anchor=NW,padx=6,pady=6)

#* button +  обработчик событий
btn = ttk.Button(text="Click",command=show_message)
btn.pack(anchor=NW,padx=6,pady=6)


root.mainloop()

city = userInput
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data,indent=2)
temparatureRound = round(weather_data['main']['temp'])
temparaturefeels = round(weather_data['main']['feels_like'])

result =  f"Сейчас в городе {city}: {temparatureRound} °C, ощущается как: {temparaturefeels} "

label2 = ttk.Label(text=result,padding=8,foreground="#01579B",background="#B3E5FC")
label2.pack(anchor=NW,padx=10,pady=10)
root.mainloop()

