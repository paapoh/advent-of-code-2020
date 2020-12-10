file_input = sorted([int(x) for x in open('input.txt').read().splitlines()])

one = 0 
two = 0
three = 1 

prev = 0

for num in file_input:
    print(num)
    if num-prev == 3:
        three += 1
    if num-prev == 2:
        two += 1
    if num-prev == 1:
        one += 1
    prev = num

print(three)
print(one * three)

def part2(lista):
    lista.insert(0,0)
    result = [1] + [0] * (len(lista)-1)
    for i in range(len(lista)):
        for j in range(i-3,i):
            if (lista[i] - lista[j]) <= 3:
                result[i] += result[j] 
    return result[-1]
print(part2(file_input))
