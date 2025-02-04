"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Total oranges
total_oranges = 60

# Additional oranges for each rank
additional_oranges = [15, 12, 9, 6, 3]

# Sum of additional oranges
sum_additional = sum(additional_oranges)

# Remaining oranges after subtracting additional oranges
remaining_oranges = total_oranges - sum_additional

# Oranges per person
per_person = Fraction(remaining_oranges, 5)

# Calculate the total oranges for each rank
a = per_person + additional_oranges[0]  # 公
b = per_person + additional_oranges[1]  # 侯
c = per_person + additional_oranges[2]  # 伯
d = per_person + additional_oranges[3]  # 子
e = per_person + additional_oranges[4]  # 男

# Results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. The total number of oranges is 60.
2. Each rank (公, 侯, 伯, 子, 男) receives an additional number of oranges: 15, 12, 9, 6, and 3 respectively.
3. The sum of these additional oranges is subtracted from the total to find the remaining oranges.
4. The remaining oranges are divided equally among the 5 ranks.
5. Each rank's total oranges are calculated by adding their respective additional oranges to the shared amount.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the number of oranges for 公, 侯, 伯, 子, and 男 respectively.
"""


"""
"""
