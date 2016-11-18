# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   Description:
   LDA core algorithms of topic model
"""
import random


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

    # initial state of the model
    def initial_state(self):
        for m in range(self.M):
            '''
                N represents the number of words in current document
            '''
            N = len(self.D[m])
            self.z[m] = []
            for n in range(N):
                topic = int(random.random() * self.K)
                '''
                    self.z records the topic distribution of each document,
                    at initial state, they are random
                '''
                self.z[m].append(topic)
                '''
                    self.nw is relevant word-topic matrix, but here, it
                    records the occurrences of each term in this topic
                '''
                self.nw[self.D[m][n]][topic] = self.nw[self.D[m][n]].get(topic, 0) + 1
                '''
                    self.nd is relevant document-topic matrix, here it is also
                    the occurrences of the topic
                '''
                self.nd[m][topic] = self.nd[m].get(topic, 0) + 1
                '''
                    self.nwSum is total number of words under each topic
                '''
                self.nwSum[topic] = self.nwSum.get(topic, 0) + 1
                n += 1
            '''
                self.ndSum is total number of words in each document
            '''
            self.ndSum[m] = N
            m += 1

    # sample the corpus
    def sample_full_condition(self, m, n):
        '''
        :param m: number of document
        :param n: place of document
        :param self.D[m][n]: number of term
        '''
        topic = self.z[m][n]
        '''
            -1 the four -1s here are mainly used to remove the affection
            of the term itself
        '''
        self.nw[self.D[m][n]][topic] -= 1
        self.nd[m][topic] -= 1
        self.nwSum[topic] -= 1
        self.ndSum[topic] -= 1
        '''
            p the
        '''

    # gibbs sampling algorithm
    def gibbs(self, alpha=2, beta=0.5):
        self.alpha = alpha
        self.beta = beta
        if self.sampleLag > 0:
            self.set_thetaSum().set_phiSum()
            self.numStat = 0.0
