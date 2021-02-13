from itertools import combinations_with_replacement,permutations
class Nonogram():
    def __init__(self,rows,columns):
        self.rows=rows
        self.columns=columns
        self.nono=[]
        row=[]
        for i in range(len(self.columns)):
            row.append(0)
        for i in range(len(self.rows)):
            self.nono.append(row)
    def isBroken(self):
        """
        for i in range(len(self.rows)):
            checkRow=[]
            br=0
            for ii in self.nono[i]:
                if ii==1:
                    br=br+1
                elif br!=0 and ii==0:
                    checkRow.append(br)
                    br=0
            if(len(checkRow)>len(self.rows[i])):
                return True
            for i in range(len(self.rows[i])):
                if checkRow[i]>self.rows[i][i]:
                    return True
        """
        for i in range(len(self.columns)):
            column=[]
            for iii in self.nono:
                column.append(iii[i])
            checkRow=[]
            br=0
            for ii in column:
                if ii==1:
                    br=br+1
                elif br!=0 and ii==0:
                    checkRow.append(br)
                    br=0
            if(len(checkRow)>len(self.columns[i])):
                return True
            for i in range(len(self.columns[i])):
                try:
                    if checkRow[i]>self.columns[i]:
                        return True
                except:
                    pass
        return False
    def isSolved(self):
        #treba provjeriti da li je broken
        brojac1=0
        brojac2=0
        for i in self.nono:
            for ii in i:
                if ii==1:
                    brojac1=brojac1+1
        for i in self.rows:
            for ii in i:
                brojac2=brojac2+ii
        return brojac1==brojac2
    def rowPermutations(self,row,duzina):
        trenutniRed=[]
        for i in row:
            for a in range(i):
                trenutniRed.append(1)
            trenutniRed.append(0)
        trenutniRed.pop()
        br_praznina=duzina-len(trenutniRed)
        praznine=[0]
        for i in range(len(row)):
            praznine.append(0)
        lista=list(range(0,br_praznina+1))
        perm = combinations_with_replacement(lista,len(praznine))
        permutacije=[]
        for i in perm:
            if (sum(i)==br_praznina):
                permutacije.append(i)
        sve_perm=[]
        for i in permutacije:
            perma=[]
            for a in i:
                perma.append(a)
            #print(perma)
            permem = permutations(perma)
            for dod in permem:
                #print(ii)
                sve_perm.append(dod)
        preciscene_perm=[]
        for i in sve_perm:
            if not(i in preciscene_perm):
                preciscene_perm.append(i)
        izbori=[]
        br = 1
        for i in preciscene_perm:
            izbor=[]
            brojac=0
            for ii in i:
                for iii in range(ii):
                    izbor.append(0)
                if (brojac<=len(i)-2):
                    for iiii in range(row[brojac]):
                        izbor.append(1)
                    if (brojac<len(i)-2):
                        izbor.append(0)
                brojac=brojac+1
            izbori.append({br:izbor})
            br=br+1
        return izbori
if __name__ == '__main__':
    rows=[[1,2],[1,3],[3],[2],[1]]
    columns = [[2], [2], [3], [3], [3]]
    nono =Nonogram(rows,columns)
    print(nono.nono)
    nono.nono=[[1, 0, 0, 1, 1], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 0, 0], [0, 1, 0, 0, 0]]
    print(nono.rowPermutations([1,3],5))
    print(nono.isBroken())
    print(nono.isSolved())