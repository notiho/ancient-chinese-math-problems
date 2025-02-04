"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
答曰： a日 。
"""

"""
Suppose there are three daughters:
- The eldest daughter returns home every 5 days.
- The middle daughter returns home every 4 days.
- The youngest daughter returns home every 3 days.

Question: after how many days will all three daughters return home on the same day?

Answer: *a* days.
"""

# Define the return periods for the three daughters
長女 = 5
中女 = 4
少女 = 3

# Find the least common multiple (LCM) of the three periods
# LCM formula: LCM(a, b) = (a * b) / GCD(a, b)

# Helper function to calculate the greatest common divisor (GCD)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Calculate LCM of two numbers
def lcm(x, y):
    return (x * y) // gcd(x, y)

# Calculate LCM of all three periods
a = lcm(lcm(長女, 中女), 少女)

a  # This is the number of days after which all three daughters will meet.
"""
"""
