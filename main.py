from BOX import Board
from BOX import Box
from random import randint
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # lives_data = []
    # init_data = []
    TRIALS = 50
    life_size = [50, 100, 150, 200, 250, 300, 350]
    WIDTH = 20
    HEIGHT = 20
    TRIAL_DAYS = 500
    # for _ in range(TRIALS):
    #     for size in life_size:
    #         game = Board(WIDTH, HEIGHT)
    #         num = size
    #         coord_list = []
    #         lives_generated = 0
    #         while lives_generated != num:
    #             x = randint(0, WIDTH - 1)
    #             y = randint(0, HEIGHT - 1)
    #             coord = (x, y)
    #             if coord not in coord_list:
    #                 game.locate_box(x, y).activate()
    #                 coord_list.append(coord)
    #                 lives_generated += 1
    #         for _ in range(TRIAL_DAYS):
    #             game.refresh()
    #         lives_data.append(game.count_lives())
    #         init_data.append(size)
    # plt.plot(init_data, lives_data, 'ro')
    # plt.show()
    num = [100, 150, 200, 250, 300, 350]
    boxes_data = []
    days_data = []
    for n in num:
        box_data = []
        day_data = []
        game = Board(WIDTH, HEIGHT)
        coord_list = []
        lives_generated = 0
        date = 0
        while lives_generated != n:
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            coord = (x, y)
            if coord not in coord_list:
                game.locate_box(x, y).activate()
                coord_list.append(coord)
                lives_generated += 1
        for _ in range(TRIAL_DAYS):
            box_data.append(game.count_lives())
            day_data.append(date)
            game.refresh()
            date += 1
        boxes_data.append(box_data)
        days_data.append(day_data)
    plt.plot(days_data[0], boxes_data[0],'b-', days_data[1], boxes_data[1], 'r-',\
             days_data[2], boxes_data[2], 'g-', days_data[3], boxes_data[3], 'y-')
    plt.show()
