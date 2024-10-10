from item_compra import ItemCompra

class CarroCompras:
    def __init__(self):
        self.item = []

    def agregar_item(self, libro, cantidad):
        nuevo_item = ItemCompra(libro, cantidad)

        self.items.append(nuevo_item)

        return nuevo_item
    
    def calcular_total(self):
        total = 0
        for item in self.items:total += item.calcular_subtotal()

        return total
    
    def quitar_item(self, isbn):
        self.items = [item for item in self.items if item.libro.isbn != isbn]
    

    
