"""
今有絲三千四百八十五兩令織紗一匹用絲五兩問得紗幾何
術曰先置絲數以二因之退位一等即得
答曰 a匹
"""

"""
Suppose there are 3485 liang of silk. It is ordered to weave silk gauze, with 5 liang of silk used per bolt.
Question: how many bolts of silk gauze can be obtained?

The procedure says: First, place the amount of silk and multiply it by 2. Then, reduce the place value by one level, and the result is obtained.

Answer: *a* bolts.
"""

# 絲三千四百八十五兩
絲 = 3485

# 用絲五兩
用絲 = 5

# 先置絲數，以二因之
因之 = 絲 * 2

# 退位一等，即得
a =因之 // 用絲
"""
Variable 'a' has wrong value. Expected: 697, Actual: 1394"""
