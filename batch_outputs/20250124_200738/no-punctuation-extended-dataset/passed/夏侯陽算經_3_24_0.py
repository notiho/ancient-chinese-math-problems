"""
今有絲三千四百八十五兩令織紗一匹用絲五兩問得紗幾何
術曰先置絲數以二因之退位一等即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 liang of silk. It is required to weave one bolt of fine silk, which uses 5 liang of silk.
Question: how many bolts of fine silk can be obtained?

The procedure says: First, place the amount of silk and multiply it by 2. Then, reduce the position by one place (i.e., divide by 10). This gives the result.

Answer: *a* bolts.
"""

# 絲三千四百八十五兩
絲數 = 3485

# 用絲五兩
用絲 = 5

# 先置絲數，以二因之
絲數乘二 = 絲數 * 2

# 退位一等，即得
a = Fraction(絲數乘二, 10)  # This simplifies the process of reducing the position by one place.#----- content ends here -----

"""
"""
