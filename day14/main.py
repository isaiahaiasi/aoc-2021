from math import inf
from time import time


def getcharlist(string):
    pairs = {}
    for i in range(len(string) - 1):
        k = string[i:i+1]
        if pairs[k]:
            pairs[k] = pairs[k] + 1
        else:
            pairs[k] = 1
    return pairs


class Polymer:
    def __init__(self, template, rules):
        self.rules = rules
        self.pm = template
        self.pairs = getcharlist(template)

    def step(self):
        tmp = ''
        for i in range(len(self.pm) - 1):
            insert = self.rules[self.pm[i:i+2]]
            tmp = tmp + self.pm[i] + insert
        self.pm = tmp + self.pm[-1]

    def lightstep(self):
        # instead of dealing with the real strings
        # (which I don't need)
        # I can just track the count of each 2-char combination
        # and use that to generate the min/max chars at the end
        # { 'NN': 1, 'NC': 1, 'CB': 1 }
        # NN -> NC++, CN++, NN-- (NN -> C)
        # NC -> NB++, BC++, NC-- (NC -> B)
        # CB -> CH++, HB++, CB-- (CB -> H)
        for k, v in self.pairs.items():
            a, b = self.getaddedkeys(k)
            self.pairs[a] = self.pairs[a] + 1
            self.pairs[b] = self.pairs[b] + 1
            self.pairs[k] = self.pairs[k] - 1

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


class InputParser:
    def __init__(self, path):
        self.path = path
        with open(path) as fp:
            self.template, rulesStr = fp.read().strip().split('\n\n')
        rlist = [k.split(' -> ') for k in rulesStr.split('\n')]
        self.rules = {k: v for k, v in rlist}


inputParser = InputParser("testinput.txt")
poly = Polymer(inputParser.template, inputParser.rules)

stepct = 18
print("STEP COUNT", stepct)
start = time()

for i in range(stepct):
    poly.step()

stepend = time()
print("step cost", stepend - start)

delta = poly.getdelta()
print(delta)

deltaend = time()
print("delta cost", deltaend - stepend)
print("total cost", deltaend - start)
