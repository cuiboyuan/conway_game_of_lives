from BOX import Board
from random import randint
import time

HEADER = '##### Game of Lives #####'
SUB_HEADER = '** A Simulation of Two-Dimensional Organisms **'
AUTHOR = '<Created by Boyuan Cui>'
CREDIT = '_Originally designed by John Conway in 1970s._'
INSTRUCTION_SETUP = 'Setting up the {} of the board (integer required):\n'
INSTRUCTION_INIT = 'Initialized a {}X{} board for game of lives.'
GENERATE = 'Choose an amount of lives to generate (integer required):\n'
SUCCEED = '<Exit succeeded>'
try:
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
        x = input('Enter a number of days to simulate.\n')
        days = 1
        while days <= int(x):
            print('Day {}:'.format(str(days)))
            Game.refresh()
            time.sleep(0.5)
            print(Game)
            days += 1
        print(SUCCEED)
        end = input('Enter \'r\' to restart the game, enter others to exit:\n')
    print(SUCCEED)
except:
    print('surprise mtfk')
    time.sleep(10)
