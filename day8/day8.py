f = open('input.txt').read()
file_input = f.splitlines()

value = 0
used = []
i = 0

while i not in used:
    used.append(i)
    op, dirnum = file_input[i].split()
    d = dirnum[0]
    num = int(dirnum[1:])
    if op == 'nop':
        i += 1
    if op == 'acc':
        if d == '-':
            value -= num
        if d == '+':
            value += num
        i += 1
    if op == 'jmp':
        if d == '-':
            i -= num
        if d == '+':
            i += num

print(value)



for j in range(len(file_input)):
    value2 = 0
    used2 = []
    i = 0
    while i not in used2:
        used2.append(i)
        if i >= len(file_input):
            print(value2)
            quit()
        op, dirnum = file_input[i].split()
        d = dirnum[0]
        num = int(dirnum[1:])
        if 'nop' in file_input[i] and i == j:
            op = 'jmp'
        if 'jmp' in file_input[i] and i == j:
            op = 'nop'

        if op == 'nop':
            i += 1
        if op == 'acc':
            if d == '-':
                value2 -= num
            if d == '+':
                value2 += num
            i += 1
        if op == 'jmp':
            if d == '-':
                i -= num
            if d == '+':
                i += num

