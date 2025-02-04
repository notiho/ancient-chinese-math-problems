"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 斤 b錢 其 c斤 斤 d錢 
"""

"""
The problem involves calculating the price per unit weight of silk based on the total cost and the total weight. Let's break it down step by step and encode the procedure in Python.

### Problem Breakdown:
- Total money spent: 13,970 (錢)
- Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Question: What is the price per 斤 (斤率)?

### Procedure:
1. Combine the weights (石, 鈞, 斤, 兩, 銖) into a single unit (斤).
2. Use the total money spent and the total weight to calculate the price per 斤.
3. Follow the ancient method to ensure the calculation adheres to the described procedure.

### Python Code:


"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
石_to_斤 = 120  # 1 石 = 120 斤
鈞_to_斤 = 30   # 1 鈞 = 30 斤
兩_to_斤 = Fraction(1, 16)  # 16 兩 = 1 斤
銖_to_斤 = Fraction(1, 384)  # 384 銖 = 1 斤

# Combine all weights into 斤
總斤 = (石 * 石_to_斤) + (鈞 * 鈞_to_斤) + 斤 + (兩 * 兩_to_斤) + (銖 * 銖_to_斤)

# Calculate the price per 斤 (斤率)
斤率 = Fraction(錢數, 總斤)

# Output results
a = 斤率.numerator  # The numerator represents the price in 錢
b = 斤率.denominator  # The denominator represents the weight in 斤

print(f"其 {a} 錢 其 {b} 斤")


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into a single unit (斤) using the provided conversion factors.
2. **Price Calculation**: The total money spent (錢數) is divided by the total weight (總斤) to calculate the price per 斤 (斤率).
3. **Output**: The result is expressed as a fraction, where the numerator (`a`) represents the price in 錢, and the denominator (`b`) represents the weight in 斤.

### Answer:
The price per 斤 is expressed as `a 錢 per b 斤`.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 5364480
Variable 'b' has wrong value. Expected: 67, Actual: 79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
