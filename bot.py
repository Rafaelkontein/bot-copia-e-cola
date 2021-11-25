from selenium import webdriver
from time import sleep
import pyautogui
import Pegando_dados

class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--profile-directory=1')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_id('sidebar-menu')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)



    def pegar_dados(self):
        import openpyxl

        pedidos = openpyxl.load_workbook('xassaas.xlsx')
        nomes_planilhas = pedidos.sheetnames  # aqui vc ta pegadno quantas paginas tem no excel

        planilhas1 = pedidos['Planilha1']  # Aqui vc ta pegando tudo que tem na planilha

        dados = []
        for camp in planilhas1['a']:  # aqui vc ta pegando exatamente oq tem na coluna b da planilha
            if camp.value is not None:

                dados.append(camp.value)
                b = len(dados)
                for camp.value in range (b):
                     list=[]
                     sleep(3)
                     dados1 = (dados)
                     sleep(3)
                     btn_buscar=self.chrome.find_element_by_id('consulta')
                     campo_escrever=self.chrome.find_element_by_id('busca')
                     sleep(3)
                     campo_escrever.send_keys(dados1)
                     sleep(2)
                     btn_buscar.click()
                     sleep(3)
                     btn_selecionar = self.chrome.find_element_by_class_name('swal2-select')

                     btn_selecionar.click()
                     sleep(0.5)
                     pyautogui.press('down')
                     sleep(0.5)
                     pyautogui.press('enter')
                     btn_ok = self.chrome.find_element_by_css_selector(
                         'body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled')
                     btn_ok.click()
                     sleep(3)
                     financeiro = self.chrome.find_element_by_class_name('text-green').text
                     margim = []
                     margim.append(financeiro)
                     print(margim)
                     campo_escrever.clear()







    def atualizar(self):
        try:
            pyautogui.press('f5')
        except Exception as b:
            print('Erro ao atulizar',b)

    def acessa(self, site):  # Aqui o site que vc vai entrar
        self.chrome.get(site)

    def sair(self): #aqui é para sair do site
        self.chrome.quit()

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector(# aqui ta pegando o seletor para clicar
                '#huro-app > div.view-wrapper > div > div > div.page-content-inner > div > div.onboarding-wrap > div > div:nth-child(2) > div > a.button.h-button.is-primary.is-outlined.is-rounded.is-raised')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    #def faz_logout(self):
            # try:
            #    perfil = self.chrome.find_element_by_css_selector(# aqui ta pegando o seletor para clicar
        #      'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-lg-flex > details > details-menu > form > button')
            #   perfil.click()
            #  except Exception as e:
    # print('Erro fazer logout:', e)

   # def verifica_usuario(self, usuario):
            # profile_link = self.chrome.find_element_by_class_name(
        #     'user-profile-link')
            #  profile_link_html = profile_link.get_attribute('innerHTML')
    # assert usuario in profile_link_html

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('login')# aqui vc etsá pegando o id do campo de escrever
            input_password = self.chrome.find_element_by_id('senha')# aqui voce está pedindo =
            btn_login = self.chrome.find_element_by_name('submit')

            input_login.send_keys('61686C') # aqui voce está pedindo para escrever no login
            input_password.send_keys('123456')  # Aqui voce está falando para escrever a senha
            sleep(3)
            btn_login.click()



        except Exception as e:
            print('Erro ao fazer login:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://fdevendas.com.br/acesso/login')



    chrome.faz_login()
    sleep(3)
    chrome.atualizar()
    sleep(3)
    chrome.clica_perfil()

    sleep(2)
    chrome.pegar_dados()