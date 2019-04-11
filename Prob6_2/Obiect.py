class Sistem_Demonstratii:
    def __init__(self, graph = None):
        if graph == None:
            graph = {}
        self.graph = graph

    def initializare_sistem(self):
        print("Cate expresii doriti sa intializati: ",end="")
        nr = int(input())
        self.nr = nr
        lista_1 = list()#lista ce contine intreaga instructiune
        lista_2 = list()#lista ce contine numele operatiilor ex i1
        lista_3 = list()#lista ce contine nodurile de plecare in cazul in care se alege o ipoteza
        lista_4 = list()#lista ce contine nodurile de sosire
        
        self.lista_1 = [0 for i in range(nr+100)]
        self.lista_2 = [0 for i in range(nr+10)]
        self.lista_3 = [0 for i in range(nr+100)]
        self.lista_4 = [0 for i in range(nr+100)]
        print("ex: t1: ipoteze i; concluzii a, b, c")

        for i in range (0, nr + 1):
            self.lista_1[i]= input("Introduce-ti expresia: ")
            o_lista = self.lista_1[i].split(":")
            stanga = str(o_lista[0])
            dreapta = str(o_lista[1])
            dreapta = dreapta.strip()
            if "a" in stanga:
                lista = dreapta.split(" ")
                j = int(0)
                for i in lista:
                    if j != 0:
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.add_node(str(stanga[0]))
                    j += 1
        
            elif "t" in stanga:
                stanga, backup = dreapta.split(";")
                stanga = stanga.strip()
                lista = stanga.split(" ")
                j = int(0)
                iterator = int(-1)
                for i in lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.add_node(str(stanga[0]))
                        self.lista_3[iterator] = stanga[0]
                        
                    j += 1
                backup = backup.strip()
                iterator_1 = int(iterator)
                alta_lista = backup.split(" ")
                j = int(0)
                iterator = int(-1)
                for k in alta_lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(alta_lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.lista_4[iterator] = stanga[0]
                        
                    j += 1
                iterator_2 = int(iterator)
                for i in range(0,iterator_1+1):
                    for j in range(0,iterator_2+1):
                        nod_1 = str(self.lista_3[i])
                        nod_2 = str(self.lista_4[j])
                        self.add_edge(str(nod_1), str(nod_2))

    def afisare(self):
        for i in range(0,self.nr+1):
             print(self.lista_1[i])
        for x in self.graph:
            print(str(x)+": " +str(self.graph[x]))

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []


    def add_edge(self, node_1, node_2):
        if node_1 in self.graph:
            if node_2 not in self.graph[node_1]:
             self.graph[node_1].append(node_2)

    def smallest_prove(self, start, end, path=None):
        if path == None:
            path = []
        graph = self.graph
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            print("Nodul nu se afla in graph "+str(start))
            return None
        for node in graph[start]:
            if node not in path:
                extended_path = self.smallest_prove(node, end, path)
                if extended_path: 
                    return extended_path
        return None

    def prove(self, start, end, path=[]):
        graph = self.graph 
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                extended_paths = self.prove(node, end, path)
                for i in extended_paths: 
                    paths.append(i)
        return paths

    def remove_edge(self, node_1, node_2):
        self.graph[node_1].remove(node_2)

    def det(self):
        for node in self.graph:
            for edge in self.graph[node]:
                if "!" in edge:
                    print("Sistemul este invalid!")
                    return
        print("Sistemul este valid")

    def sterge(self):
        graph = self.graph
        j=int(-1)
        for i in self.lista_1:
            j += 1
            print(str(j)+ " "+str(i))
        print("Ce teorema doriti stearsa(0 - " + str(self.nr) + "): ",end="")
        a = int(input())
        nr =int(0)
        self.lista_3 = [0 for i in range(nr+100)]
        self.lista_4 = [0 for i in range(nr+100)]

        for i in range (0, nr + 1):
            o_lista = self.lista_1[a].split(":")
            stanga = str(o_lista[0])
            dreapta = str(o_lista[1])
            dreapta = dreapta.strip()
            if "a" in stanga:
                lista = dreapta.split(" ")
                j = int(0)
                for i in lista:
                    if j != 0:
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        del graph[str(stanga[0])]
                    j += 1
        
            elif "t" in stanga:
                stanga, backup = dreapta.split(";")
                stanga = stanga.strip()
                lista = stanga.split(" ")
                j = int(0)
                iterator = int(-1)
                for i in lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.lista_3[iterator] = stanga[0]
                        
                    j += 1
                backup = backup.strip()
                iterator_1 = int(iterator)
                alta_lista = backup.split(" ")
                j = int(0)
                iterator = int(-1)
                for k in alta_lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(alta_lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.lista_4[iterator] = stanga[0]
                        
                    j += 1
                iterator_2 = int(iterator)
                for i in range(0,iterator_1+1):
                    for j in range(0,iterator_2+1):
                        nod_1 = str(self.lista_3[i])
                        nod_2 = str(self.lista_4[j])
                        self.remove_edge(str(nod_1), str(nod_2))
                empty_keys = [k for k,v in graph.items() if not v]
                for k in empty_keys:
                       del graph[k]
      
        for i in range(a,self.nr+1):
            if i != self.nr:
             self.lista_1[i] = self.lista_1[i+1]
            else:
                del self.lista_1[i]
        self.graph = graph
        self.nr -= 1
        

    def adaugare(self):
        print("ex: t1: ipoteze i; concluzii a, b, c",)
        nr = int(0)

        self.lista_3 = [0 for i in range(nr+100)]
        self.lista_4 = [0 for i in range(nr+100)]
        self.nr += 1

        for i in range (0, nr + 1):
            self.lista_1[self.nr]= input("Introduce-ti expresia: ")
            o_lista = self.lista_1[self.nr].split(":")
            stanga = str(o_lista[0])
            dreapta = str(o_lista[1])
            dreapta = dreapta.strip()
            if "a" in stanga:
                lista = dreapta.split(" ")
                j = int(0)
                for i in lista:
                    if j != 0:
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.add_node(str(stanga[0]))
                    j += 1
        
            elif "t" in stanga:
                stanga, backup = dreapta.split(";")
                stanga = stanga.strip()
                lista = stanga.split(" ")
                j = int(0)
                iterator = int(-1)
                for i in lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.add_node(str(stanga[0]))
                        self.lista_3[iterator] = stanga[0]
                        
                    j += 1
                backup = backup.strip()
                iterator_1 = int(iterator)
                alta_lista = backup.split(" ")
                j = int(0)
                iterator = int(-1)
                for k in alta_lista:
                    if j != 0:
                        iterator += 1
                        stanga = str(alta_lista[j])
                        stanga.strip()
                        stanga = stanga.split(",")
                        self.lista_4[iterator] = stanga[0]
                        
                    j += 1
                iterator_2 = int(iterator)
                for i in range(0,iterator_1+1):
                    for j in range(0,iterator_2+1):
                        nod_1 = str(self.lista_3[i])
                        nod_2 = str(self.lista_4[j])
                        self.add_edge(str(nod_1), str(nod_2))

    
