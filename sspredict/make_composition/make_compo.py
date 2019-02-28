import numpy as np

class build_mesh:
##"build mesh grid for pseudo-ternary diagram"
# input is increment, each pseudo-ternary element range from 1-100
    def __init__(self, increment):
        if float(increment) <=0:
            print('error: increment should be positive float')
            quit()
        self.increment = float(increment)
    def make_mesh(self):
        comp =[]
        a1 = np.arange(0,100,self.increment);
        a1 = np.append(a1,100)
        for i in a1:
            a2 = np.arange(0,100-i,self.increment)
            a2 = np.append(a2,100-i)
            for j in a2:
                comp.append([i,j,100-i-j])
        return comp

def main():
    # debug
    mesh = build_mesh(0.1)
    comp = mesh.make_mesh()
    print(len(comp))
if __name__ == "__main__":
    main()
