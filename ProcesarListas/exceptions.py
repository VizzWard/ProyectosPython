class InvalidInputNumber(Exception):
    def __init__(self):
        self.message = 'Ingrese un valor valido' # Le añadimos al error un mensaje
        super().__init__(self.message)