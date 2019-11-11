from LoginModel import login

testSuite = [
  # Run 1  - Valid Credentials, ends in accepting state
  [
     (login, ('anu12345@blabber.im','abc'), None),
  ],
  # Run 2  - Correct Username and Incorrect Password, ends in non-accepting state
  [
     (login, ('are','abc'), None),
  ],
  # Run 3  - Incorrect Username and Correct Password, ends in non-accepting state
  [
     (login, ('anu12345@blabber.im','xyz'), None),
  ],
  # Run 4  - Incorrect Username and Correct Password, ends in non-accepting state
  [
     (login, ('are','xyz'), None),
  ]
]