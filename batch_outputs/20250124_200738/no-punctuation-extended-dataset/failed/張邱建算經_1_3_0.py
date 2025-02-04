"""
今有封山周棧三百二十五里甲乙丙三人同遶周棧行甲日行一百五十里乙日行一百二十里丙日行九十里問周行㡬何日㑹
術曰置甲乙丙行里數求等數為法以周棧里數為實實如法而得一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there is a mountain path with a perimeter of 325 li. Three people, A, B, and C, walk around the path together.
A walks 150 li per day, B walks 120 li per day, and C walks 90 li per day.
Question: after how many days will they meet at the starting point?

The procedure says: Place the distances walked per day by A, B, and C. Find their least common multiple (LCM) as the divisor.
Take the perimeter of the mountain path as the dividend. Divide the dividend by the divisor to obtain the result.

Answer: *a* days.
"""

# 周棧三百二十五里
周棧 = 325

# 甲日行一百五十里
甲 = 150

# 乙日行一百二十里
乙 = 120

# 丙日行九十里
丙 = 90

# 求等數為法 (求甲、乙、丙的最小公倍數)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

法 = lcm(lcm(甲, 乙), 丙)

# 以周棧里數為實
實 = 周棧

# 實如法而得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65/6, Actual: 13/72"""
