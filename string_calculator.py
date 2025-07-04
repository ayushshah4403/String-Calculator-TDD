def add(numbers):
    if numbers == "":
        return 0
    if "," in numbers:
        nums = numbers.split(",")
        return int(nums[0]) + int(nums[1])
    return int(numbers)

