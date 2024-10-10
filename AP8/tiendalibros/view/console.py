import sys
from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.excepciones import LibroExistenteError, LibroAgotadoError, ExistenciasInsuficientesError


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print("4. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opcion: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opcian vvlida")

    def adicionar_un_libro_a_catalogo(self):
        try:
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el tiStulo del libro: ")
            precio = float(input("Ingrese el precio del libro (decimal): "))
            existencias = int(input("Ingrese la cantidad de existencias (entero): "))

            libro = self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print(f"El libro '{libro.titulo}' ha sido añadido al catalogo.")
        except LibroExistenteError as e:
            print(f"Ocurrio un error: {e}")
        except ValueError:
            print("Entrada invalida. Asegurese de ingresar valores numericos correctos para el precio y las existencias.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

    def agregar_libro_a_carrito_de_compras(self):
        try:
            isbn = input("Ingrese el ISBN del libro a agregar: ")
            cantidad = int(input("Ingrese la cantidad: "))
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print(f"Se han agregado {cantidad} unidades del libro con ISBN {isbn} al carrito.")
        except LibroAgotadoError as e:
            print(f"Ocurrio un error: {e}")
        except ExistenciasInsuficientesError as e:
            print(f"Ocurrio un error: {e}")
        except ValueError:
            print("Entrada invalida. Asegurese de ingresar un numero entero para la cantidad.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")
        
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("El libro ha sido retirado del carrito con exito.")
        except Exception as e:
            print(f"Ocurrio un error: {e}")