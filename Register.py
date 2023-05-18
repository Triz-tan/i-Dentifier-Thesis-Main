import customtkinter as ctk
import style_register as style
import cv2
from PIL import Image, ImageTk
from Home import App
class register_window(ctk.CTkToplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1024x600")
        self.title("Register")
        self.attributes('-topmost', True)

        self.register_label_heading = ctk.CTkLabel(self, text="Register", font=('Poppins', 24), text_color="white")
        self.register_label_heading.place(x=28, y=32)

        self.home_btn = style.btn_style(self, 'Home', self.home_func_btn)
        self.home_btn.place(x=555, y=23)

        self.face_btn = style.btn_style(self, 'Face Recognize', self.face_func_btn)
        self.face_btn.place(x=708, y=23)

        self.about_btn = style.btn_style(self, 'About us', self.about_func_btn)
        self.about_btn.place(x=861, y=23)

        self.frame = ctk.CTkFrame(self, width=306, height=480, corner_radius=15)
        self.frame.place(x=690, y=98)

        self.employee_pro_label = ctk.CTkLabel(self, text="Employee Profile", font=('Poppins', 24), text_color="white", bg_color="#2B2B2B")
        self.employee_pro_label.place(x=755, y=108)

        self.name_label = ctk.CTkLabel(self, text="Name", font=('Poppins', 12), text_color="white", bg_color="#2B2B2B")
        self.name_label.place(x=705, y=163)

        self.user_label = ctk.CTkLabel(self, text="User ID", font=('Poppins', 12), text_color="white", bg_color="#2B2B2B")
        self.user_label.place(x=705, y=242)

        self.position_label = ctk.CTkLabel(self, text="Position", font=('Poppins', 12), text_color="white", bg_color="#2B2B2B")
        self.position_label.place(x=705, y=321)

        self.status_label = ctk.CTkLabel(self, text="Status", font=('Poppins', 12), text_color="white", bg_color="#2B2B2B")
        self.status_label.place(x=705, y=400)

        self.name_entry = style.entry_style(self, "Enter your name")
        self.name_entry.place(x=705, y=185.5)

        self.user_entry = style.entry_style(self, "Enter your user id")
        self.user_entry.place(x=705, y=264.4)

        self.position_entry = style.entry_style(self, "Enter your position")
        self.position_entry.place(x=705, y=343.3)

        self.status_entry = style.entry_style(self, "Enter your status")
        self.status_entry.place(x=705, y=422.2)

        self.capture_btn = style.capture_btn_style(self, "Capture", self.capture_func_btn,)
        self.capture_btn.place(x=772.3, y=501.3)


        self.webcam_label = style.webcam_style_label(self)
        self.webcam_label.place(x=28, y=96, width=640, height=480)

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
      
    




    def home_func_btn(self):
        self.capture.release()
        self.destroy()
        App
    
        print("Home button just clicked")

    def face_func_btn(self):
        print("Face Recognize button just clicked")

    def about_func_btn(self):
        print("About us button just clicked")

    def capture_func_btn(self):
        print("Capture function button just clicked")


if __name__ == "__main__":
    root = ctk.CTk()
    app = register_window(root)
    app.mainloop()