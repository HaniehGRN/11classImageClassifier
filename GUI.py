import sys
import os
import tkinter as tk
import tkinter.messagebox as tk1
import tkinter.filedialog as filedialog
from pathlib import Path
from PIL import Image, ImageTk, ImageDraw
from tkinterdnd2 import DND_FILES, TkinterDnD
import numpy as np
import cv2 as cv
from keras import models
from namex import export
import sys

from tamrin1 import Predictor

#  global variables
file_path = ''
canvas_width = 730
canvas_height = 700

def btn_clicked():
    global file_path
    predictor = Predictor()
    predicted_class = predictor.predict(file_path)
    info_text.config(text="predicted class is :")
    class_text = tk.Label(
    text=f'{predicted_class}',
    bg="#d298ed", fg="white", justify="left",
    font=("Georgia", 40))
    class_text.place(x=50.0, y=250)

def on_drop(event):
    global file_path
    file_path = event.data.strip('{}')
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)
        img_label.config(image=photo)
        img_label.photo = photo
        generate_btn.place(x=690, y=480, width=180, height=55)

    else:
        tk.messagebox.showerror(title="Type Error!", message="Not a supported image file")

app = TkinterDnD.Tk()
logo = tk.PhotoImage(file="assets/iconbitmap.gif")
app.call('wm', 'iconphoto', app._w, logo)
app.title("Tkinter Designer")
app.geometry("1000x619")
app.configure(bg="#d298ed")

lhs_canvas = tk.Canvas(
    app, bg="#800080", height=2000, width=1200,
    bd=0, highlightthickness=0, relief="ridge")
lhs_canvas.place(x=0, y=0)
lhs_canvas.create_rectangle(360, 0, 500 + 1200, 1000 + 619, fill="white", outline="")
img = tk.PhotoImage(file='assets/draganddrop.png')
img_label = tk.Label(app, text="Drop an image file here", width=50, height=10, image=img, bg="white")
img_label.place(x=420.0, y=20.0, width=700.0, height=450.0)
img_label.drop_target_register(DND_FILES)
img_label.dnd_bind('<<Drop>>', on_drop)

title = tk.Label(
    text="Welcome to\nImage Classifier", bg="#800080",
    fg="white",justify="center", font=("Georgia", 30))
title.place(x=65.0, y=55)
lhs_canvas.create_rectangle(40.0, 150, 300.0, 150, fill="white", width=7, outline="")
info_text = tk.Label(
    text="This app uses a powerful\nimage classifier"
         "to detect \nobjects from 11 categories.\n"
         "\nJust upload an image,\nand it will identify\n"
         "whether it's a dog, \ncat, fish, car, laptop,\nsheep,"
         "bird, carpet,\nhorse, perfume, or\ncellphone.",
    bg="#800080", fg="white", justify="left",
    font=("Georgia", 21))
info_text.place(x=38.0, y=190)

generate_btn_img = tk.PhotoImage(file="assets/classify.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=0, highlightthickness=0,
    command=btn_clicked, relief="flat")

app.resizable(False, False)
app.mainloop()
