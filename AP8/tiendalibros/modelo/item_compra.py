class ItemCompra:

    def __init__(self, libro,cantidad:int):
        self.libro = libro
        self.cantidad:int = cantidad

    def calcular_subtotal(self, cantidad:int, precio:int):
        self.cantidad:int = cantidad
        self.precio:int = precio

        return self.cantidad * self.libro.precio
    
    pass
