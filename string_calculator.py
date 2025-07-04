def add(numbers):
    if numbers == "":
        return 0
    delimiters = [",", "\n"]
    
    #Check custom delimiters
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        custom_delimiter = parts[0][2:]
        delimiters.append(custom_delimiter)
        numbers = parts[1]
    
    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, " ")
        
    nums = [int(num) for num in numbers.split()]
    
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
    
    return sum(nums)

