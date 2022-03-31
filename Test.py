import re
import numpy as np


def main():

    AmpFactor = 0.000005
    GammaFactor = 3.134
    contrast = 1.0
    gray = 50
    inc = gray*contrast
    
    x = "1000.12324321234     1000"
    
    parasize = "parasize800.000 1234 5678"
    
    parasize = parasize.replace("parasize", "")
    
   # y = '%d' % ('42',)

    var = (re.split('(\d.*)', parasize)[1])
    
    
    
    x = parasize.split(" ")
    y = np.asfarray(x, float)
    
    res = float(x[1])
    
    print(res)
    
    #print([float(i) for i in x.split()])
    
    #print("gamma" + str(GammaFactor) + "amp" + str(AmpFactor))

main()