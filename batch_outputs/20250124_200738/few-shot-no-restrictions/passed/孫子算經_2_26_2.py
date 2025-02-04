"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from the treasury, but the exact amount of silk lost is unknown.
It is only heard that when dividing the silk among people in the grass:
- If each person gets 6 bolts of silk, there are 6 bolts left over.
- If each person gets 7 bolts of silk, there are not enough by 7 bolts.

Question: How many people and how many bolts of silk are there?

The procedure says:
- First, place the "6 bolts per person" on the top right and the "6 bolts left over" on the bottom right.
- Then, place the "7 bolts per person" on the top left and the "7 bolts short" on the bottom left.
- Multiply diagonally, sum the results to find the total silk.
- Add the surplus and deficit to find the total number of people.

Answer: The thief group has *a* people, and there are *b* bolts of silk.
"""

from fractions import Fraction

# Known values
每人得六匹 = 6
盈六匹 = 6
每人得七匹 = 7
不足七匹 = 7

# Multiply diagonally and sum to find the total silk
絹 = (每人得六匹 * 不足七匹) + (每人得七匹 * 盈六匹)

# Add the surplus and deficit to find the total number of people
人 = 盈六匹 + 不足七匹

# Final answer
a = 人
b = 絹

a, b  # Output the number of people and the number of silk bolts#----- content ends here -----

"""
"""
