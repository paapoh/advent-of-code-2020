file_input = open('day3input.txt').read().splitlines()

width = len(file_input[0])

# part1: move 3 right 1 down and count trees
def calcTrees(right, down=1):
    count = 0
    step = 0
    for line in file_input[::down]:
        if line[step % width] == '#':
            count += 1
        step += right
    return count

print(calcTrees(3))

#part2: move [1,3,5,7] right [1,2] down and count trees

first = calcTrees(1)
second = calcTrees(3)
third = calcTrees(5)
fourth = calcTrees(7)
fifth = calcTrees(1, 2)
print(first * second * third * fourth * fifth)
