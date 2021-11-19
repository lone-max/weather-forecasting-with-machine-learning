import tkinter as tk
import requests
import tkinter.font
HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print ("this is the entry:", entry)

#c0017b092eb1486779116ced95fd7c3e
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving your weather'

    
    return final_str
            

def get_weather(city):
    weather_key = 'c0017b092eb1486779116ced95fd7c3e'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params= params)
    weather= response.jso n()

    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='pic.png')
backgorund_label = tk.Label(root, image=background_image)
backgorund_label.place( relwidth=1, relheight=1)

frame = tk.Frame(root, bg= '#BBECE7' , bd=5)
frame.place( relx=0.5 , rely=0.1, relwidth=0.75 ,relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Times New Roman', 17) )
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="get weather!", font=('Times New Roman', 17), command=  lambda:get_weather(entry.get()) )
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#BBECE7', bd=10)
lower_frame.place(relx=0.5 , rely=0.25 ,relwidth=0.75, relheight=0.6,anchor='n')

label = tk.Label(lower_frame, font=('Times New Roman', 17), anchor='nw', justify ='left' , bd=4)
label.place(relwidth=1, relheight=1)



root.mainloop()

def test_function():
    print("button clicked!")
    

