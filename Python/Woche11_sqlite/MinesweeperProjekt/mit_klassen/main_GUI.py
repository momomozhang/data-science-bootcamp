import os
import tkinter as tk

from PIL import Image, ImageTk
from world import World

BACKGROUND_COLOR = "white"
SIZE_FIELD = 50


def load_images():
    images_path = os.path.join(os.path.dirname(__file__), "images")
    img_dict = {}

    questionmark_path = os.path.join(images_path, "questionmark.jpg")
    bomb_path = os.path.join(images_path, "bomb.jpg")
    flag_path = os.path.join(images_path, "flag.jpg")

    im = Image.open(questionmark_path)
    img_dict["questionmark"] = ImageTk.PhotoImage(im)

    for i in range(9):
        number_path = os.path.join(images_path, f"{i}.jpg")
        im = Image.open(number_path)
        img_dict[i] = ImageTk.PhotoImage(im)

    im = Image.open(bomb_path)
    img_dict["bomb"] = ImageTk.PhotoImage(im)

    im = Image.open(flag_path)
    img_dict["flag"] = ImageTk.PhotoImage(im)

    return img_dict


def create_image(x, y, image):
    canvas.create_image(x * SIZE_FIELD, y * SIZE_FIELD, anchor="nw", image=image)


def draw_board(game_world):
    for y in range(game_world.height):
        for x in range(game_world.width):
            tile = game_world[y, x]

            if tile.flag:
                create_image(x, y, images["flag"])
            elif not tile.opened:
                create_image(x, y, images["questionmark"])
            else:
                if tile.type == "Number":
                    create_image(x, y, images[tile.value])
                if tile.type == "Bomb":
                    create_image(x, y, images["bomb"])


def reset():
    global WORLD, GAME_OVER
    WORLD = World()
    GAME_OVER = False
    draw_board(WORLD)


def left_click(event):
    global GAME_OVER

    if GAME_OVER:
        return

    x_coor, y_coor = event.x // SIZE_FIELD, event.y // SIZE_FIELD
    WORLD.open_field(y_coor, x_coor)

    if WORLD[y_coor, x_coor].type == "Bomb":
        GAME_OVER = True
        print("Verloren")

    if WORLD.check_victory():
        print("Gewonnen!")

    draw_board(WORLD)


def right_click(event):
    global GAME_OVER

    if GAME_OVER:
        return

    x_coor, y_coor = event.x // SIZE_FIELD, event.y // SIZE_FIELD

    if not WORLD[y_coor, x_coor].opened:
        WORLD.set_flag(y_coor, x_coor)

    draw_board(WORLD)


window = tk.Tk()
window.title("Minesweeper")

WORLD = World()
GAME_OVER = False

canvas = tk.Canvas(
    window, bg=BACKGROUND_COLOR, height=WORLD.height * SIZE_FIELD, width=WORLD.width * SIZE_FIELD
)
canvas.pack()

my_menu = tk.Menu(window)
window.config(menu=my_menu)

my_menu.add_command(label="Neustart", command=reset)
my_menu.add_command(label="Spiel verlassen", command=window.destroy)

images = load_images()

canvas.bind("<Button-1>", left_click)
canvas.bind("<Button-3>", right_click)

draw_board(WORLD)

window.mainloop()
