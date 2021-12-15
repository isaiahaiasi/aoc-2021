from math import inf
from time import time


def getcharlist(string):
    pairs = {}
    for i in range(len(string) - 1):
        k = string[i:i+2]
        if k in pairs:
            pairs[k] = pairs[k] + 1
        else:
            pairs[k] = 1
    return pairs


class Polymer:
    def __init__(self, template, rules):
        self.rules = rules
        self.pairs = getcharlist(template)

    def lightstep(self):
        # get new pairs
        newPairs = {}
        for k, v in self.pairs.items():
            if v <= 0:
                continue

            rk = self.rules[k]
            pk = self.pairs[k]

            a, b = k[0] + rk, rk + k[1]
            newPairs[a] = pk if a not in newPairs else newPairs[a] + pk
            newPairs[b] = pk if b not in newPairs else newPairs[b] + pk

        self.pairs = newPairs

    def getlightdelta(self):
        chars = {}
        for k, v in self.pairs.items():
            c1, c2 = k[0], k[1]
            chars[c1] = v if c1 not in chars else chars[c1] + v
            chars[c2] = v if c2 not in chars else chars[c2] + v
        v = chars.values()
        return max(v) - min(v)


def getinput(path):
    with open(path) as fp:
        template, rulesStr = fp.read().strip().split('\n\n')
    rlist = [k.split(' -> ') for k in rulesStr.split('\n')]
    rules = {k: v for k, v in rlist}
    return template, rules


[template, rules] = getinput('testinput.txt')
poly = Polymer(template, rules)


def teststep(polymer):
    polymer.step()
    polymer.lightstep()
    fullkeys = {k: v for k, v in sorted(getcharlist(
        poly.pm).items(), key=lambda item: item[0])}
    lightkeys = {k: v for k, v in sorted(
        poly.pairs.items(), key=lambda item: item[0]) if v > 0}

    print("full:", fullkeys)
    print("light:", lightkeys)


for i in range(10):
    poly.lightstep()
print(poly.getlightdelta() / 2)
