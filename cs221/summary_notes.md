# CS221 Summary notes

Low to high level intelligence:
- reflex (linear classifiers, deep nn's)
- state (search, MDP, games)
- variable (CSP, bayesian nets)
- logic

*Dynamic programming*: breaking optimization problem into subproblems of the same form, and using recursion with memoization

*Stochastic gradient descent*:
Basically just gradient descent except you use only one training data point to compute the gradient for one step,
rather than using all of it at each step.
You can make the learning rate decrease over iterations of the algorithm.
Minibatch gradient descent sits in between stochastic and non-stochastic gradient descent.

## Feature extraction

A good way to view it is in terms of *feature templates*.
These are like feature descriptions with "blanks"; filling in the blanks in different ways
creates a group of features that are all computed in the same way.

Consider the *hypothesis class* induced by your choice of feature extractor.
This is the set of predictor functions that are possible given a feature extractor.

Even linear classifiers can produce crazy nonlinear decision boundaries, if the feature extractor is chosen to allow it.

Think about how features *scale*.
Does it make sense for prediction to be linear in a particular feature?
Maybe it should be quadratic, so throw in the square of the feature as a new feature.
Maybe it should be discretized into multiple binary features for different ranges.



## Classification and Regression


|                       | classification               | regression           |
|-----------------------|------------------------------|----------------------|
| predictor             | sign(score) = sign(w.phi(x)) | score = w . phi(x)   |
| relation to correct y | margin = score\*y            | residual = score - y |
| loss function         | 0-1, hinge, logistic         | L2 or L1             |


`hinge_loss(margin) = max(0, 1-margin)`






## Neural networks

Strung together linear predictors with activation functions at the end of each layer.

Each layer solves a bunch of sub-problems.
You can think of it as though each layer is a feature extractor for the next.

Taking gradient of loss function can be done in a systematic way as follows:

- Create computation graph for expression, where nodes are building blocks like `+` and `*` and `sum`, etc.
- Label edges with partial derivatives of the building blocks wrt their inputs.
- Observe that the chain rule is now simply multiplication of edges along paths. In other words if you want to know the deriv of one node value wrt one of its descendents, just multiply edge values along the path joining them.
- Define forward values, `f_i`s, to be the values on the nodes-- i.e. the values of subexpressions. Define backward values, `g_i`s, to be the derivatives of the output wrt `f_i`s -- i.e. how changing that node influces the root.
- Backpropagation algorithm:
  - Forward pass: Compute each `f_i`, leaves to root. So basically just compute the top level expression and make sure to remember the values of all subexpressions along the way
  - Backward pass: Compute each `g_i`, root to leaves. This is just a matter of traveling down paths to the nodes you're interested in taking a deriv wrt, and along the way multiplying the derivative expressions that you labeled on edges, which you can now compute because you have all the `f_i`s in place.

## Nearest neighbors

Store *entire* training data set.
Given a new input, find the data point closest to it and return the associated output as your prediction.


## Learning

*estimation error* is the difference between the predictor your learning algorithm can create from the given data
and the best possible predictor in the hypothesis class.

*approximation error* is the difference between the best possible predictor in the hypothesis class
and the ground truth.


Model complexity tradeoff:

- small hypothesis class leads to high approx. error, but easy to get learning algorithm to have low est. error.
- large hypothesis class leads to smaller approx. error but more difficulty getting a learning algorithm that doesn't have high est. error

Control model complexity by e.g.:

- controlling dimensionality of feature space by adding or removing features
- contolling norm of weights: regularization, early stopping

Workflow:

- Split data into train, val, test sets
- Look at data to get intuition
- Repeat the following:
  - implement features or tune hyperparameters
  - run learning algorithm
  - sanity check training and validation errors and weights
  - look at errors to brainstorm improvements
- Run on test set to get final error rates

## K-means clustering

Fix a number of clusters K.
The goal is to map data points to cluster labels 1,...,K.
Each cluster will have an associated centroid.
So there are two things we'd like to learn from the data here:

- the assignment of data points to clusters
- the locations of centroids

K means loss:
sum over the data points of the squared distance between data points and the centroid of their associated cluster.

- Fixing the cluster assignment, it's easy to choose centroids to minimize the loss: just take means of clusters.
- Fixing the centroids, it's easy to find the best cluster assignment to minimize the loss: just assign each point to
the cluster whose centroid is nearest.

K-means algorithm:
attemp to optimize jointly by initializing centroids randomly, and then
alternating in choosing the best cluster assignments and the best centroids.
Continue until convergence.



## Search Problems - Inference

A _search problem_ consists of

- a set `States` whose elements are called states, and a set `Actions` whose elements are called actions
- a start state
- a function `Actions(s)` that assigns to each state a set of actions.
- a function `Cost(s,a)` that assigns to each state `s` and action `a` in `Actions(s)` a real number cost.
- a function `Succ(s,a)` that assigns to each state `s` and action `a` in `Actions(s)` a successor state.
- a function `IsEnd(s)` that tells us whether a given state is a goal state.

So it's pretty much just a directed graph with weights on the edges, a labeled start node, and labeled goal nodes.

Directly doing a breadth-first or depth-first search is not that great and
can unncessarily expand the digraph into a tree.
Instead, one can use dynamic programming to avoid this.
But if the digraph has cycles then you can get an infinte recursion loop this way.
_Uniform cost search_ (aka Dijkstra's algorithm) will be able to handle that:

- start with all states in set `unexplored` except for the start states, which is the only element of the priority queue `frontier`
- repeat the following till `frontier` is empty:
  - pop off the top of `frontier` (i.e. the lowest priority element; priority here represents cost to get to state from start, the lowest cost found so far). call the state you just popped `s`, and call its priority `p`.
  - if `IsEnd(s)` then stop and return solution (see comment below)
  - add `s` to set `explored`
  - for each `a` in `Actions(s)`:
    - get successor `s'=Succ(s,a)`
    - if `s'` is in `explored`, continue (skip this iteration)
    - update `frontier` with `s'` and priority being `p + Cost(s,a)` (this means that if `s'` was already in frontier then its new priority shall be the min of its old priority and `p + Cost(s,a)`)

About returning solution: I've omitted in this description the details of keeping track of the optimal path found to
reach a state. You can do this by keeping backpointers from states you've explored to the states that precede them in the optimal path to them.


Uniform cost search requires costs to be nonnegative in order to be correct.

TODO: Astar stuff [N1- 84, 85, 86]

## Search Problems - Learning

TODO: structured perceptron [N1- 83,84]


## Markov Decision Processes

TODO: start from [N1 -89]
