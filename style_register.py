import customtkinter as ctk
import tkinter as tk

def btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=14)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "green",
                        height= 55,
                        width= 132,
                        border_width=1,
                        corner_radius=10,
                        border_color= "black",
                        bg_color="transparent",
                        fg_color= "#403B3B"
                        )
    return btn

def frame_btn_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=14)
    btn = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "green",
                        height= 55,
                        width= 132,
                        border_width=1,
                        corner_radius=10,
                        border_color= "black",
                        bg_color="#2B2B2B",
                        fg_color= "#403B3B"
                        )
    return btn

def entry_style(master, placeholder_text):
    entry_name = ctk.CTkEntry(
                        master,
                        placeholder_text = placeholder_text,
                        placeholder_text_color="Gray",
                        font=('rockwell', 12),
                        text_color="black",
                        width=278,
                        height=43,
                        border_width=2,
                        border_color= "black",
                        bg_color="#262626",
                        fg_color= "#EEEEEE",
                        corner_radius=10
                        )
    return entry_name

def webcam_style_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label