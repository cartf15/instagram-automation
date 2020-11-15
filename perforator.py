# try :
#     from selenium import webdriver
# except NameError as e :
#     print  (e)
import sys
sys.setrecursionlimit(2000)

from selenium import webdriver
import chromedriver_binary 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time 
import pandas as pd
import logging
import os
import shutil



#Creación de directorios

driverPath='C:/Program Files/chromedriver/'
CHROMEDRIVER=driverPath+'chromedriver.exe'
USUARIO='nessieshop'
CONTRASEÑA='Trivium1224'


#usuarios
usuarios=['minisocolombiaoficial','marikaditasvarias_','tropicalstorebga','tenderkiss.store','koistore_bog']





def create_msg(rootPath,name):
    pass

def __browser__ (CHROMEDRIVER):

    browser = webdriver.Chrome(
        executable_path =CHROMEDRIVER)
    browser.maximize_window()
    browser.get('https://www.instagram.com/')
    return browser


def __LoginIG__(browser,usuario,contraseña):
    
    
   
    try : 

        search_xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, search_xpath)))
        search_box.clear()
        time.sleep(1)
        pyperclip.copy(usuario)
        search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
        time.sleep(2)
    except Exception as e:
        print(e)

    try : 

        search_xpath = '//*[@id="loginForm"]/div/div[2]/div/label/input'
        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, search_xpath)))
        search_box.clear()
        time.sleep(1)
        pyperclip.copy(contraseña)
        search_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
        time.sleep(2)
    except Exception as e:
        print(e)

    login_path='//*[@id="loginForm"]/div/div[3]/button/div'
    login=browser.find_element_by_xpath(login_path)
    login.click()

    time.sleep(5)
    try: 
        # notnow_path='//button[@type="button"]'
        notnow_path='/html/body/div[1]/section/main/div/div/div/div/button'
        notnow=browser.find_element_by_xpath(notnow_path)
        notnow.click()
    except Exception as e: 
        print(e)

    time.sleep(5)
    try: 

        notnow2_path='/html/body/div[4]/div/div/div/div[3]/button[2]'
        notnow2=browser.find_element_by_xpath(notnow2_path)
        notnow2.click()
    except Exception as e: 
        print(e)


def __buscaUsuario__(browser,usuarios):

    for usuario in usuarios: 
        usr_search_path='/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input'
        search_box = WebDriverWait(browser, 500).until(
            EC.presence_of_element_located((By.XPATH, usr_search_path)))
        search_box.clear()
        time.sleep(1)
        pyperclip.copy(usuario)
        search_box.send_keys(Keys.SHIFT, Keys.INSERT) # Keys.CONTROL + "v"
        search_box.send_keys(Keys.ENTER)
        time.sleep(5)
        try: 

            user_path='/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a/div/div[2]/div/span'
            user=browser.find_element_by_xpath(user_path)
            user.click()
        except Exception as e: 
            print(e)
        time.sleep(5)
        try: 

            user_path='/html/body/div[1]/section/main/div/header/section/ul/li[2]/a'
            user=browser.find_element_by_xpath(user_path)
            user.click()
        except Exception as e: 
            print(e)
        time.sleep(5)
        
        for follow in range(100):
            time.sleep(randrange(3)*random())
            try: 

                
                follow_path='/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(follow)
                follow=browser.find_element_by_xpath(follow_path)
                follow.click()
            except Exception as e: 
                print(e)

        
            
            
        
        
        break


        # try : 
        #     group_xpath = f'//span[@title="{group}"]'
        #     group_title = browser.find_element_by_xpath(group_xpath)

        #     group_title.click()

    #         time.sleep(1)

    #         input_xpath = '//div[@contenteditable="true"][@data-tab="6"]'
    #         input_box = browser.find_element_by_xpath(input_xpath)

    #         pyperclip.copy(msg.format(group.split()[0]))
    #         input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
    #         input_box.send_keys(Keys.ENTER)

    #         time.sleep(2)
    #         print('Mensaje enviado')     
    #     except Exception as e:
    #         logging.info(e)
    #         print('No se logró enviar el mensaje')
    # print('Loop out')

browser=__browser__(CHROMEDRIVER)
__LoginIG__(browser,USUARIO,CONTRASEÑA)
__buscaUsuario__(browser,usuarios)