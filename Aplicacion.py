import sqlite3

conexion = sqlite3.connect("Apellidos_almacen.db")
cursor = conexion.cursor()


def registrar_datos():
    idproducto = int(input("Digite el id del producto: "))
    codigo = int(input("Digite el codigo del producto: "))
    nombre = input("Digite el nombre del producto: ")
    precio = int(input("Digite el precio del producto: "))
    datos = (idproducto, codigo, nombre, precio)
    cursor.execute("INSERT INTO producto VALUES (?, ?, ?, ?)", datos)
    conexion.commit()

def listardatos():
    cursor.execute('SELECT * FROM producto')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    conexion.commit()

def eliminarproducto():
    idprod=int(input("Digite el id del producto que desea eliminar: "))
    d=(idprod,)
    cursor.execute("DELETE FROM producto WHERE idproducto=?",d)
    conexion.commit()

def editarproducto():
    idproduc = int(input("Digite el id del producto que desea editar: "))
    cod = int(input("Digite el codigo del producto: "))
    nom = input("Digite el nombre del producto: ")
    pre= int(input("Digite el precio del producto: "))
    dat=(cod,nom,pre,idproduc)
    cursor.execute("UPDATE producto SET codigo=?,nombre = ?, precio = ? WHERE idproducto = ?", dat)
    conexion.commit()

def menu():
    print("* MENU PRINCIPAL *")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

opcion = 1

while opcion != 5:
    menu()
    opcion = int(input("opcion: "))
    if opcion == 1:
        registrar_datos()
    elif opcion == 2:
        eliminarproducto()
    elif opcion == 3:
        editarproducto()
    elif opcion == 4:
        listardatos()
    elif opcion == 5:
        print("#salir()")
    else:
        print("error()")

conexion.close()