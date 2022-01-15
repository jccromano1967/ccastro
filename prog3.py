
from distutils import command
from tkinter import Entry, Label,Text
import tkinter as tk
from xml.etree.ElementTree import tostring
import pip._vendor.requests
import json
import datetime
from pip._vendor import requests
 
from pprint import pprint

from tkinter import *


from tkinter import ttk
from tkinter import messagebox


def obtener_info():
      print(lista_desplegable.get())
      ciudad = lista_desplegable.get()
      BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
      URL = BASE_URL + "q=" + ciudad + "&appid=" + 'fdf1e72b04592aff43694e18e2a2eb00' 
      response = requests.get(URL)
      raiz = Tk()            
      if response.status_code == 200:                
                var1 = tk.StringVar()    #Crear variable
                # getting data in the json format
                data = response.json()
                
                hora_UTC = datetime.datetime.fromtimestamp(data['dt'])
                amanecer = datetime.datetime.fromtimestamp(data['sys']["sunrise"])
                atardecer = datetime.datetime.fromtimestamp(data['sys']["sunset"])
                
                
                
                
                
                
                
                raiz.title("Resultado del Clima")
                raiz.geometry("300x400")
                raiz.config(bg="blue")                   
                raiz = Text(raiz,width=30,height =50)
                raiz.pack()
                raiz.insert(INSERT,ciudad)
                raiz.insert(INSERT,' \n')                
                raiz.insert(INSERT,('Temperatura:', (data['main']['temp'])))    
                raiz.insert(INSERT,' \n') 
                raiz.insert(INSERT,('Velocidad del Viento:', data['wind']['speed']))    
                raiz.insert(INSERT,' \n') 
                raiz.insert(INSERT,('Presión Atmosférica:', data['main']['pressure']))    
                raiz.insert(INSERT,' \n') 
                raiz.insert(INSERT,('Humedad:', data['main']['humidity']))    
                raiz.insert(INSERT,' \n') 
                raiz.insert(INSERT,('Nubosidad:',str(data['clouds']['all'])+ "%"))    
                raiz.insert(INSERT,' \n') 
                raiz.insert(INSERT,('Visibilidad:',str(data['visibility']/100)+"%"))    
                raiz.insert(INSERT,' \n')
                raiz.insert(END," - ")
                raiz.mainloop()                
               
      else:
                  # showing the error message
                 print("Error in the HTTP request")
                
                 
ventana = Tk()
ventana.title("ciudades")
ventana.geometry('300x190')

#lista
lista_desplegable = ttk.Combobox(ventana,width=17)
lista_desplegable.place(x=30,y=77)

opcio = ["Tokio ",	"Delhi ",	"Shanghai ",	"Sao Paulo ",	"Mexico City ",	"Cairo ",	"Mumbai ",	"Beijing ",	"Dhaka ",	"Osaka ",	"New York ",	"Karachi ",	"Buenos Aires ",	"Chongqing ",	"Istanbul ",	"Kolkata ",	"Manila ",	"Lagos ",	"Rio de Janeiro ",	"Tianjin ",	"Kinshasa ",	"Guangzhou ",	"Los Angeles ",	"Moscow ",	"Shenzhen ",	"Lahore ",	"Bangalore ",	"Paris ",	"Bogotá ",	"Jakarta ",	"Chennai ",	"Lima ",	"Bangkok ",	"Seoul ",	"Nagoya ",	"Hyderabad ",	"London ",	"Tehran ",	"Chicago ",	"Chengdu ",	"Nanjing ",	"Wuhan ",	"Ho Chi Minh City ",	"Luanda ",	"Ahmedabad ",	"Kuala Lumpur ",	"Xian ",	"Hong Kong ",	"Dongguan ",	"Hangzhou ",	"Foshan ",	"Shenyang ",	"Riyadh ",	"Baghdad ",	"Santiago ",	"Surat ",	"Madrid ",	"Suzhou ",	"Pune ",	"Harbin ",	"Houston ",	"Dallas ",	"Toronto ",	"Dar es Salaam ",	"Miami ",	"Belo Horizonte ",	"Singapore ",	"Philadelphia ",	"Atlanta ",	"Fukuoka ",	"Khartoum ",	"Barcelona ",	"Johannesburg ",	"Saint Petersburg ",	"Qingdao ",	"Dalian ",	"Washington, D.C. ",	"Yangon ",	"Alexandria ",	"Jinan ",	"Guadalajara "
]
lista_desplegable['values']=opcio

Button(ventana,text="Clima",bg='orange',command=obtener_info).place(x=170,y=77)
            
ventana.mainloop()