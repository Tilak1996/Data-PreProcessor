import numpy as np
import scipy as sc

class StatFunc:

    def mad(self,X,mean):
        sum = 0
        for x in X:
            sum = sum + abs(x-mean)
        return (sum/len(X))

    def sma(self, X, Y, Z, xmean, ymean, zmean):
        return self.mad(X,xmean) + self.mad(Y,ymean) + self.mad(Z,zmean)

    def energy(self,X):
        sum = 0
        for x in X:
            sum = sum + x**2
        return sum

    def entropy(self,X):
        hist = np.histogram(X)
        hist = hist[:]/len(X)
        return sc.stats.entropy(hist)

    def arburg(self, X, order):
        """This version is 10 times faster than arburg, but the output rho is not correct.
        
        
        returns [1 a0,a1, an-1]
        
        """
        x = np.array(X)
        N = len(x)

        if order == 0.: 
            raise ValueError("order must be > 0")

        # Initialisation
        # ------ rho, den
        rho = sum(abs(x)**2.) / N  # Eq 8.21 [Marple]_
        den = rho * 2. * N 

        # ------ backward and forward errors
        ef = np.zeros(N)
        eb = np.zeros(N)    
        for j in range(0, N):  #eq 8.11
            ef[j] = x[j]
            eb[j] = x[j]

        # AR order to be stored
        a = np.zeros(1)
        a[0] = 1
        # ---- rflection coeff to be stored
        ref = np.zeros(order)

        # temp = 1.
        E = np.zeros(order+1)
        E[0] = rho

        for m in range(0, order):
            #print m
            # Calculate the next order reflection (parcor) coefficient
            efp = ef[1:]
            ebp = eb[0:-1]
            #print efp, ebp
            num = -2.* np.dot(ebp.conj().transpose(),  efp)
            den = np.dot(efp.conj().transpose(),  efp)
            den += np.dot(ebp,  ebp.conj().transpose())
            ref[m] = num / den

            # Update the forward and backward prediction errors
            ef = efp + ref[m] * ebp
            eb = ebp + ref[m].conj().transpose() * efp

            # Update the AR coeff.
            a.resize(len(a)+1)
            a = a + ref[m] * np.flipud(a).conjugate()

            # Update the prediction error
            E[m+1] = (1 - ref[m].conj().transpose()*ref[m]) * E[m]
            #print 'REF', ref, num, den
        return a, E[-1], ref

    def maxInds(self,X):
        max = X[0]
        inds = 0
        i = 0
        for x in X:
            if x > max:
                inds = i
                max = x
            i = i + 1
        return inds
    
    def bandsEnergy(self,X,start,end):
        start = start - 1
        sum = 0
        for x in range(start, end):
            sum = sum + (X[2*x] + X[2*x+1])**2
        return sum

    def derivative(self,X,interval=1):
        ans = []
        for i in range(1,len(X)):
            ans.append((X[i]-X[i-1])/interval)
        return ans

    def doubleDerivative(self,X,interval=1):
        ans = []
        for i in range(2,len(X)):
            ans.append((X[i-2]+X[i]-2*X[i-1])/interval**2)
        return ans
