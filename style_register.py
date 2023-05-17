import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

#Function for UI button
def get_button_capture(master, text, command):
    main_font = ctk.CTkFont(family="Helvetica", size=14)
    button_capture = ctk.CTkButton(
                        master,
                        text= text,
                        command=command,
                        font= main_font,
                        text_color="white",
                        hover= True,
                        hover_color= "green",
                        height= 55,
                        width= 132,
                        border_width=2,
                        corner_radius=10,
                        border_color= "black", 
                        bg_color="transparent",
                        fg_color= "#403B3B"
                        )
    return button_capture

    
    
def get_button_register(master, text, command):
    main_font = ctk.CTkFont(family="Helvetica", size=14)
    button_register = ctk.CTkButton(
                            master,
                            text= text,
                            command=command,
                            state='disabled',
                            font= main_font,
                            text_color="white",
                            hover= True,
                            hover_color= "green",
                            height= 55,
                            width= 132,
                            border_width=2,
                            corner_radius=10,
                            border_color= "black", 
                            bg_color="transparent",
                            fg_color= "#403B3B"
                            )
    return button_register
    
def get_button_home(master, text, command):
    main_font = ctk.CTkFont(family="Helvetica", size=14)
    button_register = ctk.CTkButton(
                            master,
                            text= text,
                            command=command,
                            font= main_font,
                            text_color="white",
                            hover= True,
                            hover_color= "green",
                            height= 55,
                            width= 132,
                            border_width=2,
                            corner_radius=10,
                            border_color= "black", 
                            bg_color="transparent",
                            fg_color= "#403B3B"
                            )
    return button_register
    
def get_button_facerecognize(master, text, command):
    main_font = ctk.CTkFont(family="Helvetica", size=14)
    button_facerecognize = ctk.CTkButton(
                            master,
                            text= text,
                            command=command,
                            font= main_font,
                            text_color="white",
                            hover= True,
                            hover_color= "green",
                            height= 55,
                            width= 132,
                            border_width=2,
                            corner_radius=10,
                            border_color= "black", 
                            bg_color="transparent",
                            fg_color= "#403B3B"
                            )
    return button_facerecognize
    
def get_button_aboutus(master, text, command):
    main_font = ctk.CTkFont(family="Helvetica", size=14)
    button_aboutus = ctk.CTkButton(
                            master,
                            text= text,
                            command=command,
                            font= main_font,
                            text_color="white",
                            hover= True,
                            hover_color= "green",
                            height= 55,
                            width= 132,
                            border_width=2,
                            corner_radius=10,
                            border_color= "black", 
                            bg_color="transparent",
                            fg_color= "#403B3B"
                            )
    return button_aboutus

def get_entry_name(master):
    entry_name = ctk.CTkEntry(
                        master,
                        placeholder_text="Enter your name",
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
    
def get_entry_userid(master):
    entry_userid = ctk.CTkEntry(
                        master,
                        placeholder_text="Enter your User ID",
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
    return entry_userid

def get_entry_position(master):
    entry_position = ctk.CTkEntry(
                        master,
                        placeholder_text="Enter your Position",
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
    return entry_position

