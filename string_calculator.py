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
        
    nums = numbers.split()
    return sum(int(num) for num in nums)

