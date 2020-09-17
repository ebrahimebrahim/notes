                            x
                            |
                            v
training data -> learner -> f
                            |
                            v
                            y


Modeling: what f's should we consider?
Inference: when we have f, how to *compute* y given x?
Learning: how shoud the learner work?

Stochastic gradient descent:
Basically just gradient descent except you use only a sample batch of training data to compute the gradient for one step,
rather than using all of it at each step.
You can make the learning rate decrease over iterations of the algorithm.

Oh actually I guess the term "stochastic g d" is used for the situation where the batch size is 1.
Otherwise its minibatch g d, or something like that


