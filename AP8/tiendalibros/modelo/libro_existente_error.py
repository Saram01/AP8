from tiendalibros.modelo.libro_error import LibroError

class LibroError(Exception):

    pass


class LibroExistenteError(LibroError):
    def __init__(self, titulo, isbn):
        super().__init__(f"El libro con titulo '{titulo}' y ISBN {isbn} ya existe en el catalogo.")
        self.titulo = titulo
        self.isbn = isbn
    
    def __str__(self):
        return f"El libro con titulo '{self.titulo}' y ISBN: {self.isbn} ya existe en el catalogo."

    
