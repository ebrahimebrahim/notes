#Overview

Two views of AI:

- Intelligent agent
    - Perception
    - Robotics
    - Language
    - Knowledge
    - Reasoning
    - Learning ... capcity for learning seems to be the most important thing here, since it seems to be what unlocks all the others, for humans at least.
- AI tools


A paradigm for solving AI problems: modeling -> inference -> learning

modeling:
take complex real world situation and simplify into model
mode can have many parameters that are not known. don't fill them in yet.

inference:
ask questions of model
write algorithms solve problems at model level

learning:
the model had parameters, right? perhaps millions of them.
use data to learn the parameters

Once learning is done, you can go back and do inference using the now well-tuned model.
The concept of learning is very general.

Course plan: low level to high level intelligence throughout course:

- Reflex: fully feed-forward. e.g. linear classifiers, deep nn's
- States: e.g. search, markov decision process, adversarial games
    - search problems: you control everything, e.g. find shortest path
    - markov process: against nature; there's randomness, e.g. blackjack
    - adversarial games: against opponent, e.g. chess
- Variables: e.g. sudoku
    - constraint satisfaction
    - bayesian
- Logic: e.g. a virtual assistant
    - need to digest heterogenous info and reason deeply with it


#Optimization

discrete optimization: domain is discrete, e.g. finding an optimal path from a discrete set of possible paths
tool: _dynamic programming_
(breaking optimization problem into subproblems of the same form, and using recursion with memoization)

cts optimization: domain cts, like R^n
tool: gradient descent

