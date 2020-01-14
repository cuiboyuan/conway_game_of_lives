from tkinter import *
import tkinter.messagebox
from BOX import *
from random import randint
import json
# import Chinese

en = {"Title": "GAME OF LIVES","Subtitle": "A Simulation of Two-Dimensional Lives",
  "Author": "<Created by Boyuan Cui>",
  "Credit": "_Originally created by John Conway in 1960s_",
  "width": "Width of the Board:", "height":  "Height of the Board:",
  "lives": "Number of Lives Generated:", "create": "Generate the Board",
  "breed": "Generate Lives", "size": "Board size: ",
"refresh": "Enter next day", "clear": "Clear Board","invalid title": "Invalid input",
  "invalid content": "All the input should be positive integers",
  "impossible title": "Impossible to generate",
  "impossible content": "Number of lives generated need to be smaller than the capacity of the board",
      "survive": "Number of Lives:"}

cn = {"Title": "康威生命游戏","Subtitle": "二维生命模拟器",
  "Author": "<作者：崔泊远>",
  "Credit": "_由约翰康威于1960年代发明_",
  "width": "世界的宽度:", "height":  "世界的高度:",
  "lives": "生命生成数量:", "create": "生成世界",
  "breed": "生成生命", "size": "世界大小：",
"refresh": "进入下一天", "clear": "清除世界","invalid title": "输入错误",
  "invalid content": "输入值需要是大于零的整数",
  "impossible title": "无法生成",
  "impossible content": "您所要求生成生命的数量大于了这个世界能够承受的数量",
      "survive": "幸存生命数量："}

CHOOSE_EN = False


if CHOOSE_EN:
    # with open("English") as o:
    #     instruction = json.load(o)
    instruction = en
else:
    instruction = cn


root = Tk()
root.title('Game of Lives')

label_title = Label(root, text=instruction['Title'], fg="white", bg="black")
label_sub = Label(root, text=instruction['Subtitle'])
label_credit = Label(root, text=instruction['Credit'])
label_author = Label(root, text=instruction['Author'])

label_width = Label(root, text=instruction['width'])
label_height = Label(root, text=instruction['height'])
label_lives = Label(root, text=instruction['lives'])

width = Entry(root)
height = Entry(root)
lives = Entry(root)


frame = Frame(root, width=200, height=300)


def submit():
    # Checking whether input is valid.
    try:
        width_int = int(width.get())
        height_int = int(height.get())
        lives_int = int(lives.get())
        if width_int <= 0 or height_int <= 0 or lives_int <= 0:
            raise ValueError
        if lives_int > width_int * height_int:
            raise TypeError
    except ValueError:
        tkinter.messagebox.showerror(instruction['invalid title'],
                                     instruction['invalid content'])
    except TypeError:
        tkinter.messagebox.showerror(instruction['impossible title'],
                                     instruction['impossible content'])
        return 'fuck'

    # Create the Board and display it.
    board_canvas = Canvas(frame, width=width_int*10, height=height_int*10,
                          bg='white')
    Game = Board(width_int, height_int)

    # Activate lives and display them
    num = lives_int
    coord_list = []
    lives_generated = 0
    while lives_generated != num:
        x = randint(0, width_int - 1)
        y = randint(0, height_int - 1)
        coord = (x, y)
        if coord not in coord_list:
            Game.locate_box(x, y).activate()
            coord_list.append(coord)

            board_canvas.create_rectangle(x*10,y*10,x*10+9,y*10+9,fill='black')

            lives_generated += 1
    print(Game)

    curr_lives = Label(root, text=instruction['survive'] + lives.get(),
                       fg='white', bg='red')
    curr_lives.grid(row=5, columnspan=3)
    board_size = Label(root, text=instruction['size'] + width.get() + " X "
                                  + height.get(), fg='white', bg='blue')
    board_size.grid(row=4, columnspan=3)

    width.delete(0, 4)
    height.delete(0, 4)
    lives.delete(0, 4)

    def update():
        Game.refresh()
        board_canvas.delete('all')
        count = 0
        for box in Game.lives:
            if box.status:
                x_coord = box.location[0] * 10
                y_coord = box.location[1] * 10
                board_canvas.create_rectangle(x_coord,y_coord,x_coord+9,
                                              y_coord+9,fill='black')
                count += 1
        print(Game)
        curr_lives = Label(root, text=instruction['survive'] + str(count),
                           fg='white', bg='red')
        curr_lives.grid(row=5,  columnspan=3)

    def clear():
        board_canvas.destroy()

    updater = Button(root, text=instruction['refresh'], command=update)
    updater.grid(row=11)
    clear_all = Button(root, text=instruction['clear'], command=clear)
    clear_all.grid(row=11, column=1)

    board_canvas.grid()


initializer = Button(root, text=instruction['create'], command=submit)
label_title.grid(row=0, columnspan=3)
label_sub.grid(row=1, columnspan=3)
label_credit.grid(row=2, columnspan=3)
label_author.grid(row=3, columnspan=3)
Label(root, text='').grid(row=4)
label_width.grid(row=6, sticky=E)
label_height.grid(row=7, sticky=E)
label_lives.grid(row=8, sticky=E)
width.grid(row=6, column=1)
height.grid(row=7, column=1)
lives.grid(row=8, column=1)
initializer.grid(row=9, column=1)
frame.grid(row=10, columnspan=3)

root.mainloop()
