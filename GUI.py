import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    if file_path:
        display_image(file_path)
        # Here you can call your CNN model classification function with file_path

def display_image(file_path):
    image = Image.open(file_path)
    image.thumbnail((400, 400))  # Resize to fit the window nicely
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.photo = photo  # Keep a reference to avoid garbage collection
    status_label.config(text=f"Loaded: {file_path}")

# Set up main window
root = tk.Tk()
root.title("Image Classifier")

# Button to open image dialog
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# Label to display image
image_label = tk.Label(root)
image_label.pack(padx=10, pady=10)

# Status label to show file path or messages
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()