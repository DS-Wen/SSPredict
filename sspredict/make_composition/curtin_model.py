import numpy as np
class ss_model:
# calculate solid solution strengthening contribution
#
    def __init__(self,V,E,S,c,ep,T,e_order,inputfile,b):
        self.V = [i*10**(-30) for i in V] ;self.ep=float(ep);self.inputfile = inputfile
        self.E = [i*10**(9) for i in E];self.T = float(T)
        self.S = [i*10**(9) for i in S];self.eorder = e_order
        self.c = [ i/100 for i in c];self.psc = [ i/100 for i in b]
    def columnheader(self):
        lines1 = open(self.inputfile).readlines()
        writeheader = []
        for e in ['psA','psB','psC']:
            writeheader.append(e)
        for e in self.eorder:
            writeheader.append(e)
        for e in ['V_ave','b_ave','E_ave','mu_ave','nu_ave','sum_cnVn^2_b6','Ty0_tensile','Delta_Eb','Delta_sigma_ss']:
            writeheader.append(e)
        return lines1, writeheader
    def str_calc(self):
        # average values
        i = 0;Vc=[];Ec=[];Sc=[]
        ep0 = 10**4    #reference strain rate (/s)
        kc = 1.38064852*10**(-23) #J/K
        while i < len(self.c):
            Vc.append(self.V[i] * self.c[i])
            Ec.append(self.E[i] * self.c[i])
            Sc.append(self.S[i] * self.c[i])
            i += 1
        aver_V = sum(Vc);aver_E = sum(Ec);aver_S = sum(Sc)
        aver_Nu = aver_E/(2*aver_S) - 1
        aver_b = (4*aver_V)**(1/3)/(2**0.5)
        i = 0;Cn_delta_Vn=[]
        while i < len(self.c):
            Cn_delta_Vn.append((self.V[i] - aver_V)**2*self.c[i])
            i += 1
        sum_cndVn_b6 = sum(Cn_delta_Vn)/aver_b**6;
        q_nu = ((1 + aver_Nu)/(1 - aver_Nu))
        dEb = 1.5618  *  0.123**(1/3) * aver_S * aver_b**3   * q_nu**(2/3) * sum_cndVn_b6**(1/3)
        J2eV=6.2415093433*10**18
        Ty0 = 0.01785 * 0.123**(-1/3)  *   aver_S    *        q_nu**(4/3) * sum_cndVn_b6**(2/3)
        Ty0_tensile = 3.06 * Ty0
        delta_ss = Ty0_tensile  * (1 - ((kc*self.T)/(dEb) * np.log(ep0/self.ep))**(2/3) )
        writedata = []
#writeheader = append(e for e in ['V_ave','b_ave','E_ave','mu_ave','nu_ave','sum_cnVn^2_b6','Ty0_tensile','Delta_Eb','Delta_sigma_ss'])
        for e in self.psc:
            writedata.append(e)
        for e in self.c:
            writedata.append(round(float(e),3))
        for e in [aver_V*10**30,aver_b*10**10,aver_E/10**9,aver_S/10**9,aver_Nu,sum_cndVn_b6,Ty0_tensile/10**6,dEb*J2eV,delta_ss/10**6]:
            writedata.append(e)
        return writedata
def main():
    # debug
    ss = ss_model(V,E,S,c,ep,T,e_order,inputfile)
    lines1, writeheader = ss.columnheader()
    writedata = ss.str_calc()

if __name__ == "__main__":
    main()
