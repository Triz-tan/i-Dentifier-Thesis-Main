import customtkinter as ctk

class Face_Recognition_Window(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1024x600")
        self.title("Face Recognition")
        self.attributes('-topmost', True)

        