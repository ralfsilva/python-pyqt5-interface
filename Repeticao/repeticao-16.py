print ('-'*30)
print ('Sequência de Fibonacci')
print ('-'*30)

t1 = t3 = 0
t2 = 1

print ('-'*30)
print ('{} -> {}'.format(t1, t2), end='')

while t3 < 377:
    t3 = t1 + t2
    print (' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    
print (' -> FIM!')