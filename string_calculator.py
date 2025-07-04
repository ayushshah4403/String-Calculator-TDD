def add(numbers):
    if numbers == "":
        return 0
    if "," in numbers:
        nums = numbers.split(",")
        return sum(int(num) for num in nums)
    return int(numbers)

