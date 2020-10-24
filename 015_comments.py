# Video https://youtu.be/f8m9egb6FDE
# Toto je jednoriadkovy komment

# Vsetko co je zakomentovane sa nikdy nevykona 
# print("toto sa nevykona ked je to zakomentovane")

"""
Toto je viac riadkovy komentar v pythone. Ktory sa tiez nikdy nevykona.
Takyto komentar sa pouziva na nieco co sa vola docstring.
Docstring specifikuje funkciu pomocou komentaru. 
"""

def custom_addition(elemnt1, element2):
    """
    Custom addition function dedicated for addition of element1 and element2.

    Parameters:

    element1 (int): First element
    element2 (int): Second element

    Returns:
    
    sum (int): addition
    """
    return element1 + element2


# Type hints example. Is a special python 3.+ syntax dedicated to ease the process of refactoring and linting
def custom_addition_2(element1: int, element2: int) -> int:
    return element1 + element2

print(custom_addition_2(1,2))

# Ak chcete nieco zakomentovat alebo odkomentovat vo VS code stlacte skratku:
# ctrl + /
# Takto viete zakomentovat aj viac oznacenych riadkov