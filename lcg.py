import numpy as np
class LCG:
    def __init__(self, seed = 1, Multiplier = 1366, Addend = 150889, Pmod = 714025):
        """Create an LCG instance"""
        self.multiplier = Multiplier
        self.addend = Addend
        self.pmod = Pmod
        self.setseed(seed)
    
    def setseed(self, seed):
        self.last = seed

    def random(self):
        """Return a single random number between 0 and 1"""
        self.last = (self.multiplier * self.last + self.addend) % self.pmod
        return self.last/self.pmod

    def randv(self, size = 1):
        """Return a numpy array of random numbers between 0 and 1"""
        v = np.empty(size)
        for i in range(size):
            v[i] = self.random()
        return v

lcgdef = LCG()
print(lcgdef.random())
print(lcgdef.randv(10))
