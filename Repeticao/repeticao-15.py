""" Sequência de Fibonacci
    f1 -> f2 -> f1 -> f2 -> f1
    0      1     1     2    3 """

f1 = 0
f2 = 1
f3 = 0
print ("{} -> {} -> ".format(f1, f2), end='')

while f2 < 100:
    
    f3 = f1 + f2
    print ("{} -> ".format(f3), end='')
    f1 = f2
    f2 = f3