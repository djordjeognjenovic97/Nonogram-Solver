from nonogram import Nonogram
import copy
class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0
def depthFirstSearch(nono):
    struktura=Stack() #lifo za dfs
    prosao=[]
    prolazi = []
    struktura.push([])
    prazanNono=nono.nono
    while struktura.isEmpty()==False:
        prolazi=copy.deepcopy(struktura.pop())
        # if da li je to rjesenje? ako jeste vrati ga
        if len(prolazi)==len(nono.nono):
            nono.nono=prazanNono
            for i in range(len(prolazi)):
                djeca = nono.rowPermutations(nono.rows[i], len(nono.nono[0]))
                for dijetee in djeca:
                    if (list(dijetee.keys())[0] == prolazi[i]):
                        nono.nono[i] = dijetee[prolazi[i]]
            if nono.isSolved() and not(nono.isBroken()):
                return nono
        #else onda dodaj dijecu tj. moguce sl poteze sa tog polja u stablo pretrage
        else:
            djeca=nono.rowPermutations(nono.rows[len(prolazi)],len(nono.nono[0]))
            for dijete in djeca:
                prolazi.append(list(dijete.keys())[0])
                nasao=False
                for korak in prosao:
                    if prolazi==korak:
                        nasao=True
                        break
                if nasao==False:
                    listica=[]
                    for i in prolazi:
                        listica.append(i)
                    prosao.append(copy.deepcopy(listica))
                    nono.nono=prazanNono
                    for i in range(len(prolazi)):
                        djetasce = nono.rowPermutations(nono.rows[i], len(nono.nono[0]))
                        for dijetee in djetasce:
                            if(list(dijetee.keys())[0]==prolazi[i]):
                                nono.nono[i] = dijetee[prolazi[i]]
                    #if not(nono.isBroken()):
                    struktura.push(copy.deepcopy(listica))
                prolazi.pop()
    print(prosao)
    return nono
if __name__ == '__main__':
    rows = [[1, 2], [1, 3], [3], [2], [1]]
    columns = [[2], [2], [3], [3], [3]]
    nono = Nonogram(rows, columns)
    depthFirstSearch(nono)
    print(nono.nono)