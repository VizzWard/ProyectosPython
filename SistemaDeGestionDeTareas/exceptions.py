class EndProgram(Exception):
    def __init__(self):
        self.message = 'Terminando el programa...' # Le añadimos al error un mensaje
        super().__init__(self.message)

class InvalidInputNumber(Exception):
    def __init__(self):
        self.message = 'Ingrese un valor valido' # Le añadimos al error un mensaje
        super().__init__(self.message)

class EndMenu(Exception):
    def __init__(self):
        self.message = 'Volviendo al menu anterior' # Le añadimos al error un mensaje
        super().__init__(self.message)