"""
Timber Music Player App
"""

### Model

# State

play = False
pause = False

# Actions

def InitializePlayer():
    global play, pause
    play = False
    pause = False

def PlayMusic():
  global play, pause
  play = True
  pause = False

def PauseMusic():
    global play, pause
    play = False
    pause = True

def InitializeEnabled():
    return play

def PlayEnabled():
  return not play

def PauseEnabled():
  return play

def Accepting():
    return play
### Metadata

state = ('play','pause')

actions = (InitializePlayer, PlayMusic, PauseMusic)
enablers = {InitializePlayer:(InitializeEnabled,), PlayMusic:(PlayEnabled,), PauseMusic:(PauseEnabled,) }
cleanup = (PauseMusic,)

# needed for multiple test runs in one session

def Reset():
  global play, pause
  play = False
  pause = False