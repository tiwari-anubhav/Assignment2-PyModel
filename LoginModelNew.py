"""
Pix Art Messenger
"""

### Model

# State

init = True
signedOut = False
signedIn = False

# Init application variables with default value
username = "anu12345@blabber.im"
password = "abc"

# Actions

def initialize():
  global signedOut, signedIn,init
  signedOut = False
  signedIn = False
  init = True

def login(user,passw):
  global init, signedIn,signedOut
  if user == username and passw == password:
    signedIn = True
    init = False
    signedOut = False
  else:
    signedIn = False
    init = False
    signedOut = True

def logout():
  global signedOut, signedIn,init
  if (signedIn):
    signedOut = True
    init = False
    signedIn = False
  else:
    signedOut = True
    signedIn = False
    init = False



def initialize_enabled():
  return not signedIn and not signedOut

def login_enabled():
  return signedIn

def logout_enabled():
  return not signedIn


def Accepting():
    return not init and not signedOut


state = ('signedIn','signedOut','init')

actions = (initialize, login, logout,)
enablers = {initialize:(initialize_enabled,), login:(login_enabled,), logout:(logout_enabled,), }
domain = {login:{'user':username,'passw':password}}

def Reset():
  global signedOut, signedIn,init
  signedOut = False
  signedIn = False
  init = True