"""
Pix Art Messenger
"""

### Model

# State
signedOut = False
signedIn = False

# Init application variables with default value
username = "anu12345@blabber.im"
password = "abc"

# Actions

def initialize():
  global signedOut, signedIn
  signedOut = False
  signedIn = False

def login(user,passw):
  global signedOut, signedIn
  if user == username and passw == password:
    signedIn = True
    signedOut = False
  else:
    signedIn = False
    signedOut = True

def logout():
  global signedOut, signedIn
  signedOut = True
  signedIn = False

def initialize_enabled():
  return not signedIn

def login_enabled():
  return signedIn

def logout_enabled():
  return not signedIn

def Accepting():
    return not signedOut


state = ('signedIn','signedOut')

actions = (initialize, login, logout)
enablers = {initialize:(initialize_enabled,), login:(login_enabled,), logout:(logout_enabled,) }
domain = {login:{'user':username,'passw':password}}

def Reset():
  global signedOut, signedIn
  signedOut = False
  signedIn = False