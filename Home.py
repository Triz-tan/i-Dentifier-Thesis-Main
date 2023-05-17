import customtkinter as ctk
from PIL import Image, ImageTk
import style_home
import Face_Recognize


ctk.set_appearance_mode("dark")

class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1024x600")
        self.root.title('Home')

        self.get_image = Image.open("GUI_images/HOME_GUI.png")
        self.background_image = ImageTk.PhotoImage(self.get_image)

        self.background_label = ctk.CTkLabel(self.root, image=self.background_image, text="")
        self.background_label.pack()

        self.home_button = style_home.get_button_home(self.root, 'Home', self.home)
        self.home_button.place(x=214, y=28)

        self.register_button = style_home.get_button_register(self.root, 'Register', self.register)
        self.register_button.place(x=367, y=28)

        self.recognize_button = style_home.get_button_recognize(self.root, 'Face Recognize', self.recognize)
        self.recognize_button.place(x=520, y=28)

        self.about_button = style_home.get_button_about(self.root, 'About Us', self.about)
        self.about_button.place(x=673, y=28)


    def home(self):
        pass

    def register(self):
        pass
        

    def recognize(self):
        Face_Recognize.Face_Recognition_Window(self.root).mainloop()
       
    def about(self):
        pass

if __name__ == '__main__':
    app = App()
    app.root.mainloop()
