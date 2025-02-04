"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 斤 b錢 其 c斤 斤 d錢 
"""

"""
This problem involves calculating the price per unit weight (jin rate) for a given amount of money and silk. Let's break it down and encode the procedure step by step.

### Problem Description:
- Money spent: 13,970 (in qian).
- Silk purchased: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
- Question: What is the price per jin (jin rate)?

### Procedure:
1. Place the quantities of shi, jun, jin, liang, and zhu as the divisor (法).
2. Multiply the total money by the rate (所率) to get the dividend (實).
3. Divide the dividend by the divisor to get the rate per jin.
4. If there is a remainder, adjust accordingly.

### Units Conversion:
- 1 shi = 120 jin
- 1 jun = 20 jin
- 1 jin = 16 liang
- 1 liang = 24 zhu

### Python Code:


"""


from fractions import Fraction

# Given values
錢數 = 13970  # Total money spent
石 = 1        # Silk in shi
鈞 = 2        # Silk in jun
斤 = 28       # Silk in jin
兩 = 3        # Silk in liang
銖 = 5        # Silk in zhu

# Unit conversions
# Convert everything to jin
總斤 = (石 * 120) + (鈞 * 20) + 斤 + Fraction(兩, 16) + Fraction(銖, 16 * 24)

# Procedure
# 法: Total weight in jin
法 = 總斤

# 實: Total money spent
實 = 錢數

# Rate per jin (斤率)
斤率 = Fraction(實, 法)

# Answer
a = 斤率.numerator  # Numerator of the rate (qian per jin)
b = 斤率.denominator  # Denominator of the rate (qian per jin)

print(f"其 {a} 錢 其 {b} 錢")


"""


### Explanation:
- We first convert all the given weights (shi, jun, jin, liang, zhu) into a single unit, jin.
- The total money spent is divided by the total weight to calculate the price per jin (斤率).
- The result is expressed as a fraction to maintain precision.

### Answer:
The price per jin is `a` qian and `b` qian.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 5364480
Variable 'b' has wrong value. Expected: 67, Actual: 72269
Missing variable in output: 'c'
Missing variable in output: 'd'"""
