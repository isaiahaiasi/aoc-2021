import re
import math


def getInput(path):
    with open(path) as fp:
        numbersText, boardsText = fp.read().split('\n', 1)
        numbers = [int(n.strip()) for n in numbersText.split(',')]
        boardsTextArr = boardsText.strip().split('\n\n')

        boards = []
        for boardText in boardsTextArr:
            board = [int(c.strip()) for c in re.split(
                '\n| ', boardText) if c.strip() != '']
            boards.append(board)
        return numbers, boards


# returns index of winning board and index of winning number
def getWinner(numbers, boards):
    # starting at i = 4, scan boards for numbers[i]
    # if match, get column & row numbers
    # if all numbers in col or row are in numbers[:i+1], WINNER!

    for callIndex in range(4, len(numbers)):
        for board in boards:
            for boardPos, boardNum in enumerate(board):
                if boardNum == numbers[callIndex]:
                    calledNums = numbers[:callIndex+1]
                    if check_winner(board, calledNums, boardPos):
                        return board, calledNums
    return -1


# which board will win last?
# - start with all numbers "called"
# - walk backwards until there's a board that ISN'T winning
def getLoser(numbers, boards):
    for i in range(len(numbers)):
        for board in boards:
            if not has_board_won(board, numbers[:len(numbers)-i]):
                return board, numbers[:len(numbers)-i+1]


def check_winner(board, calledNums, i):
    if is_subset(
        get_col(board, i), calledNums) or is_subset(
            get_row(board, i), calledNums):
        return True
    else:
        return False


def has_board_won(board, calledNums):
    for x in range(5):
        if is_subset(get_col(board, x), calledNums):
            return True
        if is_subset(get_row(board, x*5), calledNums):
            return True
    return False


def getScore(board, calledNums):
    uncalledNums = []
    for n in board:
        if n not in calledNums:
            uncalledNums.append(n)
    return sum(uncalledNums) * calledNums[-1]


def get_col(board, i):
    return [board[(i % 5) + (5 * j)] for j in range(0, 5)]


def get_row(board, i):
    return [board[(i // 5)*5 + j] for j in range(0, 5)]


# feel like this should be a builtin??
# might be if I convert to set...
def is_subset(sub, arr):
    for n in sub:
        if n not in arr:
            return False
    return True


def getResult():
    numbers, boards = getInput("input.txt")
    winBoard, calledNums = getWinner(numbers, boards)

    return getScore(winBoard, calledNums)


def getLoserResult():
    numbers, boards = getInput("input.txt")
    loseBoard, calledNums = getLoser(numbers, boards)
    return getScore(loseBoard, calledNums)


def render_board(board, calledNums):
    output = ''
    for i in range(25):
        if board[i] not in calledNums:
            output = output + pad_num(board[i], 2)
        else:
            output = output + 'xx'
        if i % 5 == 4:
            output = output + '\n'
        else:
            output = output + ' '
    print(output)


def pad_num(n, len=3):
    if n == 0:
        return '0'*len

    digits = int(math.log10(n))+1
    return '0'*(len-digits) + str(n)


if __name__ == "__main__":
    print(getLoserResult())
    # 2744 TOO LOW
    # 13912!
