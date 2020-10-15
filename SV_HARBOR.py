# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:51:58 2020

@author: alejandro.gutierrez
"""

#Importar paqueterias
import os
import shutil
# Set dir
os.chdir('C:\\Users\\SET UP THE directory PATH') # relative path: scripts dir is under Lab

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
import time 
import datetime
from datetime import date
from calendar import monthrange
import calendar

from SV_HARBOR_PAGINA_INICIO import initial_page
from SV_HARBOR_PAGINA_WHOLESALE import whole_sale_page
from SV_HARBOR_PAGINA_PROCESO import process_page
import pandas as pd


class Download_SuperValue_Data_all_retailers(unittest.TestCase):
    
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.default_directory' : 'C:\\Users\\SET UP THE DOWNLOADS PATH'} 
        chrome_options.add_experimental_option('prefs', prefs)
      #  chrome_options.add_argument('--headless')
        chromedriver_path = 'C:\\Users\\SET UP THE PATH OF chromedriver'
        url = 'https://myhome.svharbor.com/siteminderagent/forms/svhlogin.fcc?TYPE=33554433&REALMOID=06-000d8ea6-308c-1c8b-8ca7-651f0aaa0000&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=$SM$DhN8BKiYjPa0wXV87nLVLAJXPtPpXtU8fiDQXhR7CAJ%2b1sh1reaPfFF%2f99NIqOJy&TARGET=$SM$https%3a%2f%2fmyhome%2esvharbor%2ecom%2fcontent%2fsvhb%2fhome%2ehtml' #SET UP MAIN URL FOR THE SV HARBOR PAGE
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
        self.driver.get(url)
        self.WebDriverWait = WebDriverWait
        #self.driver.implicity_wait(7)
        self.PageInitial = initial_page(self.driver)
        self.PageWholesale = whole_sale_page(self.driver)
        self.PageProcess = process_page(self.driver)
        self.dir_download = 'C:\\Users\\SET UP THE DOWNLOADS PATH AGAIN'
        self.driver.maximize_window()
    
    
    @unittest.skip('Not need now') #AQUI INICIA EL TEST PARA RETAILER INDIVIDUAL SE DESCARGA DESDE EL 01 DEL MES HASTA EL UTLIMO DIA DEL ULTIMO MES COMPLETO
    def test_Descarga_archivos_AmericanLicoriceCo(self):
        
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'XXXX'  
        pswd = 'XXXX' 
        
        #Seleccionamos el retailer deseado
        retailers = ' 24158 - American Licorice Co' # SELECT A MANUFACTURER OR PUT 'all' 
        
        #Fecha de hoy
        today = date.today()
        
        # format dd/mm/YY and we get a STR value 
        d1 = today.strftime("%d/%m/%Y")
        day = d1[0:2]
        month = d1[3:5]
        year = d1[6:11]
        
        days_month = monthrange(int(year), int(month))[1] #Number of days in current month
        current_week_number = date.today().isocalendar()[1] #Current week Number
        
        #Revisamos si el mes en el que estamos esta completo, sino nos regresamos al mes pasado
        if int(day) != days_month:
            month = '0'+str(+int(month)-1) #Nos regresamos al mes que esta completo 
            days_month = monthrange(int(year), int(month))[1] #Number of days in current month
        else:
            month = month
            
        #Ingresar el rango de fechas que se busca descargar dd/mm/yyyy ultimo mes
        fecha_inicio = month + '/' + '01' + '/' + year[0:2] #'08/01/20'
        fecha_fin = month + '/' + str(days_month) + '/' + year[0:2]  #'08/31/20'
        
        fecha_inicio_format = fecha_inicio.replace("/", "") #'080120'
        fecha_fin_format = fecha_fin.replace("/", "") #'083120'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        #ELIMINAR SOLO USAR CUANDO QUEREMOS FECHAS ESPECIFICAS Este batch solo es si queremos poner una fecha personalizada y no la ultima semana/mes...
        #fecha_inicio_format = '070120'
        #fecha_fin_format = '073120'
        
        self.PageInitial.start_session(email,pswd)
        self.PageWholesale.wholesale()
        self.PageProcess.first_window()
        self.PageProcess.clear_all()
        self.PageProcess.set_vendor(retailers)
        self.PageProcess.set_endweekday()
        self.PageProcess.set_date_range(fecha_inicio_format,fecha_fin_format)
        self.PageProcess.download_page()
        time.sleep(5)
        

        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue

        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
        new_name = 'SUPER VALU %s ' %retailers + str(Current_Date) + '.csv'
        shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP THE PATH DESIRED FOR THE DOWNLOAD FILE'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
       
        #Listo
        print("%s SV is READY!!" %retailers) 
        time.sleep(3)




    #@unittest.skip('Not need now') #AQUI INICIA EL TEST PARA HALLOWEEN SE DESCARGA DESDE EL INICIO HASTA EL DIA DE HOY
    def test_Descarga_archivos_Halloween(self):
        
        before = os.listdir(self.dir_download) 

        #Cargamos los datos del inicio de sesion
        email = 'XXXX'  
        pswd = 'XXXX' 
        
        #Seleccionamos el retailer deseado
        retailers = 'Halloween Data' # Cambiar a Halloween
        
        #Fecha de hoy
        today = date.today()
        
        # format dd/mm/YY and we get a STR value 
        d1 = today.strftime("%d/%m/%Y")
        day = d1[0:2]
        month = d1[3:5]
        year = d1[6:11]
        
        days_month = monthrange(int(year), int(month))[1] #Number of days in current month
        current_week_number = date.today().isocalendar()[1] #Current week Number
            
        #Ingresar el rango de fechas que se busca descargar dd/mm/yyyy 
        #En este caso solo nos interesan datos del 07 de Julio a la fecha de hoy
        #fecha_inicio = month + '/' + '01' + '/' + year[0:2] #'08/01/20'
        fecha_fin = month + '/' + str(day) + '/' + year[0:2]  #'08/31/20'
        
        fecha_inicio_format = '070120'
        fecha_fin_format = fecha_fin.replace("/", "") #'083120'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        self.PageInitial.start_session(email,pswd)
        self.PageWholesale.wholesale()
        self.PageProcess.first_window()
        self.PageProcess.clear_all()
        
        self.PageProcess.set_Halloween()
        
        self.PageProcess.set_endweekday()
        self.PageProcess.set_date_range(fecha_inicio_format,fecha_fin_format)
        self.PageProcess.download_page()
        time.sleep(5)
        

        #Esperar a que la descarga se complete
        after = os.listdir(self.dir_download) 
        change = set(after) - set(before)
        while len(change) != 1:
            after = os.listdir(self.dir_download) 
            change = set(after) - set(before)
            if len(change) == 1:
                file_name = change.pop()
                break
            else:
                continue

        #CHECAR LA ULTIMA DESCARGA (PARA CAMBIAR EL NOMBRE A LA ULTIMA DESCARGA)
        Current_Date = datetime.datetime.now().strftime("%d-%b-%Y %HHr %MMin") 
        Initial_path = self.dir_download 
        filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime) #Es el archivo mas nuevo del path 
        
        #Eliminamos los rows que no son parte de la data
        skipedrows = pd.read_csv(filename, skiprows=5) #NEW Skiprows
        skipedrows.to_csv(r'%s'%filename, index=False)        

        new_name = 'SUPER VALU %s ' %retailers + str(Current_Date) + '.csv'
        shutil.move(filename,os.path.join(Initial_path,r'%s' %new_name))
        
        
        #MOVER EL ARCHIVO A LA UBICACION DESEADA
        new_download = 'C:\\Users\\SET UP THE PATH DESIRED FOR THE DOWNLOAD FILE'
        shutil.move('%s'%self.dir_download+'\\%s'%new_name, '%s'%new_download+'\\%s'%new_name)
       
        #Listo
        print("%s SV Halloween Data is READY!!" %retailers) 
        time.sleep(1)




    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        
        
        
if __name__ == '__main__':
    unittest.main()
       
        
        
        
        
        
        
        
        
        

        