import random
import string

# ==================== Generacion con criterios ====================

def generar_contrasena(longitud=12, mayusculas=True, numeros=True, simbolos=False):
    caracteres = string.ascii_lowercase
    obligatorios = []

    if mayusculas:
        caracteres += string.ascii_uppercase
        obligatorios.append(random.choice(string.ascii_uppercase))
    if numeros:
        caracteres += string.digits
        obligatorios.append(random.choice(string.digits))
    if simbolos:
        especiales = "!@#$%&*?"
        caracteres += especiales
        obligatorios.append(random.choice(especiales))

    relleno = random.choices(caracteres, k=longitud - len(obligatorios))
    resultado = obligatorios + relleno
    random.shuffle(resultado)
    return "".join(resultado)

def pedir_si_no(mensaje, default=True):
    valor = input(f"{mensaje} ({'S/n' if default else 's/N'}): ").strip().lower()
    if valor == "":
        return default
    return valor in ("s", "si", "y", "yes")

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
                    mayusculas = pedir_si_no("Incluir mayusculas?", default=True)
                    numeros    = pedir_si_no("Incluir numeros?",    default=True)
                    simbolos   = pedir_si_no("Incluir simbolos (!@#$%&*?)?", default=False)
                    print(f"Contrasena: {generar_contrasena(longitud, mayusculas, numeros, simbolos)}")
            except ValueError:
                print("Valor invalido.")
        elif opcion == "2":
            print("Bye!")
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    main()
