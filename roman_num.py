def toRoman(num):
    letters = ["I", "V", "X", "L", "C", "D", "M"]
    nums = [1, 5, 10, 50, 100, 500, 1000]
    roman = ""
    x = 0

    # While the full number still hasn't been converted yet
    while num > 0:
        # Check all of the possible numbers for it to be in between
        for x, y in enumerate(nums):
            if y <= num < nums[x + 1] or x == len(nums) - 1:
                roman += letters[x]
                for z in range( num // y ):
                    num = num - y
                break
    return roman




print(toRoman(12))
