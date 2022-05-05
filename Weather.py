import requests

cityName = input("Please enter a city name : ")
api_address = 'http://api.openweathermap.org/data/2.5/weather?q='+cityName+'&appid=88934e5134d0518b4a65b62a2a9835ec'
json_data = requests.get(api_address).json()
print(json_data)
import requests,json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
api_key = ""
def credits():
    cred=Toplevel()
    cred.geometry('300x300')
    cred.title('Credits for this Weather Project ')
    Label(cred,text='Created in May 2022').grid(row=1,column=3)
    Label(cred,text='Made by Lauren Rose').grid(row=2,column=2)
def proceed():
    city=cit.get()
    if city=='':
        return messagebox.showerror('Error','Enter City Name')
    elif api_key=='your api key':
        return messagebox.showerror('Error','Enter your api key')

    else:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        complete_url = base_url + "appid=" + api_key + "&q=" + cityname 
        response = requests.get(complete_url) 
        x = response.json()  
        if x["cod"] != "404": 
  
            y = x["main"] 
            currenttemp = y["temp"] 
            currentpressure = y["pressure"] 
            currenthumidiy = y["humidity"]
            z = x["weather"] 
            weather_description = z[0]["description"]  
            Label(home,text='Temperature: '+str(round(currenttemp-272.15))+' degree celsius').place(x=2,y=90)
            Label(home,text='Atmospheric Pressure: '+str(currentpressure)+' hPa').place(x=2,y=120)
            Label(home,text='Humidity: '+str(currenthumidiy)).place(x=2,y=150)
            Label(home,text='Description: '+str(weather_description)).place(x=2,y=180)
        else: 
            return messagebox.showerror('Ope! Sorry, there is an Error','No City Found')
   

home=Tk()
home.geometry('500x500')
home.title('Lauren Rose Weather App')
cit=StringVar()
Label(home,text=' Weather',font='arial 15 bold').grid(row=1,column=3)
Button(home,text='Project Details',command=credits).grid(row=1,column=4)
Label(home,text='Enter The name of a city:').grid(row=2,column=1)
Entry(home,width=15,textvariable=cit).grid(row=2,column=2)
Button(home,text='sumbit',command=proceed).grid(row=3,column=3)




home.mainloop()