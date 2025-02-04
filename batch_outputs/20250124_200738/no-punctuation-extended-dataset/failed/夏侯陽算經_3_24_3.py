"""
今有絲三千四百八十五兩令織紗一匹用絲五兩問得紗幾何
術曰先置絲數以二因之退位一等即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 liang of silk. It is required to weave silk gauze, with 5 liang of silk used per piece.
Question: how many pieces of silk gauze can be obtained?

The procedure says: First, place the amount of silk and multiply it by 2. Then, shift the position down by one place, and the result is obtained.

Answer: *a* pieces.
"""

# 絲三千四百八十五兩
絲數 = 3485

# 用絲五兩
用絲 = 5

# 先置絲數以二因之
絲數 = 絲數 * 2

# 退位一等即得
a = 絲數 // 用絲#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 697, Actual: 1394"""
