import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from utils.helpers import obtener_credenciales_validas


@pytest.fixture(scope="function")
def driver():
  
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    
    yield driver
    
   
    driver.quit()


@pytest.fixture(scope="function")
def login_exitoso(driver):

    credenciales = obtener_credenciales_validas()
    login_page = LoginPage(driver)
    
    login_page.abrir_pagina()
    login_page.realizar_login(
        credenciales["usuario"],
        credenciales["password"]
    )
    
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    
    outcome = yield
    rep = outcome.get_result()
    
    setattr(item, f"rep_{rep.when}", rep)
