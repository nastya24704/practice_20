import random


class NavalBattle:
    """Naval battle game class with shared playing field for all players."""
    
    playing_field = None

    def __init__(self, symbol: str) -> None:
        """
        Initialize a player with given hit marker.

        Parameters:
            symbol: Character to mark hits made by this player
        """
        self.symbol = symbol
        self.hits = []
        self.shots_made = set()

    @staticmethod
    def show() -> None:
        """
        Display current playing field with hidden ships and hit markers.
        '~' for unknown cells, 'o' for misses, player symbols for hits.
        """
        if NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return
        
        for row_index in range(10):
            current_line = ""
            for col_index in range(10):
                current_cell = NavalBattle.playing_field[row_index][col_index]
                if current_cell == 0 or current_cell == 1:
                    current_line += "~ "
                elif current_cell == "o":
                    current_line += "o "
                else:
                    current_line += f"{current_cell} "
            print(current_line.strip())

    def show_private(self) -> None:
        """
        Show player's private view with only their own hits revealed.
        """
        if NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return
        
        for row_index in range(10):
            current_line = ""
            for col_index in range(10):
                if (row_index, col_index) in self.hits:
                    current_line += f"{NavalBattle.playing_field[row_index][col_index]} "
                else:
                    current_line += "~ "
            print(current_line.strip())

    def shot(self, x: int, y: int) -> None:
        """
        Make a shot at given coordinates.

        Parameters:
            x: Row coordinate (1-10, starting from top-left)
            y: Column coordinate (1-10, starting from top-left)
        """
        target_row = x - 1
        target_col = y - 1

        if NavalBattle.playing_field is None:
            print("игровое поле не заполнено")
            return

        if target_row < 0 or target_row >= 10 or target_col < 0 or target_col >= 10:
            print("мимо")
            return

        shot_key = (target_row, target_col)
        if shot_key in self.shots_made:
            print("ошибка")
            return

        self.shots_made.add(shot_key)
        target_cell = NavalBattle.playing_field[target_row][target_col]

        if target_cell == 1:
            NavalBattle.playing_field[target_row][target_col] = self.symbol
            self.hits.append((target_row, target_col))
            print("попал")
        elif target_cell == 0:
            NavalBattle.playing_field[target_row][target_col] = "o"
            print("мимо")
        else:
            print("мимо")

    @classmethod
    def new_game(cls) -> None:
        """Create new random playing field with ships."""
        field = [[0 for _ in range(10)] for _ in range(10)]
        
        ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        
        for ship_size in ships:
            placed = False
            attempts = 0
            while not placed and attempts < 1000:
                attempts += 1
                horizontal = random.choice([True, False])
                
                if horizontal:
                    row = random.randint(0, 9)
                    col = random.randint(0, 9 - ship_size)
                else:
                    row = random.randint(0, 9 - ship_size)
                    col = random.randint(0, 9)
                
                if cls._can_place_ship(field, row, col, ship_size, horizontal):
                    cls._place_ship(field, row, col, ship_size, horizontal)
                    placed = True
            
            if not placed:
                return cls.new_game()
        
        cls.playing_field = field

    @staticmethod
    def _can_place_ship(field, row, col, size, horizontal) -> bool:
        """Check if ship can be placed at given position."""
        for i in range(size):
            r = row + (i if not horizontal else 0)
            c = col + (i if horizontal else 0)
            
            if field[r][c] != 0:
                return False
            
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 10 and 0 <= nc < 10:
                        if field[nr][nc] != 0:
                            return False
        return True

    @staticmethod
    def _place_ship(field, row, col, size, horizontal) -> None:
        """Place ship on field."""
        for i in range(size):
            r = row + (i if not horizontal else 0)
            c = col + (i if horizontal else 0)
            field[r][c] = 1


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
