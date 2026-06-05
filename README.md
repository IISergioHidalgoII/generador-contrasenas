# Generador de Contrasenas

Aplicacion de consola para generar contrasenas seguras con criterios configurables: longitud, mayusculas, numeros y simbolos.

## Como ejecutar

```bash
python generador.py
```

## Funciones

| Funcion | Que hace |
|---|---|
| `generar_contrasena(longitud, mayusculas, numeros, simbolos)` | Genera una contrasena aleatoria garantizando al menos un caracter de cada tipo activado |
| `pedir_si_no(mensaje, default)` | Solicita una respuesta S/N con valor por defecto |
| `mostrar_menu()` | Imprime el menu principal |
| `main()` | Controla el flujo en un bucle |

## Criterios configurables

| Criterio | Default | Descripcion |
|---|---|---|
| Longitud | 12 | Minimo 4 caracteres |
| Mayusculas | Si | Incluye A-Z |
| Numeros | Si | Incluye 0-9 |
| Simbolos | No | Incluye `!@#$%&*?` |

## Diagrama de flujo

```
Inicio
  |
  V
mostrar_menu()
  |
  V
Opcion?
  |- "1" -> input longitud
  |              |
  |              V
  |         pedir_si_no() x3 (mayusculas, numeros, simbolos)
  |              |
  |              V
  |         generar_contrasena() -> mostrar resultado -> menu
  |
  |- "2" -> Salir
  |
  `- otra -> "Opcion no valida" -> menu
```

## Logica de generacion

1. Se construye el conjunto de caracteres segun los criterios activados.
2. Se garantiza al menos un caracter de cada tipo activado (lista `obligatorios`).
3. El resto se rellena aleatoriamente hasta completar la longitud.
4. Se mezcla el resultado con `random.shuffle` para evitar patrones predecibles.

## Tecnologias

- Python 3
- Modulo `random` (estandar)
- Modulo `string` (estandar)
