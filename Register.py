import customtkinter as ctk
import style_register as style

class register_window(ctk.CTkToplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1024x600")
        self.title("Register")
        self.attributes('-topmost', True)

        self.register_label_heading = ctk.CTkLabel(self, text="Register", font=('Poppins', 24), text_color="white")
        self.register_label_heading.place(x=28, y=32)

        self.frame = ctk.CTkFrame(self, width=306, height=450, corner_radius=15)
        self.frame.place(x=690, y=98)

        self.home_button = style.home_style(self, 'Home', self.home_function_button)
        self.home_button.place(x=555, y=23)

    def home_function_button(self):
        print("Home button just clicked")




if __name__ == "__main__":
    root = ctk.CTkTk()
    app = register_window(root)
    app.mainloop()