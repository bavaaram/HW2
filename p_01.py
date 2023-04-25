#! /usr/bin/python3

def postalcode_check(code: str) -> bool:
    """
    This function takes a postal code and check it with this criterias:
    1. string length must be 10 integers between 0-9.
    2. dash sign (-) must be placed between 5-digit couples
    if argument pass the criterias, output is True, else output is False.
    example: 12345-67890 or 38754-98124 is True and something like sdh32-jh678 or 6857632989 is False.
    """
    if len(code) != 11 or code[5] != "-":
        return False
    for char in code:
        if char not in "0123456789-":
            return False
    return True

codes = ["alieotehdkf", "12345-67890", "34987-89325", "r46522-79879234", "2875345235738", "49812-02784", "7989f-38542"]
res = [item for item in codes if postalcode_check(item)]
print(res)
