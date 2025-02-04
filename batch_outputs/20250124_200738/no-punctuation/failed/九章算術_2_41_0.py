"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 斤 b錢 其 c斤 斤 d錢 
"""

"""
The problem involves calculating the price per unit weight (jin) of silk based on the total cost and total weight. Let's break it down and implement the procedure step by step.

### Problem:
You have spent 13,970 qian to buy 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu of silk. The question asks for the price per jin (unit weight) and the price per jin in qian.

### Procedure:
1. Place the total weight in shi, jun, jin, liang, and zhu as the divisor (法).
2. Multiply the total cost (錢數) by the respective rates to get the dividend (實).
3. Divide the dividend by the divisor to get the price per jin (斤率).
4. If there is a remainder, adjust the calculation accordingly.

### Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in qian
錢數 = 13970

# Total weight in shi, jun, jin, liang, and zhu
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
鈞_to_斤 = 30  # 1 jun = 30 jin
兩_to_斤 = Fraction(1, 16)  # 16 liang = 1 jin
銖_to_斤 = Fraction(1, 384)  # 384 zhu = 1 jin

# Convert total weight to jin
總斤 = 石 * 300 + 鈞 * 鈞_to_斤 + 斤 + 兩 * 兩_to_斤 + 銖 * 銖_to_斤

# Calculate price per jin (斤率)
斤率 = Fraction(錢數, 總斤)

# Extract integer and fractional parts of the price per jin
a = 斤率.numerator // 斤率.denominator  # Integer part (qian per jin)
b = 斤率 - a  # Fractional part (remaining qian per jin)

# Output results
print(f"其 {a} 錢 {b} 錢")
#----- content ends here -----


"""


### Explanation:
1. Convert the total weight into jin using the given conversion factors.
2. Divide the total cost by the total weight to get the price per jin.
3. Extract the integer and fractional parts of the price per jin for the final answer.

### Answer:
The price per jin is `a` qian and `b` fractional qian.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 35
Variable 'b' has wrong value. Expected: 67, Actual: 147065/149069
Missing variable in output: 'c'
Missing variable in output: 'd'"""
