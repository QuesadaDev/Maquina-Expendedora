tipos_moneda = [5, 10, 50, 100, 200]
dinero_intro = [5, 10, 10, 50, 100]
num_prod = 4
cambio_arr = []

productos = [("Coca-cola", 1, 80),
             ("Monster", 2, 120),
             ("Fanta", 3, 70),
             ("Agua", 4, 60),
             ("Nestea", 5, 220)
             ]


def expende(din_int, num_pro):

    suma = sum(din_int)
    print(f"Se han introducido: {suma} monedas {din_int}")

    for element in productos:
        if num_pro == element[1] and suma >= element[2]:
            cambio = suma - element[2]
            cambio_arr = cambio_moneda(cambio)
            return print(f"El producto elegido es: {element[0]}, con un precio de: {element[2]}"
                         f" se devuelven: {cambio_arr} monedas")

    if num_pro is not element[1] or suma < element[2]:
        return print("Producto no encontrado o dinero insuficiente, se han devuelto: ", suma, "monedas", din_int)


def cambio_moneda(restante):
    cambio_total = []
    for ele in reversed(tipos_moneda):
        while restante % ele >= ele or restante >= ele:
            cambio_total.append(ele)
            restante = restante - ele
        if restante == 0:
            break
    return cambio_total


expende(dinero_intro, num_prod)
