import customtkinter as ctk
import style_face_recog as style_face
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
        self.geometry("1024x600")
        self.title("Face Recognition")
        self.attributes('-topmost', True)

        self.back_btn = style.btn_style(self, 'Back', self.back_func_btn)
        self.back_btn.place(x=855.7, y=23.5)

        #Importing the mode images into a list
        self.folder_mode_path = 'test_images'
        self.mode_path_list = os.listdir(self.folder_mode_path)
        self.img_mode_list = []
        for path in self.mode_path_list:
            self.img_mode_list.append(cv2.imread(os.path.join(self.folder_mode_path, path)))
        
        #print(len(self.img_mode_list))


        self.webcam_label = style.webcam_style_label(self)
        self.webcam_label.place(x=28, y=96, width=600, height=480)

        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'capture' not in self.__dict__:
            self.capture = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.capture.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20, self.process_webcam)


    def back_func_btn(self):
        self.capture.release()
        self.destroy()
        print("Back button just clicked")





