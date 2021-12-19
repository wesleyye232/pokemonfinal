key = 'got'

print({'already' : (lambda: 2+2),
 'got' : (lambda:2 * 4),
 'one' : (lambda:2 ** 6)}[key]())

action = (lambda x: (lambda y: x+y))
act = action (99)
act (3)
#102
((lambda x:(lambda y:x+y))(99))(4)
#103
