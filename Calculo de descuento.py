def calcular_descuento(monto_total, porcentaje_descuento=35):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    while True:
        try:
            monto_total = float(input("Ingrese el monto total de la compra (o 0 para salir): "))
            if monto_total == 0:
                print("Gracias por usar el programa. ¡Hasta luego!")
                break


            descuento1 = calcular_descuento(monto_total)
            monto_final1 = monto_total - descuento1

            print(f"\nResultados con descuento predeterminado (35%):")
            print(f"Monto total de la compra: ${monto_total:.2f}")
            print(f"Descuento aplicado: ${descuento1:.2f}")
            print(f"Monto final a pagar: ${monto_final1:.2f}")

            porcentaje = float(input("\nIngrese el porcentaje del descuento: "))
            descuento2 = calcular_descuento(monto_total, porcentaje)
            monto_final2 = monto_total - descuento2

            print(f"\nResultados con descuento personalizado ({porcentaje}%):")
            print(f"Monto total de la compra: ${monto_total:.2f}")
            print(f"Descuento aplicado: ${descuento2:.2f}")
            print(f"Monto final a pagar: ${monto_final2:.2f}")

            print("\n" + "-" * 50 + "\n")

        except ValueError:
            print("Error: Por favor, ingresar un valor válido.")

if __name__ == "__main__":
    print("Calculadora de descuentos")
    main()
