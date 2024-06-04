class Cell:
    def __init__(self, alive, dead):
        self.alive = alive
        self.dead = dead

    def __str__(self):
        return "*" if self.alive else "."

