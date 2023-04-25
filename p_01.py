#! /usr/bin/python3

def postalcode_check(*args):
    """
    This function will filter postal codes that we input it as arguments with this criterias:
    1. string length must be 10 integers between 0-9.
    2. dash sign (-) must be placed between 5-digit couples
    example: 12345-67890 or 38754-98124 is acceptable and something like sdh32-jh678 or 6857632989 isn\'t acceptable.
    """
    res = []
    for item in args:
        if item[5] != "-" or len(item) != 11:
            continue
        for char in item:
            if char not in "0123456789":
                break
        res.append(item)
    return res
print(help(postalcode_check))
new = postalcode_check("alieotehdkf", "12345-67890", "34987-89325", "r46522-79879234", "2875345235738")
print(new)
