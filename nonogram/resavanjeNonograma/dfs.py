from nonogram import Nonogram
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
    #rjesenje=nono.nono
    #pocetak=nono.nono
    prolazi = []
    struktura.push(prolazi)
    while struktura.isEmpty()==False:
        #izaberi list za ekspanziju na osnovu strategije
        prolazi=struktura.pop()
        print("ss")
        print(prolazi)
        # if da li je to rjesenje? ako jeste vrati ga
        if len(prolazi)==len(nono.nono):
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
                #print(prolazi)
                #print(dijete[list(dijete.keys())[0]])
                if nasao==False:
                    listica=[]
                    for i in prolazi:
                        listica.append(i)
                    prosao.append(listica)
                    for i in range(len(prolazi)):
                        djetasce = nono.rowPermutations(nono.rows[i], len(nono.nono[0]))
                        for dijetee in djetasce:
                            if(list(dijetee.keys())[0]==prolazi[i]):
                                nono.nono[i] = dijetee[prolazi[i]]



                    #print (nono.nono)
                    if not(nono.isBroken()):
                        struktura.push(listica)
                prolazi.pop()
    return nono
if __name__ == '__main__':
    rows = [[1, 2], [1, 3], [3], [2], [1]]
    columns = [[2], [2], [3], [3], [3]]
    nono = Nonogram(rows, columns)
    depthFirstSearch(nono)
    print(nono.nono)