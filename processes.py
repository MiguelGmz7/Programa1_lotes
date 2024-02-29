import random
class Processes:
    def __init__(self):
        pass

    def setProcesos(self, processes):
        # Split the processes into batches of 5
        self.batches = [processes[i:i + 5] for i in range(0, len(processes), 5)]
    
    def genProcesos(self, num_processes):
        users = ['Jose', 'Carlos', 'Carolina', 'Juan']
        sims = ('+','-','*','/')
        total_processes = []
        for i in range(int(num_processes)):
            user = random.choice(users)
            n1 = random.randint(1, 9)
            sim = random.choice(sims)
            n2 = random.randint(1, 9)

            element = {"user": user, "n1": n1, "sim": sim, "n2":n2}
            total_processes.append(element)
        
        self.setProcesos(total_processes)
        print(self.batches)