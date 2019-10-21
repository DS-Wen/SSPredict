import numpy as np
import os
import pandas as pd
import re
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
            if re.search('element',line,re.IGNORECASE):
                if len(line.strip('\n').split(':')[1].split(","))!=3: print('element input invalid');quit()

                e1sub = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[0].split('-'))]
                eline1 = e1sub[0]
                if len(e1sub)>1: 
                    for item in e1sub[1:]: 
                        eline1 = eline1 + '-'+item
                e2sub = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[1].split('-'))]
                eline2 = e2sub[0]

                if len(e2sub)>1: 
                    for item in e2sub[1:]: 
                #        print(item)
                        eline2 = eline2 + '-'+item

                e3sub = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[2].split('-'))]
                #print(e1sub,e2sub,e3sub)
                #print(len(e1sub),len(e2sub),len(e3sub))

                eline3 = e3sub[0]
                if len(e3sub)>1: 
                    for item in e3sub[1:]: 
                        eline3 = eline3 + '-'+item

                elementline = 'element: '+eline1+', ' + eline2+', '+eline3+'\n'

            if re.search('ratio',line,re.IGNORECASE):
                if len(line.strip('\n').split(':')[1].split(","))!=3: print('element input invalid');quit()

                e1ratio = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[0].split('-'))]
                e2ratio = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[1].split('-'))]
                e3ratio = [item.strip(' ') for item in (line.strip('\n').split(':')[1].split(",")[2].split('-'))]
                ratioline = 'ratio: '+ str(e1ratio)+', '+ str(e2ratio)+', '+ str(e3ratio)+'\n'

            if re.search('structure',line,re.IGNORECASE):
                structure = line.strip('\n').split(':')[1].strip(' ').lower()
                structureline = 'structure: '+str(structure) + '\n'

            if re.search('temperature',line,re.IGNORECASE):
                try:T = line.strip('\n').split(':')[1].strip(' ');Tline = 'temperature: '+ str(T)+'\n';print('Temperature: ',T)
                except:print('temperature input invalid');quit();
            if re.search('increment',line,re.IGNORECASE):
                try:inc = line.strip('\n').split(':')[1].strip(' ');incline = 'increment: '+ str(inc)+'\n';print('Increment: ', inc)
                except:print('temperature input invalid');quit();
            if re.search('strain_r',line,re.IGNORECASE):
                try: ep = (line.strip('\n').split(':')[1].strip(' ')); srline = 'strain_r: '+ str(ep)+'\n';print('Strain rate: ', ep)
                except:print('strain rate input invalid')
            if re.search('data',line,re.IGNORECASE):
                N = fhlines.index(line)+1

        if structure != 'fcc' and structure != 'bcc':
            print('structure input invalid, only support fcc or bcc');quit()
        if e1sub == []:print('element input invalid');quit();
        if e2sub == []:print('element input invalid');quit();
        if e3sub == []:print('element input invalid');quit();
        if e1ratio == []:print('ratio input invalid');quit();
        if e2ratio == []:print('ratio input invalid');quit();
        if e3ratio == []:print('ratio input invalid');quit();

        for item in e1sub:
            e_order.append(item.strip(' '))
        for item in e2sub:
            e_order.append(item.strip(' '))
        for item in e3sub:
            e_order.append(item.strip(' '))
        self.eorder = e_order

        ''' beautiful lines: something like the following
        MnFeCoNiAlCu
        increment: 5
        strain_r: 0.001
        temperature: 300
        element: Mn-Co, Fe-Ni,Al-Cu
        ratio:50.0:50.0,50.0:50.0,50.0:50.0
        data:
        Mn,Fe,Co,Ni,Al,Cu
        12.60,12.09,11.12,10.94,16.472, 11.810
        338.84,26.375,262.89,199.1,65.498, 128.6
        130.52,8.9429,101.66,76.0,23.922, 48.0
        '''
        beautiful_lines = []
        beautiful_lines.append(fhlines[0])
        beautiful_lines.append(srline)
        beautiful_lines.append(Tline)
        beautiful_lines.append(elementline)
        beautiful_lines.append(ratioline)
        beautiful_lines.append(structureline)
        for line in fhlines[N-1:N+4]:
            beautiful_lines.append(line)
        print(beautiful_lines)
        return [e1sub, e2sub, e3sub], [e1ratio,e2ratio,e3ratio], e_order,structure,beautiful_lines

    def findnorganize(self):
        lines = open(self.file).readlines()
        for line in lines :
            if re.search('temperature',line,re.IGNORECASE):
                try:T = line.strip('\n').split(':')[1].strip(' ');print('Temperature: ',T)
                except:print('temperature input invalid');quit();
            if re.search('increment',line,re.IGNORECASE):
                try:inc = line.strip('\n').split(':')[1].strip(' ');print('Increment: ', inc)
                except:print('temperature input invalid');quit();
            if re.search('strain_r',line,re.IGNORECASE):
                try: ep = (line.strip('\n').split(':')[1].strip(' '));print('Strain rate: ', ep)
                except:print('strain rate input invalid')
            if re.search('data',line,re.IGNORECASE):
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
    elements,ratios,e_order,structure = g.grouping()
    print(elements,ratios,e_order,structure)
    Vlist, Elist, Slist, T, ep, inc = g.findnorganize()
    print(Vlist)
if __name__ == "__main__":
    main()
