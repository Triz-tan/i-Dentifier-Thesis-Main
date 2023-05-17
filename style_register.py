import customtkinter as ctk

def home_style(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=14)
    home_button_style = ctk.CTkButton(
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
    return home_button_style