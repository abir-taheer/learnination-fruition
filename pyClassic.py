def ban(num: int) -> bool:
    squared = num ** 2
    num_list = [x for x in str(squared)]
    # Iterate through all of the items in the list
    n = 0
    for x in num_list:
        beginning = num_list[:n]
        end = num_list[n:]
        first = 0 if n == 0 else int("".join(beginning))
        last = int("".join(end))
        if first + last == num:
            return True
        n = n + 1

    return False


print(ban(1))

