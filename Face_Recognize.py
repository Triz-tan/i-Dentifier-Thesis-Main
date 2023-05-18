import customtkinter as ctk

class face_recog_window(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1024x600")
        self.title("Face Recognition")
        self.attributes('-topmost', True)

        









if __name__ == "__main__":
    root = ctk.CTk()
    app = face_recog_window(root)
    app.mainloop()      