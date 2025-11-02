import pytest
from pages.inventory_page import InventoryPage


class TestInventory:
   
    
    def test_titulo_pagina_inventario(self, login_exitoso):
       
        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        
        titulo = inventory_page.obtener_titulo()
        
        assert titulo == "Products", \
            f"Título esperado: 'Products', pero se obtuvo: '{titulo}'"
    
    def test_productos_visibles_en_catalogo(self, login_exitoso):
       
        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        

        cantidad_productos = inventory_page.contar_productos()
        
   
        assert cantidad_productos > 0, \
            "No hay productos visibles en la página de inventario"
        print(f"\n✓ Se encontraron {cantidad_productos} productos en el catálogo")
    
    def test_informacion_primer_producto(self, login_exitoso):
       
        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        
       
        info_producto = inventory_page.obtener_primer_producto_info()
        
      
        assert info_producto is not None, "No se pudo obtener información del primer producto"
        assert "nombre" in info_producto, "El producto debe tener nombre"
        assert "precio" in info_producto, "El producto debe tener precio"
        assert len(info_producto["nombre"]) > 0, "El nombre del producto no puede estar vacío"
        assert len(info_producto["precio"]) > 0, "El precio del producto no puede estar vacío"
        
        print(f"\n✓ Primer producto: {info_producto['nombre']}")
        print(f"✓ Precio: {info_producto['precio']}")
    
    def test_elementos_interfaz_presentes(self, login_exitoso):
      
        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        
        assert inventory_page.verificar_menu_presente(), \
            "El menú hamburguesa no está presente en la página"
        print("\n✓ Menú hamburguesa presente")
        
        assert inventory_page.verificar_filtro_presente(), \
            "El filtro de productos no está presente en la página"
        print("✓ Filtro de productos presente")
    
    def test_cantidad_productos_esperada(self, login_exitoso):
        
        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        
     
        cantidad_productos = inventory_page.contar_productos()

        assert cantidad_productos == 6, \
            f"Se esperaban 6 productos, pero se encontraron {cantidad_productos}"
        print(f"\n✓ Cantidad correcta de productos: {cantidad_productos}")
