class Producto:
    def __init__(self, nombre, codigo, precio):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}, Precio: {self.precio}"


# Lista de instancias de la clase Producto
productos = [
    Producto("Coca-cola", 1, 80),
    Producto("Monster", 2, 120),
    Producto("Fanta", 3, 70),
    Producto("Agua", 4, 60),
    Producto("Nestea", 5, 220)
]