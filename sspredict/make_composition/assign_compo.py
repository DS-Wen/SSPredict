import numpy as np
class assign:
# assign a new concentration value to each component
# according to their ratio input
    def __init__(self,ratio,con):
        self.ratio = [float(i) for i in ratio]
        self.con = con
    def conassign(self):
        if len(self.ratio) ==1:
            new_cons = self.con
            new_ratio = [100]
            return [new_cons], new_ratio
        else:
            new_cons = [self.con*i/sum(self.ratio) for i in self.ratio]
            new_ratio = [round(100*i/sum(self.ratio),0) for i in self.ratio]
        return new_cons,new_ratio
def main():
    # debug
    c = assign(['50','40'],100)
    newcons,new_ratio = c.conassign()
    print(newcons)
if __name__ == "__main__":
    main()
