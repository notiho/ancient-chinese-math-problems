"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
答曰： a日 。
"""

"""
Suppose there are three daughters. The eldest daughter returns home every 5 days, the middle daughter every 4 days, and the youngest daughter every 3 days.
Question: after how many days will all three daughters meet at home?

Answer: *a* days.
"""

# 長女五日一歸
長女 = 5

# 中女四日一歸
中女 = 4

# 少女三日一歸
少女 = 3

# Find the least common multiple (LCM) of the three periods
# LCM is calculated as the product of the numbers divided by their greatest common divisor (GCD)

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

# Calculate LCM for all three daughters
a = lcm(lcm(長女, 中女), 少女)

a  # The answer is the LCM in days
"""
"""
