import random

class randoms:
    """ get random number range """
    def randint(start:int, stop:int) -> int:
        """ return a random number from start-end number. """
        return random.randint(start, stop)
    
    def choice(seq: list) -> int:
        """ return a choices from an sequence. """
        return random.choice(seq)
    
    def choices(seq:list, set:int) -> list:
        """ return k set of choices from the sequence. """
        return random.choices(seq, k=set)