"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of feudal lords, and they are to divide 60 oranges such that each rank receives 3 more oranges than the rank below it.
Question: how many oranges does each of the five ranks receive?

The procedure says:
First, place the number of people (5) and add 3 oranges incrementally for each rank:
- The lowest rank gets 3 oranges,
- The next rank gets 6 oranges,
- Then 9 oranges,
- Then 12 oranges,
- And the highest rank gets 15 oranges.
Sum these increments, obtaining 45.
Subtract this from the total number of oranges (60), leaving a remainder.
Divide this remainder by the number of people (5), obtaining 3 oranges per person as the base amount.
Add the uncombined increments to this base amount:
- The highest rank gets 18 oranges,
- The next rank gets 15 oranges,
- Then 12 oranges,
- Then 9 oranges,
- And the lowest rank gets 6 oranges.

Answer: The highest rank (Gong) gets *a* oranges, the next rank (Hou) gets *b* oranges, the next rank (Bo) gets *c* oranges, the next rank (Zi) gets *d* oranges, and the lowest rank (Nan) gets *e* oranges.
"""

# Total oranges
total_oranges = 60

# Incremental distribution for each rank
increments = [3, 6, 9, 12, 15]

# Sum of increments
sum_increments = sum(increments)

# Remaining oranges after subtracting increments
remaining_oranges = total_oranges - sum_increments

# Base amount per person
base_amount = remaining_oranges // 5

# Final distribution by adding base amount to increments
公 = base_amount + increments[4]  # Highest rank
侯 = base_amount + increments[3]
伯 = base_amount + increments[2]
子 = base_amount + increments[1]
男 = base_amount + increments[0]  # Lowest rank

# Assign results
a = 公
b = 侯
c = 伯
d = 子
e = 男

# Results
a, b, c, d, e#----- content ends here -----

"""
"""
