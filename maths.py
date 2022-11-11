def sum(lst:list|tuple):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum(lst[1:])
  
  
def average(lst:list|tuple):
    if lst:
        num_items = 0
        for i in lst:
            num_items += 1
        return sum(lst) // num_items
    else:
        return 0

def max(lst:list|tuple):
    max_value = lst[0]
    for i in lst[1:]:
        if i > max_value:
            max_value = i
    return max_value

def min(lst:list|tuple):
    min_value = lst[0]
    for i in lst[1:]:
        if i < min_value:
            min_value = i
    return min_value

def squaroot(number):
    return number ** (0.5)

def cuberoot(number):
    return number ** (1/3)

def root(root, rootnumber):
    if rootnumber != 0:
        return root ** (1//rootnumber)
    else:
        return "Error, Please enter a valid number."
        
def power(number, exponent):
    result = 1
    for i in range(exponent):
        result *= number
    return result

