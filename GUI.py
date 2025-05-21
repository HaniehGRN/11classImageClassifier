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
file_path = ''

#  variables
canvas_width = 730
canvas_height = 700

def btn_clicked():
    global file_path
    print(file_path)
    classes = {0: '206', 1: 'bird', 2: 'carpet', 3: 'cat', 4: 'cellphone', 5: 'dog',
               6: 'fish', 7: 'horse', 8: 'laptop', 9: 'perfume', 10: 'sheep'}
    cnnModel = models.load_model("models/finalModel.keras")
    img = cv.imread(file_path)
    if img is None:
        print("Failed to load image. Check the file path:", file_path)
        return
    n_img = cv.resize(img, (32, 32))
    n_img = img / 255.0
    n_img = n_img.reshape(1, 32, 32, 3)
    predictions = cnnModel.predict(n_img)
    predicted_class = np.argmax(predictions)
    img_label.config(text=predicted_class)

def on_drop(event):
    global file_path
    file_path = event.data.strip('{}')
    # print(file_path)
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        width, height = image.size
        photo = ImageTk.PhotoImage(image)
        img_label.config(image=photo)
        img_label.photo = photo
        generate_btn.place(x=700, y=401, width=180, height=55)

    else:
        tk.messagebox.showerror(title="Type Error!", message="Not a supported image file")

app = TkinterDnD.Tk()
logo = tk.PhotoImage(file="assets/iconbitmap.gif")
app.call('wm', 'iconphoto', app._w, logo)
app.title("Tkinter Designer")
app.geometry("1200x619")
app.configure(bg="#d298ed")

lhs_canvas = tk.Canvas(
    app, bg="#d298ed", height=2000, width=1200,
    bd=0, highlightthickness=0, relief="ridge")
lhs_canvas.place(x=0, y=0)
lhs_canvas.create_rectangle(360, 0, 500 + 1200, 1000 + 619, fill="white", outline="")
img = tk.PhotoImage(file='assets/draganddrop.png')
img_label = tk.Label(app, text="Drop an image file here", width=50, height=10, image=img, bg="white")
img_label.place(x=420.0, y=20.0, width=700.0, height=450.0)
img_label.drop_target_register(DND_FILES)
img_label.dnd_bind('<<Drop>>', on_drop)

title = tk.Label(
    text="Welcome to Image Classifier", bg="#d298ed",
    fg="white",justify="left", font=("Arial-BoldMT", int(20.0)))
title.place(x=20.0, y=90)

info_text = tk.Label(
    text="This app uses a powerful image classifier\n"
         "to detect objects from 11 categories\n"
         "Including animals, gadgets, and vehicles. "
         "\nJust upload an image, and it will identify\n"
         "whether it's a dog, cat, fish, car, laptop, sheep\n"
         ",bird, carpet, horse, perfume, or cellphone.",
    bg="#d298ed", fg="white", justify="left",
    font=("Georgia", int(16.0)))
info_text.place(x=20.0, y=200)

generate_btn_img = tk.PhotoImage(file="assets/classify.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=0, highlightthickness=0,
    command=btn_clicked, relief="flat")

app.resizable(False, False)
app.mainloop()
