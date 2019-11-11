
# pma.py LoginModelNew
# 2 states, 3 transitions, 0 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def initialize(): pass
def login(): pass
def logout(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'LoginModelNew': {'init': True, 'signedIn': False, 'signedOut': False}},
  1 : {'LoginModelNew': {'init': False, 'signedIn': False, 'signedOut': True}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = []
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (logout, (), None), 1),
  (0, (initialize, (), None), 0),
  (1, (logout, (), None), 1),
)
