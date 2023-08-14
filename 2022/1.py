X = [l.strip() for l in open('/Users/soyamdas/Desktop/Advent Of Code - 2022/input1.in')]

Q = []
for elf in ('\n'.join(X)).split('\n\n'):
    q = sum(int(x) for x in elf.split('\n'))
    Q.append(q)
Q = sorted(Q)
print(Q[-1])
print(Q[-1]+Q[-2]+Q[-3])
