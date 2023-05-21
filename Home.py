import customtkinter as ctk
from PIL import Image, ImageTk
import style_register as style
import Face_Recognize
import Register


ctk.set_appearance_mode("dark")

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1024x600")
        self.root.title('Home')

        self.get_image = Image.open("GUI_images/home_background.png")
        self.background_image = ImageTk.PhotoImage(self.get_image)

        self.background_label = ctk.CTkLabel(self.root, image=self.background_image, text="")
        self.background_label.pack()

       

        self.register_button = style.btn_style(self.root, 'Register', self.register)
        self.register_button.place(x=215, y=28)

        self.recognize_button = style.btn_style(self.root, 'Face Recognize', self.recognize)
        self.recognize_button.place(x=368, y=28)

        self.dtr_button = style.btn_style(self.root, 'DTR Download', self.dtr)
        self.dtr_button.place(x=521.2, y=28)

        self.about_button = style.btn_style(self.root, 'About us', self.about)
        self.about_button.place(x=674.4, y=28)


    def dtr(self):
        pass

    def register(self):
        Register.register_window(self.root).mainloop()
        

    def recognize(self):
        Face_Recognize.face_recog_window(self.root).mainloop()
       
    def about(self):
        pass

if __name__ == '__main__':
    app = App()
    app.root.mainloop()
