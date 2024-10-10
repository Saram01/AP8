from carro_compra import CarroCompras
from libro import Libro
from excepciones import LibroExistenteError, LibroAgotadoError, ExistenciasInsuficientesError



class Libro:
    def __init__(self, isbn: str, titulo: str, precio: float, existencias: int):
        self.isbn = isbn
        self.titulo = titulo
        self.precio = precio
        self.existencias = existencias

    def __str__(self):
        return f"Libro: {self.titulo}, ISBN: {self.isbn}, Precio: {self.precio}, Existencias: {self.existencias}"

    def __repr__(self):
        return self.__str__()

class TiendaLibros:
    
    def __init__(self):
        self.catalogo = {}
        self.carrito = CarroCompras()
        
    def adicionar_libro_a_catalogo(self, isbn: str, titulo: str, precio: float, existencias: int) -> Libro:
        
        if isbn in self.catalogo:
            raise LibroExistenteError(titulo, isbn)
        
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        
        self.catalogo[isbn] = nuevo_libro
        
        print(f"El libro '{titulo}' ha sido añadido al catalogo.")
        return nuevo_libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        if isbn not in self.catalogo:
            print(f"El libro con ISBN {isbn} no existe en el catalogo.")
            return
        
        libro = self.catalogo[isbn]

        if libro.existencias == 0:
            raise LibroAgotadoError(f"El libro con titulo '{libro.titulo}' y ISBN {isbn} esta agotado.")
        
        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(f"El libro con titulo '{libro.titulo}' y ISBN {isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {cantidad}, existencias: {libro.existencias}")

        self.carrito.agregar_item(libro, cantidad)
        print(f"Se agrego {cantidad} unidades del libro '{libro.titulo}' al carrito.")

    def retirar_item_de_carrito(self, isbn):
        
        item_a_eliminar = next((item for item in self.carrito.items if item.libro.isbn == isbn), None)

        if item_a_eliminar:
            self.carrito.quitar_item(isbn)
            print(f"El libro con ISBN {isbn} ha sido retirado del carrito.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en el carrito.")
    
