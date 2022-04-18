from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date
import json
import os

def set_driver_options(chromedriver_url):
    options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    options.add_argument("disable-gpu")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    service = Service(chromedriver_url)
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

def auto_login(driver, username, password):
    driver.get('https://ow-prd.osstem.com/login')
    driver.find_element(By.ID, 'i_id').send_keys(username)
    driver.find_element(By.ID, 'i_pass').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'btn_login').click()
    
current_dirname = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dirname, 'config.json')

with open(config_file_path, "rt", encoding="UTF8") as json_file:
    config = json.load(json_file)
    username = config['username']
    password = config['password']
    chromedriver_url = config['chromedriver']
    
    driver = set_driver_options(chromedriver_url)
    auto_login(driver, username, password)

    # driver.close()

print('completed')