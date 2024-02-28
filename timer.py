import tkinter as tk
import threading

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