import numpy as np
import pandas as pd
class findproperty:
# search input file for material properties E,n
# according to their orders in the groups
    def __init__(self,fh,e_order):
        self.file = fh
        self.eorder = e_order
    def findnorganize(self):
        lines = open(self.file).readlines()
        for line in lines :
            if line.startswith('data'):
                N = lines.index(line)+1
        print(N)
        try: data =pd.read_csv(self.file,header=N,delimiter=',');print(data)
        except:print('illegal input file format');quit()
        Vlist = [];Elist=[];Slist=[]
        for element in self.eorder:
            Vlist.append(data[element][0])
            Elist.append(data[element][1])
            Slist.append(data[element][2])
        return Vlist, Elist, Slist
def main():
    # debug
    found = findproperty('input_example',['Mn','Co','Fe','Ni','Al'])
    V,E,S = found.findnorganize()
    print(V,E,S)
if __name__ == "__main__":
    main()
