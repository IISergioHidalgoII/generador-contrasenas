import random
import string

# ==================== Generacion basica ====================

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits
    return "".join(random.choices(caracteres, k=longitud))

def mostrar_menu():
    print("\n===== Generador de Contrasenas =====")
    print("1. Generar contrasena")
    print("2. Salir")
    print("====================================")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            try:
                longitud = int(input("Longitud (default 12): ").strip() or "12")
                if longitud < 4:
                    print("La longitud minima es 4.")
                else:
                    print(f"Contrasena: {generar_contrasena(longitud)}")
            except ValueError:
                print("Valor invalido.")
        elif opcion == "2":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
