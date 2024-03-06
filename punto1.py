import tabulate
inicio = True
while inicio:
    listel = [1, 2, 3, 4, 5]
    print("""
                        +++++++++++++++++++++
                        + convertir divisas +
                        +++++++++++++++++++++
        """)
    meun = print("1.pesos a dolares \n2. pesos a euros \n3. euros a  pesos \n4. pesos a yenes \n5. salir")
    opcion = int(input("elija una opcion :"))
    if opcion == 1:
        pass
    elif opcion == 2:
        
        hola = ( int(input("Ingrese la cantidad")) * 3944)
        print(hola)
    elif opcion == 3:
        hola = ( int(input("Ingrese la cantidad")) * 2994)
        print(hola)
    elif opcion == 4:
        hola = (int(input("Ingrese la cantidad")) * 4270)
        print(hola)
    elif opcion == 5:
        break
