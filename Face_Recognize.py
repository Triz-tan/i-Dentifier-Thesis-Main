import customtkinter as ctk
import style_register as style
import cv2
from PIL import Image, ImageTk
import os
import tkinter
from tkinter import messagebox
import openpyxl
import Face_Recognize

class face_recog_window(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        
        self.title("Face Recognition")
        self.geometry("1024x600")
        self.attributes('-topmost', True)

        self.get_image = Image.open("GUI_images/face_detect.png")
        self.background_image = ImageTk.PhotoImage(self.get_image)

        self.background_label = ctk.CTkLabel(self, image=self.background_image, text="")
        self.background_label.pack()

        
       







if __name__ == "__main__":
    root = ctk.CTk()
    app = face_recog_window(root)
    app.mainloop()      