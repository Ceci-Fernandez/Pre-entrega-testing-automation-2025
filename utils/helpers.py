from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def esperar_url_contiene(driver, texto_url, timeout=10):
    
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.url_contains(texto_url))
        return True
    except:
        return False

def obtener_credenciales_validas():

    return {
        "usuario": "standard_user",
        "password": "secret_sauce"
    }
