"""
今有絲三千四百八十五兩令織紗一匹用絲五兩問得紗幾何
術曰先置絲數以二因之退位一等即得
答曰 a匹
"""

#----- content starts here -----
"""
Suppose there are 3485 liang of silk. It is required to weave it into gauze, with 5 liang of silk used per piece.
Question: how many pieces of gauze can be made?

The procedure says: First, place the number of silk [liang]. Multiply it by 2, then shift the place value down by one level. This gives the result.

Answer: *a* pieces.
"""

# 絲三千四百八十五兩
絲數 = 3485

# 用絲五兩
用絲 = 5

# 先置絲數，以二因之
結果 = 2 * 絲數

# 退位一等，即得
a = 結果 // 10  # Shifting the place value down by one level is equivalent to integer division by 10.#----- content ends here -----

"""
"""
