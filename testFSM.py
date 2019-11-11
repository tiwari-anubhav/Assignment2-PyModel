
# pma.py test
# 3 states, 4 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def PauseMusic(): pass
def PlayMusic(): pass
def InitializePlayer(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'test': {'play': False, 'pause': False}},
  1 : {'test': {'play': True, 'pause': False}},
  2 : {'test': {'play': False, 'pause': True}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [1]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (PlayMusic, (), None), 1),
  (1, (PauseMusic, (), None), 2),
  (1, (InitializePlayer, (), None), 0),
  (2, (PlayMusic, (), None), 1),
)
