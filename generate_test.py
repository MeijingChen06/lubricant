import numpy as np

from 训练.pi import number
feature_names = ['SiO₂','Al₂O₃','B₂O₃','CaO','Na₂O','Li₂O','MgO','BaO','ZnO','K₂O','PbO','SrO','GeO₂','ZrO₂','TiO₂','TeO₂','Fe$_m$O$_n$','P₂O₅']
a=[]
number=0
number1=0
for SiO2 in range(30,71,5):
    for Al2O3 in range(1,6,1):
        for B2O3 in range(20,31,2):
            for CaO in range(0, 10, 2):
                for Na2O in range(5, 16, 2):
                    for Li2O in range(0, 3, 1):
                        for MgO in range(0, 6, 1):
                            for BaO in range(0, 10, 2):
                                for ZnO in range(0, 3, 1):
                                    number1=number1+1
                                    if SiO2+Al2O3+B2O3+CaO+Na2O+Li2O+MgO+BaO+ZnO==100:
                                        number=number+1
                                        a.append([SiO2,Al2O3,B2O3,CaO,Na2O,Li2O,MgO,BaO,ZnO,0,0,0,0,0,0,0,0,0])
b=np.array(a)
np.savetxt('test7.csv',b,delimiter=',',fmt='%.2f')