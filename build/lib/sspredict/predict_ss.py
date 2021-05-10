try:
    from sspredict.make_composition import build_mesh, read_inputfile, assign, ss_model
except:
    from make_composition import build_mesh, read_inputfile, assign, ss_model
import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '-filein', type=str, help='input filename for calculation')
    parser.add_argument('-o', '-output', type=str, help='output filename for plotting')
    args = parser.parse_args()
    # read input file
    inputfile = args.f
    outputfile = args.o # output file name
    g = read_inputfile(inputfile)
    elements,ratios,e_order,structure,lines1 = g.grouping()

    #calculate ratio with a scale of 100

    V,E,S,T,ep,inc = g.findnorganize()
    # make composition mesh
    x = build_mesh(inc)
    b = x.make_mesh()

    newcons = []
    for i in b:
        cs =[]
        c = assign(ratios[0],i[0]);ce1,nrA = c.conassign()
        c = assign(ratios[1],i[1]);ce2,nrB = c.conassign()
        c = assign(ratios[2],i[2]);ce3,nrC = c.conassign()
        for item in ce1:
            cs.append(item)
        for item in ce2:
            cs.append(item)
        for item in ce3:
            cs.append(item)
        newcons.append(cs)
    sA = ':'.join([str(s) for s in nrA]);sB = ':'.join([str(s) for s in nrB]);
    sC = ':'.join([str(s) for s in nrC]);
    ratioline = 'ratio:'+sA+','+sB+','+sC+'\n'
    #print(ratioline)
    ss = ss_model(V,E,S,newcons[1],ep,T,e_order,b[0],structure,inputfile)

    writeheader = ss.columnheader()
    with open('%s.txt' % outputfile,'a') as f:
        for line in lines1:
            if 'ratio' in line:
                line = ratioline
            if '\n' not in line:
                line = line+'\n'
            f.write(line)
        f.write('Start of Predicted Data\n')
        writer = csv.writer(f)
        writer.writerow(writeheader)
    writedata_all = []

    for cons in newcons:
        i = newcons.index(cons)
        ss = ss_model(V,E,S,cons,ep,T,e_order,b[i],structure,inputfile)
        writedata = ss.str_calc()
        writedata_all.append(writedata)

    with open('%s.txt' % outputfile,'a') as f:
        writer = csv.writer(f)
        writer.writerows(writedata_all)


if __name__ == "__main__":
    main()
