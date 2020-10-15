# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:55:41 2020

@author: alejandro.gutierrez
"""

# PAGINA DEL PROCESO
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time

class process_page():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.warehouse_store_shipments = (By.XPATH, '//*[@id="31"]')
        self.shipment_history = (By.XPATH, '//*[@id="pageMenu"]/dd[8]/div/a')
        self.buttonid = (By.ID, 'btnSignIn')

        self.clearall = '//*[contains(@id, "j_idt")]'
        
        self.favorites_button = (By.ID, 'facetMyFavSearch') 
        self.tablefavorite_searches = '//*[contains(@id, "myFavoriteSearches:")]' #El ID numero 5 es el bueno 

        
        self.vendor_button = (By.XPATH, '//*[@id="facetVendor"]/div[1]') 
        self.select_all_vendors = (By.ID,'vendor:j_idt948')
        
        self.clear_vendors = '//*[contains(@id, "vendor:j_idt")]' #AL FINAL USAMOS EL CONTAIN PARA BUSCAR EL MAS PARECIDO CON ESE TEXTO  Full xpath = '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[2]/span[2]/span[4]/div/div[2]/span/div[1]/a'

        self.table_vendors_filter = (By.ID,'vendor:filterVendors')
        self.date_end_week_button = (By.XPATH,'//*[@id="facetWeekEnding"]/div[1]') #CLick en seccion End Week
        self.day_selected = (By.ID, 'weekEnding:filterWeekEnding:5') #Saturday end week 
        self.date_button = (By.XPATH, '//*[@id="facetDate"]/div[1]') #Click en seccion Date 
        self.date_range = '//*[@id="date:dateEntryType:1"]' #ELEGIR DATE RANGE EN LUGAR DE SINGLE DAY  
        self.day_initial = 'date:rangeStartDate'
        self.day_end = 'date:rangeEndDate'
        
        self.pressok = (By.XPATH, '//*[@id="ui-datepicker-div"]/div[2]/button') 

        self.add_dates_button = '//*[contains(@id, "date:j_idt")]' #AL FINAL USAMOS EL CONTAIN PARA BUSCAR EL MAS PARECIDO CON ESE TEXTO  
        
        self.download_button = (By.XPATH, '//*[@id="downloadmenu_label"]/a')
        self.store_level_detail = '//*[contains(@id, "j_idt")]' 
        self.view_downloads = (By.ID, 'viewDownloads')
        self.Download_Hour = (By.ID, 'downloadDetailsTable:0:reqTS')
        self.Download_Table = (By.ID, 'downloadDetailsTable:tb')
        self.status_down = 'downloadDetailsTable:0:status' 
        self.refresh_button = 'refresh'
        self.file_name = (By.ID, 'downloadDetailsTable:0:docName')
        self.close_window_download = (By.XPATH ,'//*[@id="topLinks"]/a')
        
    def first_window(self):
        try:
            warehouse_store_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.warehouse_store_shipments))
            warehouse_store_button.click()
            
            #Cuidado a veces no es necesario dar click en el WholeSale ya esta clickado
            shipment_history_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.shipment_history))
            shipment_history_button.click()

        except TimeoutException:
            print ("Loading -start_session- took too much time!")
            
    def clear_all(self):
        try:
            
            c_all = self.driver.find_elements_by_xpath(self.clearall)[3] #El 3 es el de clear all
            dynamic_id_clear_all = c_all.get_attribute("id")
            dynamic_id_clear_all_by = (By.ID,dynamic_id_clear_all)
            clear_a = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(dynamic_id_clear_all_by)) 
            clear_a.click()
            time.sleep(2)
            
        except TimeoutException:
            print ("Loading -clear_all- took too much time!")
            
    def set_vendor(self,retailers):
        try:
            vendorbutt = WebDriverWait(self.driver,200).until(EC.element_to_be_clickable(self.vendor_button))
            vendorbutt.click()
            
            #Select only the vendor we guess
            retailer = retailers
            table = self.driver.find_element_by_xpath("//*[@id='vendor:filterVendors']/tbody/tr/td/label[contains(text(), '%s')]" %retailer)
            table.click()

        except TimeoutException:
            print ("Loading -set_vendor- took too much time!")
    
    def set_MonthlyDC(self):
        try:
            
            fav_button = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.favorites_button))
            fav_button.click()
            
            
            fav_table = self.driver.find_elements_by_xpath(self.tablefavorite_searches)[4] #El ID 4 es el que me interesa
            dynamic_id_fav_table = fav_table.get_attribute("id")
            dynamic_id_fav_table_by = (By.ID, dynamic_id_fav_table)
            
            #Encontrar el td que contenga la palabra "Monthly DC" #//*[@id="myFavoriteSearches:j_idt123:4:j_idt125"]
            find_text = 'Monthly DC'
            #mdc = self.driver.find_element_by_xpath("//*[@id='%s']/tbody/tr/td[contains(text(), '%s')]" % (dynamic_id_fav_table, find_text))
            mdc_table =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(dynamic_id_fav_table_by))
            mdc_table.find_element(By.LINK_TEXT,'%s' %find_text).click()
            #mdc_table.click()
            time.sleep(4)
            
            
        except TimeoutException:
            print ("Loading -set_MotnhlyDC- took too much time!")   
            
            
    def set_Halloween(self):
        try:
            
            fav_button = WebDriverWait(self.driver,50).until(EC.visibility_of_element_located(self.favorites_button))
            fav_button.click()
            
            fav_table = self.driver.find_elements_by_xpath(self.tablefavorite_searches)[4] #El ID 4 es el que me interesa
            dynamic_id_fav_table = fav_table.get_attribute("id")
            dynamic_id_fav_table_by = (By.ID, dynamic_id_fav_table)
            
            #Encontrar el td que contenga la palabra "Haloween candy report1" 
            find_text = 'Haloween candy report1'
            mdc_table =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(dynamic_id_fav_table_by))
            mdc_table.find_element(By.LINK_TEXT,'%s' %find_text).click()
            time.sleep(4)
            
        except TimeoutException:
            print ("Loading -set_Halloween- took too much time!") 
            
            
            
    def set_endweekday(self):
        try:
            date_end_button = WebDriverWait(self.driver,200).until(EC.visibility_of_element_located(self.date_end_week_button))
            date_end_button.click()
            
            time.sleep(2)
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.day_selected)).click()
            

        except TimeoutException:
            print ("Loading -set_endweekday- took too much time!")


    def set_date_range(self,fecha_inicio,fecha_fin):
        try:
            datebutton = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.date_button))
            datebutton.click()
            
            time.sleep(2)
            
            rango = self.driver.find_element_by_xpath(self.date_range)
            rango.click()
            #select_multiple_range.click()
            
            time.sleep(5)
           
            dia_end = self.driver.find_element_by_id(self.day_end)
            dia_end.send_keys(fecha_fin) #EL VALOR DE LA FECHA EN FORMATO MMDDYY EJ. 080120 (08 DE AGOSTO DEL 2020)
            
            #dia_end.submit()
            
            dia_start = self.driver.find_element_by_id(self.day_initial)
            dia_start.send_keys(fecha_inicio) #EL VALOR DE LA FECHA EN FORMATO MMDDYY EJ. 080120 (08 DE AGOSTO DEL 2020)
            
            time.sleep(2)
            
            #MODIFICAR CON DYNAMIC ID
            add_button_contain = self.driver.find_elements_by_xpath(self.add_dates_button)[1] #VER QUE NUMERO DE ELEMENTO ES EL ID DE ADD DATES [4] EJ.
            dynamic_id_add_button = add_button_contain.get_attribute("id")
            #print(dynamic_id_add_button)
            add_button = self.driver.find_element_by_id(dynamic_id_add_button)
            add_button.click()
            
            time.sleep(2)
            

        except TimeoutException:
            print ("Loading -set_date_range- took too much time!")


    def download_page(self):
        try:
            down_button = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.download_button))
            down_button.click()
            
            sld = self.driver.find_elements_by_xpath(self.clearall)[2] #El 3 es el de clear all
            dynamic_id_sld = sld.get_attribute("id")
            sld_button = self.driver.find_element_by_id(dynamic_id_sld)
            sld_button.click()
            
            time.sleep(1)
            view_downs = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.view_downloads))
            view_downs.click()
                        
            #CHECAR LO DEL ROW DE LA HORA Y EL NOMBRE PARA UBICAR EL ARCHIVO QUE NOSOTROS DESCARGAMOS
            #Aqui es donde debo de fijarme en el row de la descarga que yo hice, la hora y la descripcion que tenga: Store Level Detail
            #DOWNLOAD TYPE: VENDOR_SHIPMENT_HISTORY ID: 'downloadDetailsTable:0:type' XPATH: '//*[@id="downloadDetailsTable:0:type"]'
            #HORA 09/04/20 15:30:04 id = 'downloadDetailsTable:0:reqTS' xpath = '//*[@id="downloadDetailsTable:0:reqTS"]/div
            #DESCRIPCION Vendor Shipment Store Level Detail	 id = 'downloadDetailsTable:0:desc' xpath = '//*[@id="downloadDetailsTable:0:desc"]'  texto debe decir: 'Vendor Shipment Store Level Detail'
            
            time.sleep(2) #Usar los WebdriverWaits
            HOUR = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.Download_Hour)) #webdriver.find_element_by_id('downloadDetailsTable:0:reqTS').text
            HOUR = HOUR.text
            print(HOUR)
            
            #El status que debemos de estar checando es en donde este estos datos en el renglon y despues el click igual 
            
            #FORMA 1 TE REGRESA TODOS LOS ROWS DE LA COLUMNA INDICADA y da click en el row donde encontro un valor especifico
            table_id = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.Download_Table)) #self.driver.find_element(By.ID, 'downloadDetailsTable:tb')
            rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
            
            for row in rows:
                col1 = row.find_elements(By.TAG_NAME, "td")[1] #Revisamos la HORA
                print(col1)
                if(col1.text == HOUR):
                    col = row.find_elements(By.TAG_NAME, "td")[4] #Revisamos la columna donde tenemos que clickar
                    actual_status = col.text
                    print(actual_status)
                    break
                else:
                    continue            
    
            while actual_status!='Ready':
                self.driver.find_element_by_id(self.refresh_button).click()
                time.sleep(5)
                table_id = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.Download_Table)) #self.driver.find_element(By.ID, 'downloadDetailsTable:tb')
                rows = table_id.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
                
                for row in rows:                    
                    my_element_id = "td"
                    ignored_exceptions=(NoSuchElementException,StaleElementReferenceException)
                    WebDriverWait(self.driver,20,ignored_exceptions=ignored_exceptions)\
                                            .until(EC.presence_of_element_located((By.TAG_NAME, my_element_id)))
                                        
                    col1text = row.find_elements(By.TAG_NAME, "td")[1].text #Revisamos la HORA
                    #print(col1text)
                    #col1text = col1.text
                    if(col1text == HOUR):
                        actual_status = row.find_elements(By.TAG_NAME, "td")[4].text #Revisamos la columna donde tenemos que clickar
                        print(actual_status)
                        #actual_status = col.text
                        #if status es Failed cerrar todo y cancelar operacion
                        if (actual_status == 'Failed'):
                            break
                        else:
                            continue            
                    else:
                        continue
            
            #El texto ya esta en READY! o FAILED!
            
            if actual_status == 'Ready':
                for row in rows:
                    col1 = row.find_elements(By.TAG_NAME, "td")[1] #Revisamos la HORA
                    if(col1.text == HOUR):
                        fname = row.find_elements(By.TAG_NAME, "td")[3] #Revisamos la columna donde tenemos que clickar
                        fname.click()
                        break
                    else:
                        continue
        
            else:
                print('Error: Download status "Failed" ')
            
            
        except TimeoutException:
            print ("Loading -download_page- took too much time!")
        

    def close_window(self):
        try:
            
            c_window = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.close_window_download))
            c_window.click()    
            time.sleep(1)
            
        except TimeoutException:
            print ("Loading -close_window- took too much time!")
            