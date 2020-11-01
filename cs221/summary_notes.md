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

A good way to it is in terms of *feature templates*.
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


