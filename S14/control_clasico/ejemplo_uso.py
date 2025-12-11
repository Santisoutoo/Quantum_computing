from juego_moneda_trampa import (
    control_simple,
    copiar_bit,
    correccion_error
)


def ejemplo_control():
    print("\n" + "="*60)
    print("EJEMPLO 1: CONTROL SIMPLE")
    print("="*60 + "\n")

    prog = control_simple()
    print(prog)


def ejemplo_copiar():
    print("\n" + "="*60)
    print("EJEMPLO 2: COPIAR BIT")
    print("="*60 + "\n")

    prog = copiar_bit()
    print(prog)


def ejemplo_correccion():
    print("\n" + "="*60)
    print("EJEMPLO 3: CORRECCIÓN DE ERROR")
    print("="*60 + "\n")

    prog = correccion_error()
    print(prog)


if __name__ == "__main__":
    ejemplo_control()
    ejemplo_copiar()
    ejemplo_correccion()
