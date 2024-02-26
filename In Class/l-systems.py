str = 'F+'

for i in range(4):
    new = ''
    for c in str:
        if c == 'F':
            new += 'F+F'
        elif c == 'B':
            new += 'B'
        elif c == '+':
            new += 'B-'
        else:
            new += '-'
    str = new
    print(str)