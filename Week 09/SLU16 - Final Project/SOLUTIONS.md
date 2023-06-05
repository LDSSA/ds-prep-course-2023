# Solutions for SLU16 - Final Project

## Solution 1

```python
    def check_if_mine(self, x: int, y: int) -> bool:
        """
        This method checks if there is a mine in (x,y) position.

        :param x: The x position
        :param y: The y position

        :return: True if there is a mine, False otherwise

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.check_if_mine(2, 2)
        True
        """
        return self.mines[x][y] == 1
```

## Solution 2

```python
    def count_mines_around(self, x: int, y: int) -> int:
        """
        This method counts the mines around (x,y) position.

        :param x: The x position
        :param y: The y position

        :return: The number of mines around (x,y) position

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.count_mines_around(1, 1)
        1
        """
        return sum(self.mines[w][h] for w, h in self.get_surrounding_cells(x, y))
```

## Solution 3

```python
    def click_around(self, x: int, y: int):
        """
        This method is responsible for clicking around (x,y) position.

        This method is used for clicking around positions that have no 
        mines around them. This helps speeding up the game.

        :param y: The y position
        :param x: The x position

        :return: None. Should just click on the (x,y) positions.

        :Example:
        >>> game = MinesweeperGame(3, 3)
        >>> game.mines
        [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
        >>> game.revealed
        [
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN],
            [Square.UNKNOWN, Square.UNKNOWN, Square.UNKNOWN]
        ]
        >>> game.click_around(1, 1)
        >>> game.revealed
        [
            [Square.EMPTY, Square.EMPTY, Square.EMPTY],
            [Square.EMPTY, Square.UNKNOWN, Square.ONE],
            [Square.EMPTY, Square.ONE, Square.MINE]
        ]
        
        Note that we only click around the position (1,1) and not itself
        Hint: looking at the 'test_area_revealed' method in tests.py might 
        be helpful. 
        """
        for new_x, new_y in self.get_surrounding_cells(x, y):
            self.click(new_x, new_y)
```
