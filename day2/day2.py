file_input = open('day2input.txt').read().splitlines()

#part 1: Count how many times a char appears in the word. Validate with the conditions
count = 0

for password in file_input:
    pwdSplit = password.split()
    pwdNum = pwdSplit[0].split('-')
    pwdChar = pwdSplit[1][0]
    pwdWord = pwdSplit[2]

    charCount = pwdWord.count(pwdChar)
    if int(pwdNum[0]) <= charCount <= int(pwdNum[1]):
        count += 1

print(count)


#part 2: Check if char is in neither of the positions but not both
count2 = 0

for password in file_input:
    pwdSplit = password.split()
    pwdNum = pwdSplit[0].split('-')
    pwdChar = pwdSplit[1][0]
    pwdWord = pwdSplit[2]
    if (pwdChar == pwdWord[int(pwdNum[0])-1]) ^ (pwdChar == pwdWord[int(pwdNum[1])-1]):
        count2 += 1

print(count2)
