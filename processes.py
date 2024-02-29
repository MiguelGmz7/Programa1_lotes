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
            tme = random.randint(4, 13)

            element = {"user": user, "n1": n1, "sim": sim, "n2":n2, 'tme':tme}
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
                    file.write("Proceso N: " + str(count2) + "\n")
                    file.write("Usuario: " + j['user'] + "\n")
                    file.write("N1: " + str(j['n1']) + "\n")
                    file.write("Simbolo: " + j['sim'] + "\n")
                    file.write("N2: " + str(j['n2']) + "\n")
                    file.write("Tiempo: " + str(j['tme']) + "\n")
                    file.write("\n")
                
                file.write("\n")
                file.write("\n")

                

            # file.write("test 1\n")
            # file.write("test 2\n")
            # file.write("test 3\n")
