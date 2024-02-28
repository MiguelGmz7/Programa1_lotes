
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from timer import Timer
# from tkinter import *
# Explicit imports to satisfy Flake8


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/run/media/miguel/Data/User/Courses/Sem_SO/fkinTkinter/programa_1/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MyGUI: # Generamos todo el canvas como una clase
    def __init__(self):
        self.window = Tk()
        self.window.geometry("762x665")
        self.window.configure(bg = "#FFFFFF")
        
        self.timer = Timer()


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 665,
            width = 762,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            381.0,
            50.0,
            image=image_image_1
        )

        
        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            122.0,
            148.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            122.0,
            257.0,
            image=image_image_3
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            278.5,
            192.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D5D5D5",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=196.0,
            y=174.0,
            width=165.0,
            height=35.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.start_timer,
            relief="flat"
        )
        self.button_1.place(
            x=391.0,
            y=172.0,
            width=207.0,
            height=40.0
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=540.0,
            y=596.0,
            width=207.0,
            height=40.0
        )

        # Recuadro de espera

        self.canvas.create_rectangle(
            24.0,
            284.0,
            219.0,
            584.0,
            fill="#EEE8B7",
            outline="")

        self.canvas.create_text(
            24.0,
            284.0,
            anchor="nw",
            text="espera_test",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            391.0,
            327.0,
            image=image_image_4
        )

        image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            105.0,
            606.0,
            image=image_image_5
        )

        # Recuadro de ejecucion

        self.canvas.create_rectangle(
            284.0,
            357.0,
            479.0,
            523.0,
            fill="#EEE8B7",
            outline="")

        self.canvas.create_text(
            284.0,
            357.0,
            anchor="nw",
            text="ejecucion_test",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        self.canvas.create_text(
            182.0,
            596.0,
            anchor="nw",
            text="0",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 24 * -1)
        )

        image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            643.0,
            257.0,
            image=image_image_6
        )

        # Recuadro de terminados
        self.canvas.create_rectangle(
            546.0,
            287.0,
            741.0,
            584.0,
            fill="#EEE8B7",
            outline="")

        self.canvas.create_text(
            546.0,
            287.0,
            anchor="nw",
            text="terminados_test",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            645.0,
            133.0,
            image=image_image_7
        )

        
        
        self.clock = self.canvas.create_text(
            593.0,
            115.0,
            anchor="nw",
            text="0:00",
            fill="#FFFFFF",
            font=("JosefinSansRoman Regular", 27 * -1)
        )  

        self.window.resizable(False, False)




        #---------------------------


        #---------------------------
        self.window.mainloop()

    def start_timer(self):
        
        try:
            if self.timer.running:
                raise Exception
            else:
                self.timer.start(self.window, self.canvas, self.clock)
        except Exception:
            messagebox.showerror("Error","Ya se esta ejecutando el programa")        

        
        
MyGUI()