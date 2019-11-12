import numpy as np


class fir(object):
    def __init__(self, taps, f1, f2, filter_type):

        self.w = self.window_hamming(taps)

        if filter_type == 'low_pass':
            h = self.lowPass_coefficient(taps, f1)

        elif filter_type == 'band_pass':
            h = self.bandPass_coefficient(taps, f1, f2)

        else:
            raise Exception ("Need to specify type of filter")


        self.h = np.empty(len(h))
        self.samples = np.empty(taps)

        for i in range(taps):
             self.h[i] = h[i] * self.w[i]

        self.taps = taps
        self.idx = 0

    def sinc(self, x):
        if x == 0:
            return 1
        else:
            return np.sin(np.pi * x) / (np.pi * x)

    def lowPass_coefficient(self, taps, f):

        n = np.zeros(taps)

        for i in range(taps):
            n[i] = i - (taps // 2)
        
        h = np.zeros(taps)

        for i in range(taps):
            h[i] = 2.0 * f * self.sinc(2.0 * f * n[i])
        
        return h

    def bandPass_coefficient(self, taps, f1, f2):

        n = np.zeros(taps)
        h = np.zeros(taps) 
        for i in range(taps):
            n[i] = i - int(taps/2)

        for i in range(taps):
            h[i] = 2.0*f1*self.sinc(2.0*f1*n[i]) - 2.0*f2*self.sinc(2.0*f2*n[i])
 
        return h

    def window_hamming(self, taps):

        w = np.empty(taps)
        alpha = 0.54
        beta = 0.46
        for i in range(taps):
            w[i] = alpha - beta * np.cos(2.0 * np.pi * i / (taps - 1))

        return w

    def filter(self, sample):

        self.samples[self.idx] = sample

        result = 0.0
        
        for i in range(self.taps):
            index = (self.idx + i) % self.taps
            result += self.samples[index] * self.h[i]

        self.idx = (self.idx + 1) % self.taps

        return result

    def getCoefficients(self):
        return self.h