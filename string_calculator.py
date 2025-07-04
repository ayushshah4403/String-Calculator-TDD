def add(numbers):
    if numbers == "":
        return 0
    delimiters = [",", "\n"]
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, " ")
    nums = numbers.split()
    return sum(int(num) for num in nums)

