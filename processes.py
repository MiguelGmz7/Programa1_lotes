import random
import tkinter as tk
class Processes:
    def __init__(self):
        self.time_string = tk.StringVar()
        self.string = ""
        

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

