ret = open('day7input.txt').read().splitlines()
bagdict={}

for line in ret:
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

perkeleen_kultanen = "shiny gold"
on_olemassa = {}
for k, v in bagdict.items():
    on_olemassa[k] = []
    try:
        for kk, vv in v.items():
            on_olemassa[k]+=[kk]*int(vv)
    except:
        pass
c=0

def perkele(current_bag):
    if current_bag==" " or on_olemassa.get(current_bag) is None:
        return 0
    nyky = len(on_olemassa[current_bag])
    nykyset = []
    for k in on_olemassa[current_bag]:
        nykyset.append(perkele(k))
    return sum(nykyset)+nyky
print(perkele('shiny gold'))