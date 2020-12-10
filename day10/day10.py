file_input = [int(x) for x in open('input.txt').read().splitlines()]

one = 0 
two = 0
three = 1 

prev = 0

for num in sorted(file_input):
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

