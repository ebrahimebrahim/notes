from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """
  def __init__(self):
    self.lastPositions = []
    self.dc = None


  def getAction(self, gameState):
    """
    getAction chooses among the best options according to the evaluation function.

    getAction takes a GameState and returns some Directions.X for some X in the set {North, South, West, East, Stop}
    ------------------------------------------------------------------------------
    Description of GameState and helper functions:

    A GameState specifies the full game state, including the food, capsules,
    agent configurations and score changes. In this function, the |gameState| argument
    is an object of GameState class. Following are a few of the helper methods that you
    can use to query a GameState object to gather information about the present state
    of Pac-Man, the ghosts and the maze.

    gameState.getLegalActions():
        Returns the legal actions for the agent specified. Returns Pac-Man's legal moves by default.

    gameState.generateSuccessor(agentIndex, action):
        Returns the successor state after the specified agent takes the action.
        Pac-Man is always agent 0.

    gameState.getPacmanState():
        Returns an AgentState object for pacman (in game.py)
        state.configuration.pos gives the current position
        state.direction gives the travel vector

    gameState.getGhostStates():
        Returns list of AgentState objects for the ghosts

    gameState.getNumAgents():
        Returns the total number of agents in the game

    gameState.getScore():
        Returns the score corresponding to the current state of the game


    The GameState class is defined in pacman.py and you might want to look into that for
    other helper methods, though you don't need to.
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best


    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

######################################################################################
# Problem 1b: implementing minimax

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (problem 1)
  """
  def registerInitialState(self, state):
      print("Value of initial state with depth {}: {}".format(
        self.depth,
        self.vmm(state, self.depth, self.index)
      ))

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction. Terminal states can be found by one of the following:
      pacman won, pacman lost or there are no legal moves.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game

      gameState.getScore():
        Returns the score corresponding to the current state of the game

      gameState.isWin():
        Returns True if it's a winning state

      gameState.isLose():
        Returns True if it's a losing state

      self.depth:
        The depth to which search should continue

    """

    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    actions = gameState.getLegalActions(self.index)
    for d in range(self.depth,0,-1):
      values = [ self.vmm(gameState.generateSuccessor(self.index, action), d, self.index) for action in actions ]
      max_value = max(values)
      maximizing_actions = [actions[i] for i in range(len(actions)) if values[i]==max_value]
      assert(len(maximizing_actions)>0)
      if len(maximizing_actions)==1:
        return maximizing_actions[0]
      actions = maximizing_actions
    return random.choice(actions)
    # END_YOUR_CODE

  def vmm(self, s, d, player_index):
    if s.isWin() or s.isLose():
      return s.getScore()
    if d==0:
      return self.evaluationFunction(s)
    next_player_index = (player_index + 1) % s.getNumAgents()
    if player_index==0:
      return max( self.vmm(s.generateSuccessor(player_index,action), d, next_player_index) for action in s.getLegalActions(player_index) )
    elif player_index != s.getNumAgents() - 1:
      return min( self.vmm(s.generateSuccessor(player_index,action), d, next_player_index) for action in s.getLegalActions(player_index) )
    else:
      return min( self.vmm(s.generateSuccessor(player_index,action), d-1, next_player_index) for action in s.getLegalActions(player_index) )





