def actualizar(productos, id, nombre, precio, inventario):
    productos[id] = [nombre, precio, inventario]

def borrar(productos, id):
    del productos[id]

def agregar(productos, id, nombre, precio, inventario):
    productos[id] = [nombre, precio, inventario]

def promedio(productos):
    promedio = 0.0
    cant = 0

    for clave in productos:
        promedio += productos[clave][1]
        cant += 1
    
    promedio /= cant

    return promedio

def vInventario(productos):
    vInventario = 0.0

    for clave in productos:
        vInventario += (productos[clave][1] * productos[clave][2])

    return vInventario

def precioMayor(productos):
    precio = ""
    aux = list()
    condicion = 0

    for clave in productos:
        aux.append(productos[clave][1])

        if(productos[clave][1] is max(aux)):
            condicion = clave

    precio = productos[condicion][0]
    return precio

def precioMenor(productos):
    precio = ""
    aux = list()
    condicion = 0

    for clave in productos:
        aux.append(productos[clave][1])

        if(productos[clave][1] is min(aux)):
            condicion = clave

    precio = productos[condicion][0]
    return precio

if __name__=='__main__':
    opcion = input()
    aux = input()

    entrada = aux.split(' ')
    id = int(entrada[0])
    nombre = str(entrada[1])
    precio = float(entrada[2])
    inventario = int(entrada[3])

    productos = {1:["Manzanas", 6000.0, 25],
                2:["Limones", 2500.0, 15],
                3:["Peras", 2700.0, 33],
                4:["Arandanos", 9300.0, 34],
                5:["Tomates", 2100.0, 42],
                6:["Fresas", 4100.0, 10],
                7:["Helado", 4500.0, 41],
                8:["Galletas", 500.0, 8],
                9:["Chocolates", 4500.0, 80],
                10:["Jamon", 15000.0, 10]}

    existencia = False
    imprimir = False

    for clave in productos:
        if(clave == id):
            existencia = True

    if(opcion == "AGREGAR"):
        if(existencia == True):
            print("ERROR")
        else:
            agregar(productos, id, nombre, precio, inventario)
            imprimir = True

    elif(opcion == "BORRAR"):
        if(existencia != True):
            print("ERROR")
        else:    
            borrar(productos, id)
            imprimir = True
            
    elif(opcion == "ACTUALIZAR"):
        if(existencia != True):
            print("ERROR")
        else: 
            actualizar(productos, id, nombre, precio, inventario)
            imprimir = True

    else:
        print("ERROR")

    if (imprimir == True):
        promedio = "{:.1f}".format(promedio(productos))
        inventario = "{:.1f}".format(vInventario(productos))

        print(precioMayor(productos),precioMenor(productos),promedio,inventario)