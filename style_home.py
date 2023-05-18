import customtkinter as ctk


def get_button_home(master, text, command):
    main_font = ctk.CTkFont(family="Poppins", size=15)
    button_home = ctk.CTkButton(
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
    return button_home
