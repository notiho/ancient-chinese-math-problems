"""
今有五等諸侯，共分橘子六十顆，人別加三顆。問：五人各得幾何？
術曰：先置人數別加三顆于下，次六顆，次九顆，次一十二顆，上十五顆，副并之，得四十五，以減六十顆，餘人數除之，得人三顆，各加不并者，上得一十八顆為公分，次得一十五為侯分，次得一十二為伯分，次得九為子分，下得六為男分。
答曰：公 a顆 ，侯 b顆 ，伯 c顆 ，子 d顆 ，男 e顆 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Total number of oranges
total_oranges = 60

# Additional oranges for each rank
additional_oranges = [15, 12, 9, 6, 3]

# Sum of additional oranges
sum_additional_oranges = sum(additional_oranges)

# Remaining oranges after subtracting the sum of additional oranges
remaining_oranges = total_oranges - sum_additional_oranges

# Each person's base share
base_share = remaining_oranges // 5

# Calculating the share for each rank
a = base_share + additional_oranges[0]  # 公
b = base_share + additional_oranges[1]  # 侯
c = base_share + additional_oranges[2]  # 伯
d = base_share + additional_oranges[3]  # 子
e = base_share + additional_oranges[4]  # 男

# The results
a, b, c, d, e


"""


### Explanation:
1. The total number of oranges is 60.
2. Each rank has an additional number of oranges: 公 (15), 侯 (12), 伯 (9), 子 (6), 男 (3).
3. The sum of these additional oranges is subtracted from the total, leaving the base share for each person.
4. The base share is divided equally among the 5 ranks.
5. Each rank's share is calculated by adding their additional oranges to the base share.

### Results:
- `a` (公): 18 oranges
- `b` (侯): 15 oranges
- `c` (伯): 12 oranges
- `d` (子): 9 oranges
- `e` (男): 6 oranges
"""


"""
"""
