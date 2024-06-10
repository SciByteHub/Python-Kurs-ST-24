#libs
import random
import time

#defining classes
class Cell:
    def __init__(self, alive):
        self.alive = alive
        
    def update_status(self, alive_neighbors):
        if self.alive:
            if alive_neighbors < 2 or alive_neighbors > 3:
                self.alive = False
        else:
            if alive_neighbors == 3:
                self.alive = True

    def __str__(self):
        return "■" if self.alive else " "
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(random.choice([True, False])) for x in range(self.width)] for y in range(self.height)]
        
    def count_alive_neighbors(self, x, y):
        alive_neighbors = 0
        
        for cell_in_x in range(x - 1, x + 2):
            for cell_in_y in range(y - 1, y + 2):
                if (cell_in_x == x and cell_in_y == y) or cell_in_x < 0 or cell_in_y < 0 or cell_in_x >= self.height or cell_in_y >= self.width:
                    continue
                if self.grid[cell_in_x][cell_in_y].alive:
                    alive_neighbors += 1
        return alive_neighbors
    
    def update_board(self):
        new_grid = [[Cell(random.choice([False])) for x in range(self.width)] for y in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                alive_neighbors = self.count_alive_neighbors(x, y)
                cell = self.grid[x][y]
                new_cell = Cell(cell.alive)
                new_cell.update_status(alive_neighbors)
                new_grid[x][y] = new_cell
        self.grid = new_grid 
    
    def display(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def __str__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)

#engine
if __name__ == "__main__":
    print(f"Hello user ! Welcome to the Conway Game Of Life")
    width = int(input(f"Enter width of game board: "))
    height = int(input(f"now enter height of game board: "))
    board = Board(width, height)
    
    print("Initial status of cells: ")
    board.display()
    
    while True:
        # command = input((f"In a moment game of life will begin, if you would like to quit the game press ctrl + c at once. Begin ? (yes/no): "))
        # if command.lower() == "yes":
            # while True:
                
                print(f"\n next generation: ")
                board.update_board()
                board.display()
                time.sleep(5)
        #         update = input(f"Press ENTER if you wish to continue or q to quit the game: ")
        #         if update == 'q':
        #             print("Exiting the game. Goodbye!")
        #             break
        # elif command == 'q' or command == 'no':
        #     print("Exiting the game. Goodbye!")
        #     break
        # else:
        #     print("Invalid input. Please type 'yes' to start or 'q' to quit.")
    
        
        
        
        