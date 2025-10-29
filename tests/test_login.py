import pytest
from pages.login_page import LoginPage
from utils.helpers import esperar_url_contiene, obtener_credenciales_validas


class TestLogin:
    
    def test_login_exitoso_validacion_url(self, driver):
     
        credenciales = obtener_credenciales_validas()
        login_page = LoginPage(driver)
        
        login_page.abrir_pagina()
        login_page.realizar_login(
            credenciales["usuario"],
            credenciales["password"]
        )
        
      
        assert esperar_url_contiene(driver, "/inventory.html"), \
            "No se redirigió correctamente a la página de inventario"
        assert "/inventory.html" in driver.current_url, \
            f"URL esperada debe contener '/inventory.html', pero es: {driver.current_url}"
    
    def test_login_exitoso_validacion_titulo(self, driver):
     
        credenciales = obtener_credenciales_validas()
        login_page = LoginPage(driver)
     
        login_page.abrir_pagina()
        login_page.realizar_login(
            credenciales["usuario"],
            credenciales["password"]
        )
       
        esperar_url_contiene(driver, "/inventory.html")
        assert driver.title == "Swag Labs", \
            f"Título esperado: 'Swag Labs', pero se obtuvo: '{driver.title}'"
    
    def test_login_con_credenciales_invalidas(self, driver):
      
        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        login_page.realizar_login("usuario_invalido", "password_invalida")
        
        mensaje_error = login_page.obtener_mensaje_error()
        assert mensaje_error is not None, "Debería mostrar un mensaje de error"
        assert "Epic sadface" in mensaje_error, \
            f"El mensaje de error debería contener 'Epic sadface', pero es: {mensaje_error}"
