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

    @staticmethod
    def show() -> None:
        """
        Display current playing field with hidden ships and hit markers.
        '~' for unknown cells, 'o' for misses, player symbols for hits.
        """
        if NavalBattle.playing_field is None:
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
        Enemy hits and misses are hidden as '~'.
        """
        if NavalBattle.playing_field is None:
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
            print("мимо")
            return

        if target_row < 0 or target_row >= 10 or target_col < 0 or target_col >= 10:
            print("мимо")
            return

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

player1 = NavalBattle('#')
player2 = NavalBattle('*')

NavalBattle.show()
player1.shot(1, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)

player2.show_private()

player1.shot(1, 1)
NavalBattle.show()
