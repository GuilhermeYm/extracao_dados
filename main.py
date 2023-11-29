from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl as op 
import os 



def limpar_tela():
    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')



def inicio():
    site = str(input("Qual é o site em que você irá extrair os dados: "))
    enter = input("Pressione enter para continuar")
    excel_txt = int(input("E por último precisamos saber se você quer colocar todos os dados em planilha ou em um arquivo txt\n[1] - Excel\n[2] - Txt\nSua opção:  "))
    nome_arquivo = str(input("Nome do arquivo: "))
    extrair_dados(site=site, nome_arquivo=nome_arquivo, excel_txt=excel_txt)


def extrair_dados(site, nome_arquivo, excel_txt):
    navegador = int(input("Temos duas opções de navegador para que você possa utilizar: [1] - Edge [2] - Chrome"))
    
    if navegador not in [1, 2]:
        print("Opção de navegador inválida.")
        return

    workbook = op.Workbook()
    workbook.create_sheet('Dados')
    pag = workbook['Dados']
    pag['A1'].value = 'Dados'

    if navegador == 1:
        xpath_option = int(input("Precisamos saber se você irá querer extrair um ou dois dados do site.\n[1] - Um dado\n[2] - Dois dados\n"))
        if xpath_option == 1:
            xpath = str(input("E por último, qual é o Xpath: "))
            driver = webdriver.Edge()
            driver.get(f"{site}")            
            dados = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            ) 
            if excel_txt == 1:
                for dado in dados:
                    pag.append([dado.text])
            else:
                with open(f"{nome_arquivo}.txt", "a") as file:
                    for dado in dados:
                        file.write(f"{dado.text}\n")
        else:
            xpath_1 = str(input("E por último, qual é o Xpath do primeiro dado: "))
            xpath_2 = str(input("E do segundo? "))
            driver = webdriver.Edge()
            driver.get(f"{site}")            
            dados_1 = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath_1))
            ) 
            dados_2 = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath_2))
            ) 
            if excel_txt == 1:
                for dado_1, dado_2 in zip(dados_1, dados_2):
                    pag.append([dado_1.text, dado_2.text])
            else:
                with open(f"{nome_arquivo}.txt", 'a') as file:
                    for dado_1, dado_2 in zip(dados_1.text, dados_2.text):
                        file.write(f"{dado_1.text, dado_2.text}\n")
    else:
        xpath_option = int(input("Precisamos saber se você irá querer extrair um ou dois dados do site.\n[1] - Um dado\n[2] - Dois dados\n"))
        if xpath_option == 1:
            xpath = str(input("E por último, qual é o Xpath: "))            
            driver = webdriver.Chrome()
            driver.get(f"{site}")            
            dados = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath))
            ) 
            if excel_txt == 1:
                for dado in dados:
                    pag.append([dado.text])
            else:
                with open(f"{nome_arquivo}.txt", 'a') as file:
                    for dado in dado:
                        file.write(f"{dado.text}\n")
        else:
            xpath_1 = str(input("E por último, qual é o Xpath do primeiro dado: "))
            xpath_2 = str(input("E do segundo? "))
            driver = webdriver.Chrome()
            driver.get(f"{site}")            
            dados_1 = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath_1))
            ) 
            dados_2 = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, xpath_2))
            ) 
            if excel_txt == 1:
                for dado_1, dado_2 in zip(dados_1, dados_2):
                    pag.append([dado_1.text, dado_2.text])
            else: 
                with open(f"{nome_arquivo}.txt", 'a') as file:
                    for dado_1, dado_2 in zip(dados_1.text, dados_2.text):
                        file.write(f"{dado_1.text, dado_2.text}\n")

    workbook.save(f'{nome_arquivo}.xlsx')

inicio()
