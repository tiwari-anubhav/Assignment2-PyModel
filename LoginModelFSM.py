
# pma.py LoginModel
# 2 states, 4 transitions, 1 accepting states, 0 unsafe states, 0 finished and 0 deadend states

# actions here are just labels, but must be symbols with __name__ attribute

def initialize(): pass
def login(): pass
def logout(): pass

# states, key of each state here is its number in graph etc. below

states = {
  0 : {'LoginModel': {'init':True,'signedIn': False, 'signedOut': False}},
  1 : {'LoginModel': {'init':False,'signedIn': False, 'signedOut': True}},
  2 : {'LoginModel': {'init':False,'signedIn': True, 'signedOut': True}},
}

# initial state, accepting states, unsafe states, frontier states, deadend states

initial = 0
accepting = [2]
unsafe = []
frontier = []
finished = []
deadend = []
runstarts = [0]

# finite state machine, list of tuples: (current, (action, args, result), next)

graph = (
  (0, (initialize, (), None), 1),
  (1, (login, (), None), 2),
  (2, (logout, (), None), 1),
  (1, (logout, (), None), 1),
)
