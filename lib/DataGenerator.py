# time3Dstat
# time3dmag
# fft3dstat
# fft3dmag
import numpy as np
import scipy as sc
from StatFunc import StatFunc

class Time3DStat:
    
    def __init__(self,windowX,windowY,windowZ):
        self.windowX = windowX
        self.windowY = windowY
        self.windowZ = windowZ

    def generate(self):
        fun = StatFunc()
        ans = [
            np.mean(self.windowX),
            np.mean(self.windowY),
            np.mean(self.windowZ),
            np.std(self.windowX),
            np.std(self.windowY),
            np.std(self.windowZ),
        ]
        ans.append([
            fun.mad(self.windowX,ans[0]),
            fun.mad(self.windowY,ans[1]),
            fun.mad(self.windowZ,ans[2]),
            np.max(self.windowX),
            np.max(self.windowY),
            np.max(self.windowZ),
            np.min(self.windowX),
            np.min(self.windowY),
            np.min(self.windowZ),
            fun.sma(self.windowX,self.windowY,self.windowZ,ans[0],ans[1],ans[2]),
            fun.energy(self.windowX),
            fun.energy(self.windowY),
            fun.energy(self.windowZ),
            sc.stats.iqr(self.windowX),
            sc.stats.iqr(self.windowY),
            sc.stats.iqr(self.windowZ),
            fun.entropy(self.windowX),
            fun.entropy(self.windowY),
            fun.entropy(self.windowZ),
        ])
        arc = fun.arburg(self.windowX,4)
        ans.append(arc[0])
        arc = fun.arburg(self.windowY,4)
        ans.append(arc[0])
        arc = fun.arburg(self.windowZ,4)
        ans.append(arc[0])
        corr = np.corrcoef(self.windowX,self.windowY)
        ans.append(corr[0][1])
        corr = np.corrcoef(self.windowY,self.windowZ)
        ans.append(corr[0][1])
        corr = np.corrcoef(self.windowX,self.windowZ)
        ans.append(corr[0][1])

        return ans

class Time3DMag:
    def __init__(self,window):
        self.window = window

    def generate(self):
        fun = StatFunc()
        ans = [
            np.mean(self.window),
            np.std(self.window),
        ]
        ans.append([
            fun.mad(self.window,ans[0]),
            np.max(self.window),
            np.min(self.window),
            
        ])