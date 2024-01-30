from producto import productos


def mostrar_productos():
    for product in productos:
        print(product)


def introduce_monedas():

    int_monedas = input("\nIntroduce las monedas separadas por comas: ")
    monedas_introducidas = [int(moneda) for moneda in int_monedas.split(',')]

    int_prod = input("Selecciona el número del producto: ")
    producto_selecionado = int(int_prod)

    return monedas_introducidas, producto_selecionado


def expendedora(din_int, num_pro):

    suma = sum(din_int)
    print(f"\nSe han introducido: {suma} monedas {sorted(din_int)}")

    for element in productos:
        if num_pro == element.codigo and suma >= element.precio:
            cambio = suma - element.precio
            cambio_arr = cambio_moneda(cambio)
            return print(f"El producto elegido es: {element.nombre}, con un precio de: {element.precio}"
                         f" se devuelven: {cambio_arr} monedas")

    return print("Producto no encontrado o dinero insuficiente, se han devuelto: ", suma, "monedas", din_int)


def cambio_moneda(restante):
    cambio_total = []
    tipos_moneda = [5, 10, 50, 100, 200]

    for ele in reversed(tipos_moneda):
        while restante % ele >= ele or restante >= ele:
            cambio_total.append(ele)
            restante = restante - ele
        if restante == 0:
            break
    return cambio_total


mostrar_productos()
monedas, producto = introduce_monedas()
expendedora(monedas, producto)
