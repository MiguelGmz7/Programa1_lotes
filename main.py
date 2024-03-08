from pathlib import Path
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import threading
import random

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/run/media/miguel/Data/User/Courses/Sem_SO/fkinTkinter/programa_1/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class MyGui:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("762x665")
        self.window.configure(bg = "#FFFFFF")
        
        self.timer = Timer()
        #self.processes = Processes()

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
            text="",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        self.canvas_espera = Canvas(
            self.canvas,
            bg = "#EEE8B7",
            height=300,
            width=195,
            bd=0
        )
        self.canvas_espera.place(x=24.0,y=284.0)

        self.label_espera = Label(self.canvas_espera,
            bd=1,
            bg="#EEE8B7",
            font=("JetBrainsMonoRoman Regular",11))
        
        self.label_espera.pack()
        

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
            text="",
            fill="#000000",
            font=("JetBrainsMonoRoman Regular", 15 * -1)
        )

        self.canvas_ejecucion = Canvas(
            self.canvas,
            bg = "#EEE8B7",
            height=166,
            width=195,
            bd=0
        )

        self.canvas_ejecucion.place(x=284.0,y=357.0)

        self.label_ejecucion = Label(self.canvas_ejecucion,
            bd=1,
            bg="#EEE8B7",
            font=("JetBrainsMonoRoman Regular",11))
        
        self.label_ejecucion.pack()

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

        self.imprimir = self.window.mainloop()

        # funciones de GUI

    def start_timer(self):
        if self.timer.running:
            messagebox.showerror("Error","Ya se esta ejecutando el programa")
        
        elif not self.entry_1.get().isdigit():
            messagebox.showerror("Error","Tienes que ingresar un numero")
            
        else:
            self.timer.start(self.window, self.canvas, self.clock)
        

class Timer:
    def __init__(self):
        self.time_string = tk.StringVar()
        self.running = False
        self.seconds = 0
           

    def update_time(self,window,canvas,clock):
        if self.running:
            self.seconds += 1
            minutes = self.seconds // 60
            seconds = self.seconds % 60
            self.time_string.set(f"{minutes}:{seconds:02}")
            canvas.itemconfig(clock, text=self.time_string.get())
            window.after(1000, self.update_time,window,canvas,clock)
    
    def start(self, window, canvas, clock):
        
        self.running = True
        threading.Thread(target=self.update_time,args=(window,canvas,clock)).start()

    def stop(self, canvas, clock):
        self.running = False
        self.seconds = 0



class Processes:
    def __init__(self):
        self.time_string = tk.StringVar()
        self.string = ""
        self.done = False
        

    def setProcesos(self, processes):
        # Split the processes into batches of 5
        self.batches = [processes[i:i + 5] for i in range(0, len(processes), 5)]
        self.head = self.batches[0][0]
    
    def genProcesos(self, num_processes):
        users = ['Jose', 'Carlos', 'Carolina', 'Juan']
        sims = ('+','-','*','/')
        total_processes = []
        count = 0
        for i in range(int(num_processes)):
            count += 1
            user = random.choice(users)
            n1 = random.randint(1, 9)
            sim = random.choice(sims)
            n2 = random.randint(1, 9)
            tme = random.randint(4, 13)

            element = {"id":count, "user": user, "n1": n1, "sim": sim, "n2":n2, 'tme':tme}
            total_processes.append(element)
        
        self.setProcesos(total_processes)
        self.print_process()
        
    def print_process(self):
        
        count = 0
        count2 = 0
        with open('datos.txt', 'w') as file:
            for i in self.batches:
                count += 1
                file.write("Lote N: " + str(count) + "\n")
                file.write("------------------")
                file.write("\n")
                for j in i:
                    count2 += 1
                    file.write(str(count2)+". "+j['user']+"\n")
                    file.write(str(j['n1'])+" "+ j['sim']+ " "+ str(j['n2']) +"\n")
                    file.write("TME: "+str(j['tme'])+"\n"+"\n")

                
                file.write("\n")
                file.write("\n")
    
                
    def execute_process(self,label,window):
        if self.head['tme'] > 0:
            self.head['tme'] -= 1

            self.string += str(self.head['id'])+". "+self.head['user']+"\n"
            self.string += str(self.head['n1'])+" "+ self.head['sim']+ " "+ str(self.head['n2']) +"\n"
            self.string += "TME: "+str(self.head['tme'])

            self.time_string.set(self.string)
            label.config(text=self.time_string.get())
            self.string = ""
            self.time_string.set("")
            window.after(1000, self.execute_process,label,window)
            self.execute = True
        else:
            self.string = ""
            self.time_string.set("")
            label.config(text="")
            self.finish_e = self.batches[0][0]
            del self.batches[0][0] 
            #print(self.finish_e)
            # self.execute = False
            # #self.semaforo.acquire()
            self.done = True
    
 

gui = MyGui()
gui.window.mainloop()
