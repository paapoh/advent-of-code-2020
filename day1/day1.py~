file_input = [int(x) for x in open('day1input.txt').read().splitlines()]

#part 1: Find two numbers which sum up to 2020 and multiply them.
for num in file_input:
    if 2020-num in file_input:
        print((2020-num) * num)
        break

#part 2: Find three numbers which sum up to 2020 and multiply them.
for num in file_input:
    for num2 in file_input:
        for num3 in file_input:
            if num+num2+num3 == 2020:
                print(num*num2*num3)
                break
        else:
            continue
        break
    else:
        continue
    break
#O(n^3) Yikes
