"""
今有絲三千四百八十五兩令織紗一匹用絲五兩問得紗幾何
術曰先置絲數以二因之退位一等即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 liang of silk. It is required to weave silk gauze, with 5 liang of silk used for each piece.
Question: how many pieces of silk gauze can be obtained?

The procedure says: First, place the number of silk [liang].
Multiply it by 2, then shift the place value down by 1 level (i.e., divide by 10).
This gives the result.

Answer: *a* pieces.
"""

# 絲三千四百八十五兩
絲數 = 3485

# 以二因之
絲數乘二 = 2 * 絲數

# 退位一等 (即除以 10)
a = 絲數乘二 // 10#----- content ends here -----

"""
"""
