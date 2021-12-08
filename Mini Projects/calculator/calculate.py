import math

print([ m for m in dir(math) if not m.startswith('__')])

all = [ m for m in dir(math) if not m.startswith('__')]
trigo = all[0:7] + all[10:12] + all[50:52] + all[53:55]
print(trigo)