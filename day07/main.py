# [16,1,2,0,4,2,7,1,2,14] -> [2, 2, ... ] consuming least "fuel"

# PART 1
# 1 fuel = 1 int; eg, 16 -> 2 = 14 fuel

# PART 2
# fuel cost = n pos => 1 + 2 + ... + n fuel; eg 16 -> 2 = 66 fuel

# find the position which would cost the least fuel to align every index to
# HOW MUCH FUEL WOULD IT COST?

from statistics import median


def get_input(path):
    with open(path, "r") as fp:
        text = fp.read()
        return [int(c.strip()) for c in text.strip().split(',')]


def get_old_optimal_pos(arr):
    return round(median(arr))


def get_old_fuel_cost(arr, pos):
    return sum([abs(n - pos) for n in arr])


# BRUTE FORCE :(
# for each possible position, find the cost
# return the position with the lowest cost
def naive_get_optimal_fuel_cost(arr):
    arrmin = min(arr)
    arrmax = max(arr)
    costs = []
    for n in range(arrmax + 1):
        costs.append(get_total_fuel_cost(arr, n + arrmin))
    return min(costs) + arrmin


def get_fuel_cost(a, b):
    return sum(range(abs(a - b) + 1))


def get_total_fuel_cost(arr, pos):
    costs = [get_fuel_cost(n, pos) for n in arr]
    return sum(costs)


def do_main():
    input = get_input("input/true.txt")
    cost = naive_get_optimal_fuel_cost(input)
    print(cost)


if __name__ == "__main__":
    do_main()

    # 104149135 TOO HIGH
    # 104149091... I WAS SO CLOSE THE FIRST TIME WTF T_T
