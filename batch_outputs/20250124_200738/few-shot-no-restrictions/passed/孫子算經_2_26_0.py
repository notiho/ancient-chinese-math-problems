"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from the treasury, but the exact amount of silk lost is unknown.
It is only heard that when dividing the silk among people in the grass, each person gets 6 bolts of silk, with 6 bolts left over.
If each person gets 7 bolts of silk, there are not enough bolts for 7 bolts per person.
Question: how many people and how many bolts of silk are there?

The procedure says: First, place the "6 bolts per person" on the top right, and the "6 bolts left over" on the bottom right.
Then, place the "7 bolts per person" on the top left, and the "not enough for 7 bolts" on the bottom left.
Multiply the corresponding values diagonally, add the results to get the total silk, and add the "leftover" and "not enough" to get the total number of people.

Answer: there are *a* people and *b* bolts of silk.
"""

# Known values
人得六匹 = 6  # Each person gets 6 bolts
盈六匹 = 6   # 6 bolts left over
人得七匹 = 7  # Each person gets 7 bolts
不足七匹 = 7  # Not enough for 7 bolts

# Procedure
# Multiply diagonally and add to get the total silk
絹 = (人得六匹 * 不足七匹) + (人得七匹 * 盈六匹)

# Add the leftover and not enough to get the total number of people
人 = 盈六匹 + 不足七匹

# Final result
a = 人
b = 絹#----- content ends here -----

"""
"""
