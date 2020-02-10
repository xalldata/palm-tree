#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def testFct(entry):
    print("this is the entry :", entry)

   
def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str ='City: %s \nConditions: %s \nTemperature: (°F) %s' % (name, desc, temp)
    except:
        final_str = 'This city does not exist!'
    return final_str

def get_weather(city):
    weather_key = 'Enter the key provided by openweathermap.org'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    label['text'] = format_response(weather)
    
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])
    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


canvas.configure(background='#77DAB4')


frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18), anchor = 'nw', justify='left', bd=4, fg="black")
label.place(relwidth=1, relheight=1)

root.mainloop()


# In[ ]:




