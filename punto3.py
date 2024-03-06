start = True
while start:
      listel = [1, 2]
      print("""
                        ++++++++++++++++++++++
                        + registrar producto +
                        ++++++++++++++++++++++
        """)
meun = print("1. registrar nuevo producto \n2. salir")
opcion = int(input("elija una opcion :"))
if opcion == 1:
      nombre = input('Ingrese el nombre: ')
      email = input('Ingrese el correo electrónico: ')
      id
      nombres
      apellidos
      ubicacion
      email
      edad
      ocupacion
    

    telefonos = {
        'movil': '',
        'casa' : '',
        'personal': '',
        'oficina':''


      with open('productos.json', 'w') as archivo:
        json.dump(productos, archivo, indent=4)
        
 cargar_productos():
    try:
        with open('inventario.json', 'r') as archivo:
            productos = json.load(archivo)
    except FileNotFoundError:
        productos = []
    return productos