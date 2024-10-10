from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, mensaje, cantidad_a_comprar, existencias_actuales):
        super().__init__(mensaje)
        self.cantidad_a_comprar = cantidad_a_comprar
        self.existencias_actuales = existencias_actuales

    def __str__(self):
        return (f"El libro con titulo '{self.mensaje}' no tiene suficientes existencias "
                f"para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, "
                f"existencias: {self.existencias_actuales}.")
