from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
  
    _TITULO_PAGINA = (By.CLASS_NAME, "title")
    _ITEMS_CARRITO = (By.CLASS_NAME, "cart_item")
    _NOMBRE_ITEM = (By.CLASS_NAME, "inventory_item_name")
    _PRECIO_ITEM = (By.CLASS_NAME, "inventory_item_price")
    _CANTIDAD_ITEM = (By.CLASS_NAME, "cart_quantity")
    _BOTON_CHECKOUT = (By.ID, "checkout")
    _BOTON_CONTINUAR_COMPRANDO = (By.ID, "continue-shopping")
    _BOTON_REMOVER = (By.CSS_SELECTOR, "[class*='cart_button']")
    
    def __init__(self, driver):
      
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def obtener_titulo(self):
    
        titulo = self.wait.until(
            EC.visibility_of_element_located(self._TITULO_PAGINA)
        )
        return titulo.text
    
    def obtener_items_carrito(self):
      
        try:
            items = self.wait.until(
                EC.presence_of_all_elements_located(self._ITEMS_CARRITO)
            )
            return items
        except:
            return []
    
    def contar_items_carrito(self):
       
        return len(self.obtener_items_carrito())
    
    def obtener_nombres_productos(self):
    
        items = self.obtener_items_carrito()
        nombres = []
        for item in items:
            nombre = item.find_element(*self._NOMBRE_ITEM).text
            nombres.append(nombre)
        return nombres
    
    def verificar_producto_en_carrito(self, nombre_producto):
       
        nombres = self.obtener_nombres_productos()
        return nombre_producto in nombres
    
    def obtener_info_primer_item(self):
        
        items = self.obtener_items_carrito()
        if items:
            primer_item = items[0]
            nombre = primer_item.find_element(*self._NOMBRE_ITEM).text
            precio = primer_item.find_element(*self._PRECIO_ITEM).text
            cantidad = primer_item.find_element(*self._CANTIDAD_ITEM).text
            return {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            }
        return None
