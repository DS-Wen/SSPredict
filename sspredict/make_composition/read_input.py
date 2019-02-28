import numpy as np
import os
import pandas as pd
class read_inputfile:
# group the elements from reading the input file
    def __init__(self,fh):
        if os.path.isfile('./'+fh):
            self.file = fh
            self.eorder = None
        else:
            print('input file not in current directory')
            quit()
    def grouping(self):
        e_order = []
        fhlines = open(self.file).readlines()
        for line in fhlines:
            if line.startswith('e:'):
                e1sub = (line.strip('\n').strip('e:').split(",")[0].strip(' ').split('-'))
                e2sub = (line.strip('\n').strip('e:').split(",")[1].strip(' ').split('-'))
                e3sub = (line.strip('\n').strip('e:').split(",")[2].strip(' ').split('-'))
            if line.startswith('ratio:'):
                e1ratio = (line.strip('\n').strip('ratio:').split(",")[0].strip(' ').split('-'))
                e2ratio = (line.strip('\n').strip('ratio:').split(",")[1].strip(' ').split('-'))
                e3ratio = (line.strip('\n').strip('ratio:').split(",")[2].strip(' ').split('-'))
        for item in e1sub:
            e_order.append(item)
        for item in e2sub:
            e_order.append(item)
        for item in e3sub:
            e_order.append(item)
        self.eorder = e_order
        return [e1sub, e2sub, e3sub], [e1ratio,e2ratio,e3ratio], e_order
    def findnorganize(self):
        lines = open(self.file).readlines()
        for line in lines :
            if ('temperature') in line:
                try:T = line.strip('\n').split(':')[1].strip(' ');print('Temperature: ',T)
                except:print('temperature input invalid');quit();
            if ('increment') in line:
                try:inc = line.strip('\n').split(':')[1].strip(' ');print('Increment: ', inc)
                except:print('temperature input invalid');quit();
            if ('strain_r') in line:
                try: ep = (line.strip('\n').split(':')[1].strip(' '));print('Strain rate: ', ep)
                except:print('strain rate input invalid')
            if ('data') in line:
                N = lines.index(line)+1
        #print(N)
        try: data =pd.read_csv(self.file,header=N,delimiter=',');print(data)
        except:print('illegal input file format');quit()
        Vlist = [];Elist=[];Slist=[]
        for element in self.eorder:
            Vlist.append(data[element][0])
            Elist.append(data[element][1])
            Slist.append(data[element][2])
        return Vlist, Elist, Slist, T, ep, inc

def main():
    # debug
    g = read_inputfile('input_example')
    elements,ratios,e_order = g.grouping()
    print(len(elements))
if __name__ == "__main__":
    main()
