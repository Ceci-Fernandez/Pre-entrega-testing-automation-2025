from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"

    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self  
    def ingresar_usuario(self, usuario):
        input_usuario = self.wait.until(EC.visibility_of_element_located(self._USERNAME_INPUT))
        input_usuario.clear()
        input_usuario.send_keys(usuario)
        return self

    def ingresar_password(self, password):
        input_password = self.wait.until(EC.visibility_of_element_located(self._PASSWORD_INPUT))
        input_password.clear()
        input_password.send_keys(password)
        return self

    def hacer_click_login(self):
        boton_login = self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        boton_login.click()
        return self

    def realizar_login(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_password(password)
        self.hacer_click_login()
        return self

    def obtener_mensaje_error(self):
        try:
            error = self.wait.until(EC.visibility_of_element_located(self._ERROR_MESSAGE))
            return error.text
        except:
            return None