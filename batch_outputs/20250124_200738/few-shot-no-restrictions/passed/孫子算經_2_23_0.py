"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

#----- content starts here -----
"""
Suppose there are five ranks of nobles (Gong, Hou, Bo, Zi, Nan), and they are to divide 60 oranges.
Each person is to receive 3 more oranges than the person ranked below them.
Question: how many oranges does each of the five nobles receive?

The procedure says:
First, place the number of people and add 3 oranges for each rank below:
- The lowest rank (Nan) gets 6 oranges.
- The next rank (Zi) gets 9 oranges.
- The next rank (Bo) gets 12 oranges.
- The next rank (Hou) gets 15 oranges.
- The highest rank (Gong) gets 18 oranges.
Add these together, obtaining 45.
Subtract this from the total of 60 oranges, leaving 15.
Divide this remainder equally among the 5 people, giving 3 oranges each.
Add this to the base distribution for each rank.

Answer:
The Gong gets *a* oranges.
The Hou gets *b* oranges.
The Bo gets *c* oranges.
The Zi gets *d* oranges.
The Nan gets *e* oranges.
"""

# Total oranges
總橘子 = 60

# Base distribution (without the extra 3 oranges for each person)
base_distribution = [6, 9, 12, 15, 18]

# Sum of the base distribution
base_sum = sum(base_distribution)

# Remaining oranges after subtracting the base distribution
remaining_oranges = 總橘子 - base_sum

# Divide the remaining oranges equally among the 5 people
extra_per_person = remaining_oranges // 5

# Final distribution
final_distribution = [base + extra_per_person for base in base_distribution]

# Assign results
e, d, c, b, a = final_distribution

# Output results
a, b, c, d, e  # 公, 侯, 伯, 子, 男#----- content ends here -----

"""
"""
