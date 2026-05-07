class NavalBattle:
    """
    Battleship game class.
    
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
    
    @staticmethod
    def show() -> None:
        """
        Display the game board to the console.
        ~ - hidden cell (ships are hidden)
        o - miss
        player symbol - hit
        """
        if NavalBattle.playing_field is None:
            print("Game board not set")
            return
        
        if NavalBattle._hit_field is None:
            NavalBattle._hit_field = [['~' for _ in range(10)] for _ in range(10)]
        
        for row in NavalBattle._hit_field:
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
