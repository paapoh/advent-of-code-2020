file_input = open('day7input.txt').read().splitlines()



bagdict={}

for line in file_input:
    bagColor, bags_string = line.split(' bags contain ')
    bags = bags_string.split(', ')
    testi ={}
    if bags_string[:2] != 'no':
        for bag in bags:
            bagsplit = bag.split(' ')
            num = int(bagsplit[0])
            string = bagsplit[1] + ' ' +bagsplit[2]
            testi[string] = num
    bagdict[bagColor] = testi

totuus = True
validit = ['shiny gold']

lista=[]

while totuus:
    ado = False
    for bag in bagdict:
        for ins in bagdict[bag]:
            if (ins in validit) and (bag not in lista):
                validit.append(bag)
                ado = True
                lista.append(bag)
    if not ado:
        totuus = False

print(len(validit)-1)
