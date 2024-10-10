from tiendalibros.modelo.libro_error import LibroError


class LibroError(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

class LibroExistenteError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        mensaje = f"El libro con titulo '{titulo}' y ISBN {isbn} ya existe en el catalogo."
        super().__init__(mensaje)

class LibroAgotadoError(LibroError):
    def __init__(self, titulo: str, isbn: str):
        self.titulo = titulo
        self.isbn = isbn
        mensaje = f"El libro con titulo '{titulo}' y isbn {isbn} esta agotado."
        super().__init__(mensaje)

    def __str__(self):
        return f"El libro con titulo '{self.titulo}' y isbn {self.isbn} esta agotado."

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, titulo: str, isbn: str, cantidad_a_comprar: int, existencias: int):
        mensaje = (f"El libro con titulo '{titulo}' y ISBN {isbn} no tiene suficientes existencias "
                   f"para realizar la compra: cantidad a comprar: {cantidad_a_comprar}, existencias: {existencias}.")
        self.cantidad_a_comprar = cantidad_a_comprar
        self.titulo = titulo
        self.isbn = isbn
        self.existencias = existencias
        super().__init__(mensaje)

    def __str__(self):
        return (f"El libro con titulo '{self.titulo}' y ISBN {self.isbn} no tiene suficientes existencias "
                f"para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, "
                f"existencias: {self.existencias}.")