from __future__ import annotations
from typing import List
from random import randint


class Box:

    status: bool
    location: List[int]
    neighbors: List[Box]

    def __init__(self, coord_x: int, coord_y: int) -> None:

        self.status = False
        self.location = [coord_x, coord_y]
        self.neighbors = []

    def __eq__(self, other: Box) -> bool:

        same_x = self.location[0] == other.location[0]
        same_y = self.location[1] == other.location[1]

        if same_x and same_y:
            return True
        else:
            return False

    def __str__(self) -> str:

        if self.status:
            return 'O'
        else:
            return ' '

    def activate(self) -> None:

        self.status = True

    def find_neighbor(self, other: Box) -> None:

        condition1 = abs(other.location[0] - self.location[0]) <= 1
        condition2 = abs(other.location[1] - self.location[1]) <= 1

        if condition1 and condition2:
            if other not in self.neighbors:
                if other != self:
                    self.neighbors.append(other)

    def update(self) -> None:

        live = 0
        for b in self.neighbors:
            if b.status:
                live += 1
        if live == 3:
            self.status = True
        elif live == 2:
            pass
        else:
            self.status = False


class Board:

    base: int
    height: int
    lives: List[Box]

    def __init__(self, base: int, height: int) -> None:

        self.base = base
        self.height = height
        self.lives = []
        for i in range(height):
            for j in range(base):
                self.lives.append(Box(j, i))
        for box in self.lives:
            for other in self.lives:
                box.find_neighbor(other)

    def __str__(self) -> str:

        result = ' '+'#'*(self.base) + ' \n'
        for i in range(self.height):
            result += '|'
            for j in range(self.base):
                result += str(self.lives[j + i * self.base])
            result += '|\n'
        result += (' '+'#'*(self.base) + ' ')
        return result

    def refresh(self) -> None:

        for b in self.lives:
            b.update()

    def locate_box(self, coord_x: int, coord_y: int) -> Box:

        return self.lives[coord_y * self.base + coord_x]

    def count_lives(self) -> int:

        result = 0
        for box in self.lives:
            if box.status:
                result += 1
        return result


'''
Advanced stable organism found
20X10 Board:
 #################### 
|               OOO O|
|       O    O O   O |
|     O O O OOO  O   |
|  OO O O    OOO O   |
|O                O  |
|O         OOO       |
| O O   O OOO   O O O|
| O       O     O  O |
|            O O     |
|      O OO O   O   O|
 #################### 
after 119 days:
 #################### 
|                  OO|
|                O  O|
|          O     OO  |
|         O O O      |
|        O OO OOOOO  |
|        O   O    O  |
|         OO O OOO   |
|          O  O      |
|          O   O     |
|           OOOO     |
 #################### 
 
 ########## 
|          |
|          |
|    OO OO |
|    OO O  |
| O       O|
|O O     OO|
| O       O|
|    OO O  |
|    OO OO |
|          |
 ########## 
 
 ########## 
|        OO|
|         O|
|   OO  O O|
|   O  O OO|
|    O O   |
|   OO O OO|
|  O   O O |
| O OOOO O |
|  O    O  |
|   OOOO   |
 ########## 
 
 ############ 
|   OO OOOOOO|
|  O O O    O|
| O    O OO O|
|O OOOOO  O O|
|O O    O O O|
|O O  O O O O|
|O O O O  O O|
|O O O O OO O|
|O O O  O   O|
|O O OO O   O|
| O     O O O|
|  OOOOOO OO |
 ############ 
'''
if __name__ == '__main__':
    HEADER = '##### Game of Lives #####'
    SUB_HEADER = '** A Simulation of Two-Dimensional Organisms **'
    AUTHOR = '<Created by Boyuan Cui>'
    CREDIT = '_Originally designed by John Conway in 1970s._'
    INSTRUCTION_SETUP = 'Setting up the {} of the board (integer required):\n'
    INSTRUCTION_INIT = 'Initialized a {}X{} board for game of lives.'
    GENERATE = 'Choose an amount of lives to generate (integer required):\n'
    SUCCEED = '<Exit succeeded>'

    end = 'r'
    while end.lower() == 'r':
        print(HEADER, SUB_HEADER, AUTHOR, CREDIT + '\n', sep='\n')
        width = int(
            input(INSTRUCTION_SETUP.format('width')))
        height = int(
            input(INSTRUCTION_SETUP.format('height')))
        Game = Board(width, height)

        print(INSTRUCTION_INIT.format(width, height))
        num = int(input(GENERATE))
        coord_list = []
        lives_generated = 0
        while lives_generated != num:
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            coord = (x, y)
            if coord not in coord_list:
                Game.locate_box(x,y).activate()
                coord_list.append(coord)
                lives_generated += 1

        print('Start with:')
        print(Game)
        x = input('Enter any key to start.\n')
        i = 1
        command = ''
        while command.lower() != 'x':
            print('Day {}:'.format(str(i)))
            Game.refresh()
            print(Game)
            command = input('Enter \'x\' to exit, enter others to continue:\n')
            i += 1
        print(SUCCEED)
        end = input('Enter \'r\' to restart the game, enter others to exit:\n')
    print(SUCCEED)

    # Game = Board(38, 20)
    # Game.locate_box(1,6).activate()
    # Game.locate_box(1,5).activate()
    # Game.locate_box(2,5).activate()
    # Game.locate_box(2,6).activate()
    # Game.locate_box(36,3).activate()
    # Game.locate_box(36,4).activate()
    # Game.locate_box(35,3).activate()
    # Game.locate_box(35,4).activate()
    # Game.locate_box(11,5).activate()
    # Game.locate_box(11,6).activate()
    # Game.locate_box(11,7).activate()
    # Game.locate_box(12,4).activate()
    # Game.locate_box(12,8).activate()
    # Game.locate_box(13,3).activate()
    # Game.locate_box(13,9).activate()
    # Game.locate_box(14,3).activate()
    # Game.locate_box(14,9).activate()
