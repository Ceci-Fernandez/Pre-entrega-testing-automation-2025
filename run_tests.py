import pytest
import sys


def main():
   
    test_files = [
        "tests/test_login.py",
        "tests/test_inventory.py",
        "tests/test_cart.py"
    ]
    

    pytest_args = test_files + [
        "-v",                           
        "--html=reporte.html",          
        "--self-contained-html",        
        "-s",                           
        "--tb=short",                   
    ]
    
    print("=" * 70)
    print("EJECUTANDO TESTS DE AUTOMATIZACIÓN - SAUCEDEMO.COM")
    print("=" * 70)
    print("\nTests a ejecutar:")
    for test_file in test_files:
        print(f"  • {test_file}")
    print("\n" + "=" * 70 + "\n")
    
    # Ejecutar pytest con los argumentos especificados
    exit_code = pytest.main(pytest_args)
    
    print("\n" + "=" * 70)
    if exit_code == 0:
        print("✓ TODOS LOS TESTS PASARON EXITOSAMENTE")
    else:
        print("✗ ALGUNOS TESTS FALLARON")
    print("=" * 70)
    print("\nReporte HTML generado: reporte.html")
    print("=" * 70 + "\n")
    
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
