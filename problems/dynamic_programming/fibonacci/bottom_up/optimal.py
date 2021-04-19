

def fib_forward_facing(n: int):  # Forward facing
    table = [0 for _ in range(n + 1)]
    table[1] = 1
    for i in range(len(table)):
        tabulate_forward_values(table, i)
    return table[-1]


def tabulate_forward_values(table: list, i: int):  # Forward facing
    if i + 2 < len(table):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    elif i + 1 < len(table):
        table[i + 1] += table[i]


def fib_backwards_facing(n: int) -> int:
    table = [0 for _ in range(n + 1)]
    table[1] = 1
    for i in range(2, n + 1):
        tabulate_previous_values(table, i)
    return table[-1]


def tabulate_previous_values(table: list, i: int):
    table[i] += table[i - 1] + table[i - 2]


if __name__ == '__main__':
    print(fib_forward_facing(6))
    print(fib_forward_facing(42))
    print(fib_forward_facing(3000))

    print(fib_backwards_facing(6))
    print(fib_backwards_facing(42))
    print(fib_backwards_facing(3000))
