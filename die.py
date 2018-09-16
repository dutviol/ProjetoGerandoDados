from random import randint

class Die():
    """Uma que representa um único dado """
    
    def __init__(self, num_size = 6):
        """Supõe que seja um dado de seis lados"""
        self.num_size = num_size
    
    def roll(self):
        """ Devolve um valor aleatório entre um e o número de lados do dado"""
        return randint(1, self.num_size)