from collections import defaultdict
from os import close
from queue import PriorityQueue
import array as arr
from typing import ClassVar


data = defaultdict(list)
data['S'] = ['G', 12, 'A', 1]
data['A'] = ['B', 3, 'C', 1]
data['B'] = ['D', 3]
data['C'] = ['D', 1, 'G', 2]
data['D'] = ['G', 3]

# data['Oradea'] = ['Zerind', 71, 'Sibiu', 151]
# data['Zerind'] = ['Oradea', 71, 'Arad', 75]
# data['Arad'] = ['Zerind', 75, 'Sibiu', 140, 'Timisoara', 118]
# data['Sibiu'] = ['Oradea', 151, 'Arad', 140, 'Fagaras', 99, 'RimnicuVilcea', 80]
# data['Timisoara'] = ['Arad', 118, 'Lugoj', 111]
# data['Lugoj'] = ['Timisoara', 111, 'Mehadia', 70]
# data['Mehadia'] = ['Lugoj', 70, 'Dobreta', 75]
# data['Dobreta'] = ['Mehadia', 75, 'Craiova', 120]
# data['Craiova'] = ['Dobreta', 120, 'RimnicuVilcea', 146, 'Pitesti', 138]
# data['RimnicuVilcea'] = ['Sibiu', 80, 'Craiova', 146, 'Pitesti', 97]
# data['Pitesti'] = ['RimnicuVilcea', 97, 'Craiova', 138, 'Bucharest', 101]
# data['Fagaras'] = ['Sibiu', 99, 'Bucharest', 211]

class Node:
    def __init__(self, name, par = None, g = 0):
        self.name = name
        self.par = par
        self.g = g
    def display(self):
        print (self.name, self.g)
    def __lt__(self, other):
        if other == None:
            return False
        return self.g < other.g

def equal(O, G):
    if O.name == G.name:
        return True
    return False
def checkInPriority(tmp, c):
    if tmp == None:
        return False
    return (tmp in c.queue)
def checkInOpen(tmp, c):
    if tmp == None:
        return False
    else:
        for search in c:
            if(tmp == search):
                return True  
        return False
def getPath(O):
    print (O.name)
    if O.par != None:
        getPath(O.par)
    else:
        return
def addToOpen(tmp, c):
    count = 0
    dich = len(c)

    if(dich == 0): 
        c.insert(count, tmp)
    else: 
        while(count < dich):
            if(tmp.g < c[count].g): 
                c.insert(count, tmp)
                break
            else:
                if(count == (dich - 1)):
                    c.append(tmp)
            count+=1

def UniformCostSearch(S, G):
    Open = []
    Closed = PriorityQueue()
    Open.append(S)

    while True:
        if len(Open) == 0:
            print('Tim kiem that bai')
            return
        
        O = Open[0]
        Open.remove(O)
        Closed.put(O)

        if equal(O, G) == True:
            print('Tim kiem thanh cong')
            getPath(O)
            print('distance: ', O.g)
            return

        i = 0
        while i < len(data[O.name]):
            name = data[O.name][i]
            g = O.g + data[O.name][i + 1]
            tmp = Node(name = name, g = g)
            tmp.par = O
            
            check1 = checkInOpen(tmp, Open)
            
            check2 = checkInPriority(tmp, Closed)
            
            if not check1 and not check2:
                addToOpen(tmp, Open)
            i+=2

def main():
    UniformCostSearch(Node('S'), Node('D'))
    # UniformCostSearch(Node('Arad'), Node('Bucharest'))

if __name__ == "__main__":
    main()
