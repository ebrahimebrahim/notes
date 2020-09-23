#!/usr/bin/python

import random
import collections
import math
import sys
from util import *

############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    words = x.split()
    return {word:len(list(filter(lambda w:w==word,words))) for word in words}
    # END_YOUR_CODE

############################################################
# Problem 3b: stochastic gradient descent

import numpy as np

def scl(s,v):
    """return s*v where is a scalar and v is a sparse vector"""
    return {key:s*val for key,val in v.items()}

def learnPredictor(trainExamples, testExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    '''
    weights = {}  # feature => weight
    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    def loss_hinge(x,y,w):
        return max(0,1-y * dotProduct(w,x))

    def ave_loss(data,w):
        return np.array([loss_hinge(x,y,w) for x,y in data]).mean()

    def error_rate(data,w):
        return sum(int(dotProduct(w,x)*y <= 0) for x,y in data)/float(len(data))

    def loss_hinge_grad(x,y,w):
        if 1 - (y*dotProduct(w,x)) <= 0 : return scl(0,x)
        else: return scl(-y,x)

    trainExamplesF = np.array([[featureExtractor(x),y] for x,y in trainExamples])
    testExamplesF = np.array([[featureExtractor(x),y] for x,y in testExamples])

    for i in range(numIters):
        print("Iteration {}:\n\tTraining loss:\t{}\n\tTest loss:\t{}\n\tTraining error rate:\t{}\n\tTest error rate:\t{}".format(
            i,
            ave_loss(trainExamplesF,weights),
            ave_loss(testExamplesF,weights),
            error_rate(trainExamplesF,weights),
            error_rate(testExamplesF,weights)
        ))
        for x,y in trainExamplesF:
            increment(weights,-eta,loss_hinge_grad(x,y,weights))
    # END_YOUR_CODE
    return weights

############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        keys = random.sample(weights.keys(),random.randint(1,len(weights.keys())))
        phi = {k:abs(int(random.gauss(0,2)))+1 for k in keys}
        y = 1 if dotProduct(weights,phi) > 0 else -1
        # END_YOUR_CODE
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 3e: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        x_nospace = ''.join(c for c in x if c not in [' ','\t'])
        w = {}
        for i in range(len(x_nospace)-(n-1)):
            if x_nospace[i:i+n] in w.keys():
                w[x_nospace[i:i+n]] += 1
            else:
                w[x_nospace[i:i+n]] = 1
        return w
        # END_YOUR_CODE
    return extract

############################################################
# Problem 4: k-means
############################################################


def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (our solution is 25 lines of code, but don't worry if you deviate from this)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE
