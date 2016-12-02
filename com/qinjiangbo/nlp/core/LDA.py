# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   Description:
   LDA core algorithms of topic model
"""
import random
import time


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
        self.phiSum = {}
        self.numStat = 0.0
        self.thetaSum = {}
        self.run()

    # initialize the variables
    def run(self):
        self.set_V() \
            .set_ND() \
            .set_NW() \
            .set_NWSUM() \
            .set_NDSUM()

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
                self.nd[i][j] = 0.0
        return self

    def set_M(self, value=0):
        self.M = value
        return self

    def set_V(self):
        Set = set()
        for s in self.D:
            Set = Set | set(s)
        self.V = len(Set)
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
                self.phiSum[k][v] = 0.0
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
            p the distribution of the theme produced by the dictionary. if the word is T
            p(k|T) = ((number of T in theme k + beta) / (total number of words in theme k + V * beta))     --->p(T|k)
                    * ((number of theme k in document + alpha) / (total number of themes in document + K * alpha))   --->p(k|d)
        '''
        p = {}
        for k in range(self.K):
            p[k] = (self.nw[self.D[m][n]][k] + self.beta) / (self.nwSum[k] + self.V * self.beta) * (
                self.nd[m][k] + self.alpha) / (self.ndSum[m] + self.K * self.alpha)

        for k in range(1, len(p)): p[k] += p[k - 1]

        '''
            we choose the theme for the nth word in mth document
        '''
        u = random.random() * p[self.K - 1]
        for topic in range(len(p)):
            if u < p[topic]: break
        self.nw[self.D[m][n]][topic] += 1
        self.nd[m][topic] += 1
        self.nwSum[topic] += 1
        self.ndSum[m] += 1
        return topic

    # update the params
    def update_params(self):
        for m in range(len(self.D)):
            for k in range(self.K):
                '''
                    self.thetaSum[m][k] the accumulated probability value of theme k in document m
                        = the occurrences of theme k in document / total number of themes in document
                '''
                self.thetaSum[m][k] += (self.nd[m][k] + self.alpha) / (self.ndSum[m] + self.K * self.alpha)
        for k in range(self.K):
            for w in range(self.V):
                '''
                    self.phiSum[k][w] the accumulated probability value for theme-word duple
                        = the occurrences of word assigned to theme k / total number of words in theme k
                '''
                self.phiSum[k][w] += (self.nw[w][k] + self.beta) / (self.nwSum[k] + self.V * self.beta)
        '''
            self.numStat the statistic of accumulation
        '''
        self.numStat += 1

    # gibbs sampling algorithm
    def gibbs(self, alpha=2, beta=0.5):
        self.alpha = alpha
        self.beta = beta
        if self.sampleLag > 0:
            self.set_thetaSum().set_phiSum()
            self.numStat = 0.0
        self.initial_state()
        for i in range(self.maxIter):
            if i % 1000 == 0:
                print("iteration", i, time.ctime())
            for m in range(len(self.z)):
                for n in range(len(self.z[m])):
                    '''
                        self.z[m][n] here updates the distribution of nth word in mth document
                    '''
                    self.z[m][n] = self.sample_full_condition(m, n)
            '''
                self.burnIn is to ignore the some sampling results
                It is common to ignore some number of samples at the beginning (the so-called burn-in period)
                self.sampleLag is to control the update frequency
            '''
            if i > self.burnIn and self.sampleLag > 0 and i % self.sampleLag == 0:
                self.update_params()

    def get_theta(self):
        '''
        theta document-theme distribution
        :return:
        '''
        theta = {}
        for m in range(self.M):
            theta[m] = {}
            for k in range(self.K):
                theta[m][k] = 0
        if self.sampleLag > 0:
            for m in range(self.M):
                for k in range(self.K):
                    theta[m][k] = self.thetaSum[m][k] / self.numStat
        else:
            for m in range(self.M):
                for k in range(self.K):
                    theta[m][k] = (self.nd[m][k] + self.alpha) / (self.ndSum[m] + self.K * self.alpha)
        return theta

    def get_phi(self):
        '''
        phi theme-word distribution
        :return:
        '''
        phi = {}
        for k in range(self.K):
            phi[k] = {}
            for v in range(self.V):
                phi[k][v] = 0
        if self.sampleLag > 0:
            for k in range(self.K):
                for v in range(self.V):
                    phi[k][v] = self.phiSum[k][v] / self.numStat
        else:
            for k in range(self.K):
                for v in range(self.V):
                    phi[k][v] = (self.nw[k][v] + self.alpha) / (self.nwSum[k] + self.K * self.alpha)
        return phi


if "__main__" == __name__:
    documents = [
        [1, 4, 3, 2, 3, 1, 4, 3, 2, 3, 1, 4, 3, 2, 3, 6],
        [2, 2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 2],
        [1, 6, 5, 6, 0, 1, 6, 5, 6, 0, 1, 6, 5, 6, 0, 0],
        [5, 6, 6, 2, 3, 3, 6, 5, 6, 2, 2, 6, 5, 6, 6, 6, 0],
        [2, 2, 4, 4, 4, 4, 1, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 0],
        [5, 4, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2]
    ]
    lda = LDA(documents, 5)
    lda.configure(10000, 2000, 10)
    lda.gibbs()
    theta = lda.get_theta()
    print("theta:", theta)
