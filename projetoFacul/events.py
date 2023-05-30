from PIL import Image, ImageTk
from tkinter import ttk


def bg_fun(frame):
    bg_img = Image.open("./imagens/bg1.jpg")
    bg_img_resized = bg_img.resize((750, 450), Image.LANCZOS)
    frame.bg_img_tk = ImageTk.PhotoImage(bg_img_resized)
    label_bg = ttk.Label(frame, image=frame.bg_img_tk)
    label_bg.pack()


def center(window):
    width = 750
    height = 450

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    center_v = f"{width}x{height}+{x}+{y}"

    return center_v


def center_low(window):
    width = 650
    height = 350

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    center_v = f"{width}x{height}+{x}+{y}"

    return center_v


def bg_fun_low(frame):
    bg_img = Image.open("./imagens/bg1.jpg")
    bg_img_resized = bg_img.resize((650, 390), Image.LANCZOS)
    frame.bg_img_tk = ImageTk.PhotoImage(bg_img_resized)
    label_bg = ttk.Label(frame, image=frame.bg_img_tk)
    label_bg.pack()
