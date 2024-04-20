import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image , ImageTk
import ttkbootstrap as bstr
import io
import PIL

# function weather
def get_weather(city):
    API_key = "b9a7751d834d0a91e9b44aa120377cbb"
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Error" ," City not found")
        return None
    
    # parse the respon JSON
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']
    
    # get icon url
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url,temperature,description,city,country)

#  function search

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # if city is found,unpack the weather information 
    icon_url,temperature,description,city,country = result
    location_label.configure(text=f"{city},{country}")
    
    data = requests.get(icon_url,stream=True).raw
    image = Image.open(data)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image =icon
    
    temperature_label.configure(text=f"Temperature: {temperature:.2f}c")
    description_label.configure(text=f"Description: {description}")
    
    

root = bstr.Window(themename="morph")
root.title("weather app")
root.geometry("400x400")

#entry widget -> to enter the city name
city_entry = bstr.Entry(root,font="Helvetica, 18")
city_entry.pack(pady =10)

#button widget -> to searcch for the weather information
search_button = bstr.Button(root,text="search",command=search )
search_button.pack(pady = 10)

location_label = tk.Label(root)
location_label.pack(pady=20)

#label city country 
icon_label = tk.Label(root)
icon_label.pack()

#label temperature
temperature_label = tk.Label(root, font="Helvectia, 20")
temperature_label.pack()

# label description
description_label = tk.Label(root,font="Helvectia, 20")
description_label.pack()

root.mainloop()
