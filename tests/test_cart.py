import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

class TestCart:

    def test_agregar_producto_al_carrito(self, login_exitoso):
      
        driver = login_exitoso
        inventory_page = InventoryPage(driver)

        info_producto = inventory_page.obtener_primer_producto_info()
        contador_inicial = inventory_page.obtener_contador_carrito()

        inventory_page.agregar_primer_producto_al_carrito()

        contador_final = inventory_page.obtener_contador_carrito()

        assert contador_final == contador_inicial + 1, f"Esperaba {contador_inicial + 1}, pero obtuve {contador_final}"
        assert contador_final == 1, f"El contador debería ser 1, pero es {contador_final}"

        print(f"\n✓ Producto agregado: {info_producto['nombre']}")
        print(f"✓ Contador del carrito: {contador_final}")

    def test_producto_aparece_en_carrito(self, login_exitoso):

        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        nombre_producto = inventory_page.obtener_primer_producto_info()["nombre"]
        inventory_page.agregar_primer_producto_al_carrito()
        inventory_page.hacer_click_carrito()

        assert "cart.html" in driver.current_url, "No se navegó correctamente al carrito"

        assert cart_page.verificar_producto_en_carrito(nombre_producto), f"El producto '{nombre_producto}' no aparece en el carrito"

        print(f"\n✓ Producto en carrito: {nombre_producto}")

    def test_cantidad_items_en_carrito(self, login_exitoso):

        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        inventory_page.agregar_primer_producto_al_carrito()
        inventory_page.hacer_click_carrito()

        cantidad_items = cart_page.contar_items_carrito()
        assert cantidad_items == 1, f"Debería haber 1 item en el carrito, pero hay {cantidad_items}"

        print(f"\n✓ Items en carrito: {cantidad_items}")

    def test_informacion_producto_en_carrito(self, login_exitoso):

        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        info_inventario = inventory_page.obtener_primer_producto_info()

        inventory_page.agregar_primer_producto_al_carrito()
        inventory_page.hacer_click_carrito()

        info_carrito = cart_page.obtener_info_primer_item()

        assert info_carrito is not None, "No se encontró información del item en el carrito"
        assert info_carrito["nombre"] == info_inventario["nombre"], f"Nombre distinto. Inventario: '{info_inventario['nombre']}', Carrito: '{info_carrito['nombre']}'"
        assert info_carrito["precio"] == info_inventario["precio"], f"Precio distinto. Inventario: '{info_inventario['precio']}', Carrito: '{info_carrito['precio']}'"
        assert info_carrito["cantidad"] == "1", f"La cantidad debería ser '1', pero es '{info_carrito['cantidad']}'"

        print(f"\n✓ Producto en carrito: {info_carrito['nombre']}")
        print(f"✓ Precio: {info_carrito['precio']}")
        print(f"✓ Cantidad: {info_carrito['cantidad']}")

    def test_titulo_pagina_carrito(self, login_exitoso):

        driver = login_exitoso
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        inventory_page.hacer_click_carrito()
        titulo = cart_page.obtener_titulo()

        assert titulo == "Your Cart", f"Título esperado: 'Your Cart', pero se obtuvo: '{titulo}'"

        print(f"\n✓ Título del carrito: {titulo}")