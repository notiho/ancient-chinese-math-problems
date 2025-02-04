"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to determine the rates of two types of arrows (矢簳) based on the total money spent and the total number of arrows purchased. Let's proceed step by step according to the procedure described in the problem.

---

### Definitions:
- **出錢**: Total money spent = 980
- **矢簳**: Total arrows = 5820

The problem asks us to find the rates (貴賤率) of two types of arrows, where one type is more expensive (貴) and the other is cheaper (賤). The procedure involves reversing the rates (反其率) and calculating the quantities accordingly.

---

### Procedure in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢 (Total money spent)
錢數 = 980

# 矢簳 (Total arrows)
矢簳數 = 5820

# 貴賤率 (Assume rates: 貴 = 2 arrows per 1錢, 賤 = 8 arrows per 1錢)
貴率 = 2  # 貴: 2枚/錢
賤率 = 8  # 賤: 8枚/錢

# Step 1: Calculate the total "實" for each rate
貴實 = 錢數 * 貴率  # 貴的總數
賤實 = 錢數 * 賤率  # 賤的總數

# Step 2: Reverse the rates (反其率)
# 貴: 1錢 gets 2枚, so reverse rate is 1/2
# 賤: 1錢 gets 8枚, so reverse rate is 1/8
貴反率 = Fraction(1, 貴率)
賤反率 = Fraction(1, 賤率)

# Step 3: Calculate the total number of 貴 and 賤 arrows
# Using the formula: 矢簳數 = 貴反率 * 貴實 + 賤反率 * 賤實
貴矢 = Fraction(矢簳數 * 貴反率, 貴反率 + 賤反率)
賤矢 = 矢簳數 - 貴矢

# Step 4: Calculate the number of arrows per 1錢 for each type
貴每錢 = Fraction(貴矢, 錢數)
賤每錢 = Fraction(賤矢, 錢數)

# Results
a = 貴矢  # 貴的總數
b = 貴每錢  # 貴的每錢數
c = 賤矢  # 賤的總數
d = 賤每錢  # 賤的每錢數

# Output
a, b, c, d
#----- content ends here -----


"""


---

### Explanation of Variables:
- `a`: Total number of expensive arrows (貴矢).
- `b`: Number of expensive arrows per 1錢 (貴每錢).
- `c`: Total number of cheap arrows (賤矢).
- `d`: Number of cheap arrows per 1錢 (賤每錢).

This code follows the procedure described in the problem and calculates the rates and quantities of the two types of arrows.
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 4656
Variable 'b' has wrong value. Expected: 5, Actual: 1164/245
Variable 'c' has wrong value. Expected: 5520, Actual: 1164
Variable 'd' has wrong value. Expected: 6, Actual: 291/245"""
