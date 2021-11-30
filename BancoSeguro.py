import pandas as pd
from  selenium import webdriver
import openpyxl
import  pyautogui
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def acessar(self, site):
        self.chrome.get(site)

    def login(self):
        logim=self.chrome.find_element_by_css_selector('#EUsuario_CAMPO')
        senha=self.chrome.find_element_by_css_selector('#ESenha_CAMPO')
        entrar=self.chrome.find_element_by_css_selector('#lnkEntrar')



        logim.send_keys('PAM_4766_DDIAS')

        senha.send_keys('Digital2')


        entrar.click()

    def INSS(self):
        inss=self.chrome.find_element_by_css_selector('#navbar-collapse-funcao > ul > li:nth-child(4) > a')
        




if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessar('http://wss.credisim.com.br/BSGWEBSITES/WebAutorizador/Login/AC.UI.LOGIN.aspx?FISession=4c8bfc306923')
    chrome.login()
    sleep(5)
    chrome.INSS()