######################################################################################
# Problem 2a: implementing alpha-beta

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (problem 2)
  """

  def registerInitialState(self, state):
      print("Value of initial state with depth {}: {}".format(
        self.depth,
        self.vmm(state, self.depth, self.index)
      ))

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """

    # BEGIN_YOUR_CODE (our solution is 36 lines of code, but don't worry if you deviate from this)
    actions = gameState.getLegalActions(self.index)
    for d in range(self.depth,0,-1):
      values = [ self.vmm(gameState.generateSuccessor(self.index, action), d, self.index) for action in actions ]
      max_value = max(values)
      maximizing_actions = [actions[i] for i in range(len(actions)) if values[i]==max_value]
      assert(len(maximizing_actions)>0)
      if len(maximizing_actions)==1:
        return maximizing_actions[0]
      actions = maximizing_actions
    return random.choice(actions)
    # END_YOUR_CODE

  # alpha is the largest lower bound seen on a max node of an ancestor
  # beta is the smallest upper bound seen on a min node of an ancestor
  def vmm(self, s, d, player_index, alpha=float('-inf'),beta=float('inf')):
    if s.isWin() or s.isLose():
      return s.getScore()
    if d==0:
      return self.evaluationFunction(s)
    next_player_index = (player_index + 1) % s.getNumAgents()
    if player_index==0:
      max_vmm_succ = float('-inf')
      for action in s.getLegalActions(player_index):
        vmm_succ = self.vmm(s.generateSuccessor(player_index,action), d, next_player_index, alpha, beta) 
        alpha = max(alpha, vmm_succ)
        max_vmm_succ = max(max_vmm_succ, vmm_succ)
        if vmm_succ > beta : break # prune
      return max_vmm_succ
    next_d = d if player_index != s.getNumAgents() - 1 else d-1
    min_vmm_succ = float('inf')
    for action in s.getLegalActions(player_index):
      vmm_succ = self.vmm(s.generateSuccessor(player_index,action), next_d, next_player_index, alpha, beta)
      beta = min(beta, vmm_succ)
      min_vmm_succ = min(min_vmm_succ,vmm_succ)
      if vmm_succ < alpha : break # prune
    return min_vmm_succ



######################################################################################
# Problem 3b: implementing expectimax

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (problem 3)
  """

  def registerInitialState(self, state):
      print("Value of initial state with depth {}: {}".format(
        self.depth,
        self.vmm(state, self.depth, self.index)
      ))

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """

    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    actions = gameState.getLegalActions(self.index)
    for d in range(self.depth,0,-1):
      values = [ self.vmm(gameState.generateSuccessor(self.index, action), d, self.index) for action in actions ]
      max_value = max(values)
      maximizing_actions = [actions[i] for i in range(len(actions)) if values[i]==max_value]
      assert(len(maximizing_actions)>0)
      if len(maximizing_actions)==1:
        return maximizing_actions[0]
      actions = maximizing_actions
    return random.choice(actions)
    # END_YOUR_CODE

  def vmm(self, s, d, player_index):
    if s.isWin() or s.isLose():
      return s.getScore()
    if d==0:
      return self.evaluationFunction(s)
    next_player_index = (player_index + 1) % s.getNumAgents()
    if player_index==0:
      return max( self.vmm(s.generateSuccessor(player_index,action), d, next_player_index) for action in s.getLegalActions(player_index) )
    next_d = d if player_index != s.getNumAgents() - 1 else d-1
    actions = s.getLegalActions(player_index)
    return 1.0/len(actions) * sum( self.vmm(s.generateSuccessor(player_index,action), next_d, next_player_index) for action in actions )

######################################################################################
# Problem 4a (extra credit): creating a better evaluation function

def betterEvaluationFunction(s):
  """
    Your extreme, unstoppable evaluation function (problem 4).

    DESCRIPTION: <write something here so we know what you did>
  """

  # BEGIN_YOUR_CODE (our solution is 13 lines of code, but don't worry if you deviate from this)
  score = s.getScore()
  pacmanPos = s.getPacmanPosition()
  unscared_ghost_positions = []
  for g in s.getGhostStates():
    if g.scaredTimer == 0:
      unscared_ghost_positions.append(g.getPosition())
  dist_to_nearest_ghost = min(manhattanDistance(pos,pacmanPos)  for pos in unscared_ghost_positions) if unscared_ghost_positions else 99999
  dist_to_nearest_food = min(manhattanDistance(pos,pacmanPos)  for pos in s.getFood().asList())
  ghosts_not_scared = all(g.scaredTimer == 0 for g in s.getGhostStates())
  return score + (-30)*1/dist_to_nearest_ghost + (-0.1)*dist_to_nearest_food
  # END_YOUR_CODE

# Abbreviation
better = betterEvaluationFunction
