file_input = open('input.txt').read()
nums = [int(x) for x in file_input.split()]

#Part 1:
faulty = 0
for i in range(25, len(nums)):
    numero = 0
    for num1 in (sorted(nums[i-25:i])):
            if num1 > nums[i]:
                break
            for num2 in (sorted(nums[i-25:i])):
                if num2 > nums[i]:
                    break
                if num1 + num2 == nums[i]:
                    numero = nums[i]
    if numero == 0:
        faulty = nums[i]
print(faulty)

#Part 2:
fst = 0
snd = 1
while True:
    lista = nums[fst:snd]
    summa = sum(lista)
    if summa < faulty:
        snd += 1
    if summa > faulty:
        fst += 1
        snd = fst+1
    if summa == faulty:
        print(max(lista) + min(lista))
        break
