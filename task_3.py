import random

class NavalBattle:
    """
    Battleship game class with random ship placement.
    
    Class Attributes:
        playing_field: Game board 10x10 (0-empty, 1-ship).
        _hit_field: Board with hit/miss marks.
    """
    
    playing_field = None
    _hit_field = None
    
    def __init__(self, symbol: str) -> None:
        """
        Initialize a player.
        
        Args:
            symbol: Symbol to mark hits with.
        """
        self.symbol = symbol
    
    @classmethod
    def show(cls) -> None:
        """
        Display the game board to the console.
        ~ - hidden cell (ships are hidden)
        o - miss
        player symbol - hit
        """
        if cls.playing_field is None:
            print("Game board not set")
            return
        
        if cls._hit_field is None:
            cls._hit_field = [['~' for _ in range(10)] for _ in range(10)]
        
        for row in cls._hit_field:
            print(' '.join(row))
    
    def shot(self, x: int, y: int) -> None:
        """
        Make a shot at coordinates (x, y).
        
        Args:
            x: X coordinate (1-10).
            y: Y coordinate (1-10).
        """
        if self.__class__.playing_field is None:
            print("Game board not set")
            return
        
        i = y - 1
        j = x - 1
        
        if i < 0 or i >= 10 or j < 0 or j >= 10:
            print("error")
            return
        
        if self.__class__._hit_field[i][j] != '~':
            print("error")
            return
        
        if self.__class__.playing_field[i][j] == 1:
            print("hit")
            self.__class__._hit_field[i][j] = self.symbol
        else:
            print("miss")
            self.__class__._hit_field[i][j] = 'o'
    
    @classmethod
    def new_game(cls) -> None:
        """
        Create a new game board with randomly placed ships.
        Ships do not touch each other (including diagonals).
        """
        cls.playing_field = [[0 for cell in range(10)] for cell in range(10)]
        cls._hit_field = [['~' for cell in range(10)] for cell in range(10)]
        
        ships = [(4, 1), (3, 2), (2, 3), (1, 4)]
        
        for length, count in ships:
            for cell in range(count):
                placed = False
                while not placed:
                    direction = random.choice([0, 1])
                    
                    if direction == 0:  # Horizontal
                        x = random.randint(0, 9 - length)
                        y = random.randint(0, 9)
                    else:  # Vertical
                        x = random.randint(0, 9)
                        y = random.randint(0, 9 - length)
                    
                    if cls._can_place_ship(x, y, length, direction):
                        cls._place_ship(x, y, length, direction)
                        placed = True
    
    @classmethod
    def _can_place_ship(cls, x: int, y: int, length: int, direction: int) -> bool:
        """
        Check if a ship can be placed at the given position.
        
        Args:
            x: X coordinate (0-9).
            y: Y coordinate (0-9).
            length: Ship length.
            direction: Direction (0-horizontal, 1-vertical).
        
        Returns:
            bool: True if placement is possible, False otherwise.
        """
        start_x = max(0, x - 1)
        start_y = max(0, y - 1)
        
        if direction == 0:  # Horizontal
            end_x = min(9, x + length)
            end_y = min(9, y + 1)
        else:  # Vertical
            end_x = min(9, x + 1)
            end_y = min(9, y + length)
        
        for i in range(start_y, end_y + 1):
            for j in range(start_x, end_x + 1):
                if cls.playing_field[i][j] != 0:
                    return False
        
        for k in range(length):
            if direction == 0:
                if cls.playing_field[y][x + k] != 0:
                    return False
            else:
                if cls.playing_field[y + k][x] != 0:
                    return False
        
        return True
    
    @classmethod
    def _place_ship(cls, x: int, y: int, length: int, direction: int) -> None:
        """
        Place a ship on the game board.
        
        Args:
            x: X coordinate (0-9).
            y: Y coordinate (0-9).
            length: Ship length.
            direction: Direction (0-horizontal, 1-vertical).
        """
        for k in range(length):
            if direction == 0:
                cls.playing_field[y][x + k] = 1
            else:
                cls.playing_field[y + k][x] = 1


player1 = NavalBattle('#')
player1.shot(6, 2)
NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
[1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)
