import os
import time

os.system('cls')

bus = [["O" for x in range(4)] for y in range(4)]

nombres= []
edades = []
telefonos = []
columnas = []
filas = []
compras = []

precio_pasaje = 24000

print("Bienvenido a TurBus")
print("Por Favor, Elija Una Opción")
while True:
    
    print("\n1. Mostrar Asientos Disponibles\n2. Comprar Asiento\n3. Mostrar Ventas Relizadas\n4. Generar Archivo CSV de las Ventas\n5. Salir ")
    opc = int(input("\nSu opción a realizar es: ")) 


    if opc==1:
        os.system('cls')
        print("MOSTRAR ASIENTOS DISPONIBLES")
        time.sleep(1)

        print("\nFRENTE DEL BUS")
        
        for f in bus:
            print(f)
        time.sleep(5)
        



    elif opc==2:
        os.system('cls')
        print("COMPRA DE ASIENTOS")
        time.sleep(1)
        print(f"**RECUERDE QUE EL PRECIO DE CADA ASIENTO ES DE ${precio_pasaje} Pesos**")
        time.sleep(1)
        nombre = input("Ingrese nombre del Pasajero: ")
        nombres.append(nombre)

        edad = int(input("Ingrese edad del Pasajero: "))
        if edad < 18:
            precio_pasaje = precio_pasaje * 0.8
            print(f"Por ser estudiante, tu pasaje ha quedado en: {int(precio_pasaje)} Gracias a un 20% de Dscto!")
        elif edad > 65:
            precio_pasaje = precio_pasaje * 0.85
            print(f"Por ser Adulto Mayor, tu pasaje ha quedado en: {int(precio_pasaje)} Gracias a un 15% de Dscto!")
        else:
            pass
        edades.append(edad)
        telefono = int(input("Ingrese Número de Teléfono: "))
        telefonos.append(telefono)
        print("Procesando...")
        time.sleep(2)
        print("Datos Ingresados Correctamente!")
        time.sleep(1)
        os.system('cls')
        
        print("FRENTE DEL BUS\n")
        for f in bus:
            print(f)
        columna = int(input("\nIngrese el Número de columna que desee (1,4): ")) -1
        fila = int(input("Ingrese el Número de fila que desee (1,4): ")) -1
        if bus[fila][columna] == "O":
            bus[fila][columna] = "X"
            filas.append(fila)
            columnas.append(columna)
            print(f"Felicidades! Asiento {fila+1},{columna+1} reservado correctamente para {nombre}.")
            print("Gracias Por su compra!")
            compra = [nombre, edad, telefono, fila, columna]
            compras.append(compra)
            time.sleep(3)
            os.system('cls')
        


    elif opc==3:
        os.system('cls')
        print("MUESTRA DE VENTAS REALIZADAS\n")
        time.sleep(1)
        for f in bus:
            print(f)

        for x in (compras):
            print(f"\nCompra del Asiento {columna+1,[4]},{fila+1,[3]} Hecha por:")
            print(f"\nPasaje comprado por: {x,[0]}")
            print(f"Edad: {x,[1]} años")
            print(f"Teléfono: {x,[2]}")
           
        time.sleep(5)

        
        
        



    elif opc==4:
        pass
    
    
    else: 
        os.system('cls')
        print("Gracias Por Preferirnos :)")
        time.sleep(2)
        break