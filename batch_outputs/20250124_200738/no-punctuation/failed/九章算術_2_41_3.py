"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 斤 b錢 其 c斤 斤 d錢 
"""

"""
The problem you provided is about calculating the price per unit weight (斤, jin) of silk based on the total cost and the total weight. Let's break it down and translate it into Python step by step.

The problem states:

- Total money spent: 13,970 (錢)
- Total weight: 1 石 (shi), 2 鈞 (jun), 28 斤 (jin), 3 兩 (liang), 5 銖 (zhu)
- The goal is to calculate the price per 斤 (jin).

The procedure ("術") explains how to calculate the rate:

1. Place the total weight (in 石, 鈞, 斤, 兩, 銖) as the divisor (法).
2. Multiply the total money by the rate to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit weight.
4. If there is a remainder, adjust accordingly.

Now, let's implement this in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in 石, 鈞, 斤, 兩, 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
鈞_per_石 = 30  # 1 石 = 30 鈞
斤_per_鈞 = 10  # 1 鈞 = 10 斤
兩_per_斤 = 16  # 1 斤 = 16 兩
銖_per_兩 = 24  # 1 兩 = 24 銖

# Convert total weight to 銖 (smallest unit)
總銖 = (
    石 * 鈞_per_石 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    鈞 * 斤_per_鈞 * 兩_per_斤 * 銖_per_兩 +
    斤 * 兩_per_斤 * 銖_per_兩 +
    兩 * 銖_per_兩 +
    銖
)

# Convert 銖 back to 斤 as the divisor (法)
法 = Fraction(總銖, 兩_per_斤 * 銖_per_兩)

# Calculate the price per 斤 (斤率)
斤率 = Fraction(錢數, 法)

# Convert the price per 斤 to 錢 and fractions of 錢
a = 斤率.numerator // 斤率.denominator  # Whole 錢
b = 斤率.numerator % 斤率.denominator   # Fractional part of 錢

# Output the results
print(f"其 {a} 錢 {b}/{斤率.denominator} 錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (銖) for precise calculation.
2. **Divisor (法)**: The total weight in 銖 is converted back to 斤, which serves as the divisor.
3. **Rate Calculation**: The total money is divided by the total weight (in 斤) to get the price per 斤.
4. **Fraction Handling**: The result is expressed as whole 錢 and fractional 錢.

### Answer Format:
The output will give the price per 斤 in the form of whole 錢 and fractional 錢.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 40
Variable 'b' has wrong value. Expected: 67, Actual: 16120
Missing variable in output: 'c'
Missing variable in output: 'd'"""
