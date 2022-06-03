from random import randint


class Dado:
    """Uma classe que representa um único dado"""

    def __init__(self, num_lados=6):
        """Supõe que seja um dado de seis lados"""

        self.num_lados = num_lados

    def rolar(self):
        """Devolve um valor aleatório entre 1 e o número de lados"""

        return randint(1, self.num_lados)
