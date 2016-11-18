# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   Description:
   LDA core algorithms of topic model
"""


class LDA(object):
    # declaration for parameters in LDA topic model
    def __init__(self, data, k=20):
        self.D = data  # input the data
        self.K = k
        self.V = 0  # the number of terms in dict
        self.M = len(self.D)
        self.alpha = 2
        self.beta = 0.5
        self.maxIter = 1000
        self.burnIn = 100
        self.sampleLag = 20
        self.nw = {}  # number of instances of word i(term) assigned to topic j
        self.nd = {}  # number of words in document i assigned to topic j
        self.nwSum = {}  # total number of words assigned to topic j
        self.ndSum = {}  # total number of words in document i
        self.z = {}  # topic assignments for each word
        self.phiSum = 0
        self.numStat = 0.0
        self.thetaSum = {}
        self.run()

    # initialize the variables
    def run(self):
        pass

    def set_NDSUM(self):
        for i in range(self.M):
            self.ndSum[i] = 0.0
        return self

    def set_NWSUM(self):
        for i in range(self.K):
            self.nwSum[i] = 0.0
        return self

    def set_NW(self):
        for i in range(self.V):
            self.nw[i] = {}
            for j in range(self.K):
                self.nw[i][j] = 0.0
        return self

    def set_ND(self):
        for i in range(self.M):
            self.nd[i] = {}
            for j in range(self.K):
                self.nw[i][j] = 0.0
        return self

    def set_M(self, value=0):
        self.M = value
        return self

    def set_V(self):
        Set = set()
        for s in self.D:
            Set = Set | set(s)
        self.V = len(Set)
        print("self.V=%s" % self.V)
        return self

    def set_K(self, value):
        self.K = value
        return self

    def set_alpha(self, value):
        self.alpha = value
        return self

    def set_beta(self, value):
        self.beta = value
        return self

    def configure(self, iterations, burnIn, sampleLag):
        self.maxIter = iterations
        self.burnIn = burnIn
        self.sampleLag = sampleLag

    def set_thetaSum(self):
        for m in range(self.M):
            self.thetaSum[m] = {}
            for j in range(self.K):
                self.thetaSum[m][j] = 0.0
        return self

    def set_phiSum(self):
        for k in range(self.K):
            self.phiSum[k] = {}
            for v in range(self.V):
                self.thetaSum[k][v] = 0.0
        return self

    # gibbs sampling algorithm
    def gibbs(self, alpha=2, beta=0.5):
        self.alpha = alpha
        self.beta = beta
        if self.sampleLag > 0:
            self.set_thetaSum().set_phiSum()
            self.numStat = 0.0
