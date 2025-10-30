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
def esperar_titulo_contiene(driver, texto_titulo, timeout=10):
  
    try:
        wait = WebDriverWait(driver, timeout)
        wait.until(EC.title_contains(texto_titulo))
        return True
    except:
        return False


def tomar_screenshot(driver, nombre_archivo):
    
    try:
        driver.save_screenshot(f"screenshots/{nombre_archivo}")
        print(f"Screenshot guardado: {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar screenshot: {e}")