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
        self.pm = template
        self.pairs = getcharlist(template)
        self.stepct = 0
        self.lightstepct = 0

    def step(self):
        tmp = ''
        for i in range(len(self.pm) - 1):
            insert = self.rules[self.pm[i:i+2]]
            tmp = tmp + self.pm[i] + insert
        self.pm = tmp + self.pm[-1]
        self.stepct = self.stepct + 1

    def lightstep(self):
        # instead of dealing with the real strings
        # (which I don't need)
        # I can just track the count of each 2-char combination
        # and use that to generate the min/max chars at the end
        # { 'NN': 1, 'NC': 1, 'CB': 1 }
        # NN -> NC++, CN++, NN-- (NN -> C)
        # NC -> NB++, BC++, NC-- (NC -> B)
        # CB -> CH++, HB++, CB-- (CB -> H)

        # get new pairs
        newPairs = {}
        for k, v in self.pairs.items():
            if v <= 0:
                continue
            a, b = self.getaddedkeys(k)
            pk = self.pairs[k]
            newPairs[a] = pk if a not in newPairs else newPairs[a] + pk
            newPairs[b] = pk if b not in newPairs else newPairs[b] + pk
            newPairs[k] = -pk if k not in newPairs else newPairs[k] - pk

        # merge newPairs into self.pairs
        for k in newPairs:
            if k in self.pairs:
                self.pairs[k] = self.pairs[k] + newPairs[k]
            else:
                self.pairs[k] = newPairs[k]

        self.lightstepct = self.lightstepct + 1

    def getaddedkeys(self, key):
        c = self.rules[key]
        return key[0] + c, c + key[1]

    def getdelta(self):
        # get dict of each char in pm, with its number of occurances
        chars = {}
        for ch in self.pm:
            if ch in chars:
                chars[ch] = chars[ch] + 1
            else:
                chars[ch] = 1

        return max(chars.values()) - min(chars.values())

    def getlightdelta(self):
        chars = {}
        for k, v in self.pairs.items():
            c1, c2 = k[0], k[1]
            chars[c1] = v if c1 not in chars else chars[c1] + v
            chars[c2] = v if c2 not in chars else chars[c2] + v
        v = chars.values()
        return max(v) - min(v)


class InputParser:
    def __init__(self, path):
        self.path = path
        with open(path) as fp:
            self.template, rulesStr = fp.read().strip().split('\n\n')
        rlist = [k.split(' -> ') for k in rulesStr.split('\n')]
        self.rules = {k: v for k, v in rlist}


inputParser = InputParser("input.txt")
poly = Polymer(inputParser.template, inputParser.rules)


def teststep(polymer):
    polymer.step()
    polymer.lightstep()
    fullkeys = {k: v for k, v in sorted(getcharlist(
        poly.pm).items(), key=lambda item: item[0])}
    lightkeys = {k: v for k, v in sorted(
        poly.pairs.items(), key=lambda item: item[0]) if v > 0}

    print("full:", fullkeys)
    print("light:", lightkeys)


for i in range(40):
    poly.lightstep()
print(poly.getlightdelta() / 2)

# 2967977072189 TOO HIGH
