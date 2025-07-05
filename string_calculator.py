import re

_call_count_ = 0

def add(numbers):
    global _call_count_
    _call_count_ += 1
    if numbers == "":
        return 0
    delimiters = [",", "\n"]
    
    #Check custom delimiters
    if numbers.startswith("//"):
        delimiter_part, numbers = numbers.split("\n", 1)
        custom = delimiter_part[2:]
        
        #Check for long delimiter
        
        if custom.startswith("[") and custom.endswith("]"):
            long_delimiter = custom[1:-1]
            delimiters.append(long_delimiter)
        else:
            delimiters.append(custom)
        
    delimiter_regex = "|".join(map(re.escape, delimiters))
    num_list = [int(n) for n in re.split(delimiter_regex, numbers)]
    
   #Handling negatives 
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise Exception(f"Negatives not allowed: {','.join(map(str, negatives))}")
    
    return sum(num for num in num_list if num <= 1000)

def get_call_count():
    return _call_count_