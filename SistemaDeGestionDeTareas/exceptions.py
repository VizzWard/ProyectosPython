class EndProgram(Exception):
    """
    Excepción para indicar que el programa debe terminar.

    Esta excepción se utiliza para señalar que el programa debe finalizar
    su ejecución de manera controlada, típicamente cuando el usuario elige
    salir del programa.

    Attributes:
        message (str): Mensaje que indica que el programa está terminando.

    """
    def __init__(self):
        self.message = 'Terminando el programa...' # Le añadimos al error un mensaje
        super().__init__(self.message)

class InvalidInputNumber(Exception):
    """
    Excepción para manejar entradas numéricas inválidas.

    Esta excepción se lanza cuando el usuario proporciona un valor numérico
    que no es válido en el contexto actual, como una opción de menú inexistente.

    Attributes:
        message (str): Mensaje que solicita al usuario ingresar un valor válido.
    """
    def __init__(self):
        self.message = 'Ingrese un valor valido' # Le añadimos al error un mensaje
        super().__init__(self.message)

class EndMenu(Exception):
    """
    Excepción para indicar que se debe salir del menú actual.

    Esta excepción se utiliza para señalar que se debe terminar la ejecución
    del menú actual y volver al menú anterior o a un nivel superior en la
    jerarquía de menús del programa.

    Attributes:
        message (str): Mensaje que indica que se está volviendo al menú anterior.
    """
    def __init__(self):
        self.message = 'Volviendo al menu anterior' # Le añadimos al error un mensaje
        super().__init__(self.message)