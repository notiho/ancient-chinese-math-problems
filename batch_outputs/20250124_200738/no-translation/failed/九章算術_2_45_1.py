"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to calculate the rates of two types of arrows (矢簳) based on the given total money and total number of arrows. Here's the Python code following the "反其率術" procedure:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢九百八十
錢數 = 980

# 矢簳五千八百二十枚
矢簳數 = 5820

# Assume the two types of arrows are divided into x枚 and y枚
# Let x枚 be the cheaper arrow and y枚 be the more expensive arrow
# We need to find their rates (貴賤率)

# Step 1: Define the rates (假設貴賤率)
# Let the cheaper arrow rate be 1枚 per 1錢 (a枚, b枚 一錢)
# Let the more expensive arrow rate be 2枚 per 1錢 (c枚, d枚 一錢)

# Step 2: Calculate the total cost for each type of arrow
# Total cost = (number of cheaper arrows / cheaper rate) + (number of expensive arrows / expensive rate)

# Step 3: Solve for the distribution of arrows
# Total arrows = cheaper arrows + expensive arrows
# Total cost = cost of cheaper arrows + cost of expensive arrows

# Using the given data:
# Total arrows = 5820
# Total cost = 980

# Let x枚 be the cheaper arrows and y枚 be the expensive arrows
# x枚 + y枚 = 5820
# (x枚 / 1) + (y枚 / 2) = 980

# Solve the equations:
# y枚 = 5820 - x枚
# x枚 + (5820 - x枚) / 2 = 980
# 2x枚 + 5820 - x枚 = 1960
# x枚 = 1960 - 5820
# x枚 = 3880
# y枚 = 5820 - 3880
# y枚 = 1940

# Step 4: Calculate the rates
a = 1  # Cheaper rate (枚 per 錢)
b = 1  # Cheaper rate (錢 per 枚)
c = 2  # Expensive rate (枚 per 錢)
d = 1  # Expensive rate (錢 per 枚)

# Final answer:
# Cheaper arrows: 3880枚 at a rate of 1枚 per 1錢
# Expensive arrows: 1940枚 at a rate of 2枚 per 1錢
#----- content ends here -----


"""


**Answer:**
- Cheaper arrows: `a = 3880枚`, `b = 1錢`
- Expensive arrows: `c = 1940枚`, `d = 2錢`
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 1
Variable 'b' has wrong value. Expected: 5, Actual: 1
Variable 'c' has wrong value. Expected: 5520, Actual: 2
Variable 'd' has wrong value. Expected: 6, Actual: 1"""
