from statistics import median

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_key = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def get_input(path):
    with open(path) as fp:
        return fp.read().split('\n')


def get_score(input):
    score = 0
    score2_list = []
    for line in input:
        stack = []
        corrupted = False
        for c in line:
            # non-closing c, push to stack
            if c in pairs:
                stack.append(c)
            # closing c is valid, pop off stack
            elif pairs[stack[-1]] == c:
                stack.pop()
            # closing c is invalid, set score and break
            else:
                score = score + score_key[c]
                corrupted = True
                break
            pass

        if not corrupted:
            sub_complete_score = 0
            for i in range(len(stack))[::-1]:
                c_val = ['(', '[', '{', '<'].index(stack[i]) + 1
                sub_complete_score = (sub_complete_score * 5) + c_val
                pass
            score2_list.append(sub_complete_score)
            print(sub_complete_score)
            pass
        pass
    return median(score2_list)


if __name__ == "__main__":
    input = get_input("input.txt")
    score_key = get_score(input)
    print("final", score_key)
