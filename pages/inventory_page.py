from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
  
    _TITULO_PAGINA = (By.CLASS_NAME, "title")
    _PRODUCTOS = (By.CLASS_NAME, "inventory_item")
    _NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
    _PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
    _BOTON_AGREGAR_CARRITO = (By.CSS_SELECTOR, ".btn_inventory")
    _ICONO_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
    _BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    _MENU_HAMBURGUESA = (By.ID, "react-burger-menu-btn")
    _FILTRO_PRODUCTOS = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        titulo = self.wait.until(EC.visibility_of_element_located(self._TITULO_PAGINA))
        return titulo.text

    def obtener_productos(self):
        productos = self.wait.until(EC.presence_of_all_elements_located(self._PRODUCTOS))
        return productos

    def contar_productos(self):
        return len(self.obtener_productos())

    def obtener_primer_producto_info(self):
        productos = self.obtener_productos()
        if productos:
            primer_producto = productos[0]
            nombre = primer_producto.find_element(*self._NOMBRE_PRODUCTO).text
            precio = primer_producto.find_element(*self._PRECIO_PRODUCTO).text
            return {"nombre": nombre, "precio": precio}
        return None

    def verificar_menu_presente(self):
        try:
            menu = self.wait.until(EC.presence_of_element_located(self._MENU_HAMBURGUESA))
            return menu.is_displayed()
        except:
            return False

    def verificar_filtro_presente(self):
        try:
            filtro = self.wait.until(EC.presence_of_element_located(self._FILTRO_PRODUCTOS))
            return filtro.is_displayed()
        except:
            return False

    def agregar_primer_producto_al_carrito(self):
        botones = self.wait.until(EC.presence_of_all_elements_located(self._BOTON_AGREGAR_CARRITO))
        if botones:
            botones[0].click()
        return self

    def obtener_contador_carrito(self):
       
        try:
            badge = self.driver.find_element(*self._BADGE_CARRITO)
            return int(badge.text)
        except:
            return 0

    def hacer_click_carrito(self):
        icono_carrito = self.wait.until(EC.element_to_be_clickable(self._ICONO_CARRITO))
        icono_carrito.click()
        return self