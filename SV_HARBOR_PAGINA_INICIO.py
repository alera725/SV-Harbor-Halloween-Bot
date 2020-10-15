# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:46:54 2020

@author: alejandro.gutierrez
"""

# PAGINA INCIO
from selenium.webdriver.support.ui import WebDriverWait # Guardar en las paginas
from selenium.webdriver.support import expected_conditions as EC #Guardar en las paginas import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class initial_page():
    def __init__(self,my_driver):
        self.driver = my_driver
        self.userr = (By.ID, 'USER')
        self.passwordd = (By.ID, 'PASSWORD')
        self.buttonid = (By.ID, 'btnSignIn')
        
    def start_session(self,email,passwd):
        try:
            user_label = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.userr))
            user_label.send_keys(email)
            passwd_label = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.passwordd))
            passwd_label.send_keys(passwd)
            button_login = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.buttonid))
            button_login.click()
            
        except TimeoutException:
            print ("Loading -start_session- took too much time!")


    


