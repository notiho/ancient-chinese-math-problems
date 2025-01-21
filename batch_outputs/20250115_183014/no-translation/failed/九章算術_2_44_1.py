"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to calculate the rate of exchange (貴賤率) for the two types of 羽 (翭). Here's the Python code based on the given procedure:


"""


from fractions import Fraction

# 出錢六百一十
錢數 = 610

# 買羽二千一百翭
羽數 = 2100

# Procedure:
# 貴賤率術曰：以錢數為法，所率為實，實如法而一。
法 = 錢數
實 = 羽數

# 不滿法者反以實減法，法少，實多。
if 實 < 法:
    法, 實 = 實, 法

# 二物各以所得多少之數乘法實，即物數。
a = 法  # First type of 羽
b = Fraction(法, 實)  # First type rate (翭 per 錢)

c = 實  # Second type of 羽
d = Fraction(實, 法)  # Second type rate (翭 per 錢)

# Output results
print(f"其 {a}翭 ， {b}翭 一錢 其 {c}翭 ， {d}翭 一錢")


"""


This code follows the procedure described in the problem and calculates the rates for the two types of 羽 (翭). Let me know if you need further clarification or adjustments!
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 610
Variable 'b' has wrong value. Expected: 3, Actual: 61/210
Variable 'c' has wrong value. Expected: 960, Actual: 2100
Variable 'd' has wrong value. Expected: 4, Actual: 210/61"""
