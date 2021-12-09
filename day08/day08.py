from time import time

# any given string has 1-3 numbers it could be based on its length:
# len 2, 3, 4, 7 -> each can only be ONE number
# len 5, 6 -> each could be 3 possible numbers

#  AAAA
# B    C
# B    C
#  DDDD
# E    F
# E    F
#  GGGG

# cdfbe = [2, 3, 5]
# compare to known numbers, see if number overlapping is possible?
# eg, ab:cdfbe = 1
# comp. canonical: CF:ACDEG(2)=1; CF:ACDFG(3)=2; CF:ABDFG(5):1
# therefore, we can eliminate 3, leaving [2, 5]
# next, eafb:cdfbe = 3
# comp. canonical: BCDF:ACDEG(2)=2, BCDF:ABDFG(5)=3
# therefore, we can eliminate 2, leaving [5]
# since len of possible nums is 1, we can add it to the list of known strings

# map string to number by length
# compare unique string sets to each-other, knowing which overlap
# (caps: canonical)
canonical = ['ABCEFG', 'CF', 'ACDEG', 'ACDFG', 'BCDF',
             'ABDFG', 'ABDEFG', 'ACF', 'ABCDEFG', 'ABCDFG']


def count_overlap(a, b):
    n = 0
    shorter, longer = [a, b] if len(a) < len(b) else [b, a]
    for c in shorter:
        if c in longer:
            n = n + 1
    return n


def get_possible(num):
    possible = []
    for i in range(len(canonical)):
        if len(num) == len(canonical[i]):
            possible.append(i)
    return possible


# mutates possible array
# eg:
# num = cdfbe
# possible_nums = [2, 3, 5]
# known_sequences = [[1, "ab"], [4, "eafb"], [7, "dab"], [8, "acedgfb"]]
# (8 isn't gonna be very helpful, huh?...)
# returns True if only one value left, otherwise false
def eliminate_by_overlap(num, possible_nums, known_sequences):
    for known in known_sequences:
        # say num is "cdfbe", and possible_nums are [2, 3, 5]
        # if known is [1, "ab"],
        overlap = count_overlap(num, known[1])
        for pos_num in possible_nums:
            c_overlap = count_overlap(canonical[pos_num], canonical[known[0]])
            if c_overlap != overlap:
                # this num is proven impossible, so it's eliminated
                possible_nums = [n for n in possible_nums if n != pos_num]
                if len(possible_nums) == 1:
                    return possible_nums[0]
    return -1


# line = { digits, output }
def get_nums(line):
    known_sequences = []
    for n in line['digits']:
        num = get_num(n)
        if num >= 0:
            known_sequences.append([num, n])
    for n in line['digits']:
        # don't check ones that are already known...
        if n in [i[1] for i in known_sequences]:
            continue

        possible_nums = get_possible(n)
        eliminated = eliminate_by_overlap(n, possible_nums, known_sequences)
        if eliminated != -1:
            known_sequences.append([eliminated, n])
        else:
            print("huh???", possible_nums)
    return known_sequences


def get_num(numstr):
    numlen = len(numstr)
    if numlen == 2:
        return 1
    if numlen == 3:
        return 7
    if numlen == 4:
        return 4
    if numlen == 7:
        return 8
    return -1


def parse_input(path):
    input = []
    with open(path) as fp:
        for line in fp.read().split('\n'):
            digstr, outstr = [seg.strip() for seg in line.split('|')]
            input.append({'digits': digstr.split(' '),
                         'output': outstr.split(' ')})
    return input


def count_unique(input):
    count = 0
    for line in input:
        for num in line['output']:
            for i in [2, 3, 4, 7]:
                if len(num) == i:
                    count = count + 1
    return count


if __name__ == "__main__":
    input = parse_input("input.txt")
    start = time()
    total = 0
    for line in input:
        numstr = ''
        assoc = get_nums(line)
        for num in line['output']:
            for n in assoc:
                same_size = len(num) == len(n[1])
                same_chars = count_overlap(num, n[1]) == len(num)
                if same_size and same_chars:
                    numstr = numstr + str(n[0])
        print(numstr)
        total = total + int(numstr)
    end = time()
    print("time", end - start)
    print(total)
