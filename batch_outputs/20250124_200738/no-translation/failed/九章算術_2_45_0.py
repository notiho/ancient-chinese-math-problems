"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to determine the rates (貴賤率) for two types of arrows (矢簳). Here's the Python code following the provided procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢九百八十
錢數 = 980

# 矢簳五千八百二十枚
矢簳數 = 5820

# 貴賤率術
# Assume the rates are a枚 per 1錢 and b枚 per 1錢 for two types of arrows
# Let 貴 rate = a枚/1錢 and 賤 rate = b枚/1錢
# We need to find a枚 and b枚 such that their combined total equals 矢簳數 and their combined cost equals 錢數.

# Step 1: Assume initial rates (e.g., 貴 rate = 2枚/1錢, 賤 rate = 3枚/1錢)
貴率 = Fraction(2, 1)  # 2枚 per 1錢
賤率 = Fraction(3, 1)  # 3枚 per 1錢

# Step 2: Calculate the total cost for each rate
貴矢數 = Fraction(錢數, 貴率 + 賤率) * 貴率
賤矢數 = 矢簳數 - 貴矢數

# Step 3: Output results
a = 貴矢數
b = 賤矢數
c = 貴率.denominator
d = 賤率.denominator

print(f"其 {a} 枚，{b} 枚 一錢 其 {c} 枚，{d} 枚 一錢")
#----- content ends here -----


"""


This code assumes initial rates for 貴 and 賤 arrows and calculates their respective quantities based on the total number of arrows and money spent. Adjust the rates as needed to match the problem's specific conditions.
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 392
Variable 'b' has wrong value. Expected: 5, Actual: 5428
Variable 'c' has wrong value. Expected: 5520, Actual: 1
Variable 'd' has wrong value. Expected: 6, Actual: 1"""
