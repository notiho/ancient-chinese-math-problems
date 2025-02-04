"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
This problem involves determining the price ratio of two types of arrows (expensive and cheap) given the total cost and total quantity. Let's break it down and translate it into Python code.

### Problem:
- Total money spent: 980 qian.
- Total arrows purchased: 5820 arrows.
- The goal is to determine the price ratio (expensive vs. cheap arrows) and the number of each type of arrow.

### Procedure:
1. Use the total money as the divisor (法).
2. Use the total number of arrows as the dividend (實).
3. Divide the dividend by the divisor to find the base price ratio.
4. Adjust the ratio to ensure integers for both types of arrows.
5. Use the adjusted ratio to calculate the number of expensive and cheap arrows.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 980  # qian
total_arrows = 5820  # arrows

# Step 1: Calculate the base price ratio
base_ratio = Fraction(total_arrows, total_money)

# Step 2: Simplify the ratio to integers
# The base ratio gives us the relationship between expensive and cheap arrows
# Let's assume the ratio is a:b (expensive:cheap)
a = base_ratio.numerator  # Expensive arrows per qian
b = base_ratio.denominator  # Cheap arrows per qian

# Step 3: Calculate the number of expensive and cheap arrows
# Total expensive arrows = (total_money * a) / (a + b)
# Total cheap arrows = (total_money * b) / (a + b)
total_expensive_arrows = (total_money * a) // (a + b)
total_cheap_arrows = (total_money * b) // (a + b)

# Step 4: Calculate the price per arrow for each type
price_per_expensive_arrow = Fraction(1, a)  # qian per arrow
price_per_cheap_arrow = Fraction(1, b)  # qian per arrow

# Output the results
print(f"Expensive arrows: {total_expensive_arrows} arrows, {a} arrows per qian")
print(f"Cheap arrows: {total_cheap_arrows} arrows, {b} arrows per qian")
print(f"Price per expensive arrow: {price_per_expensive_arrow} qian")
print(f"Price per cheap arrow: {price_per_cheap_arrow} qian")
#----- content ends here -----


"""


### Explanation of Variables:
- `a` and `b` represent the price ratio of expensive to cheap arrows.
- `total_expensive_arrows` and `total_cheap_arrows` calculate the number of each type of arrow based on the ratio.
- `price_per_expensive_arrow` and `price_per_cheap_arrow` calculate the cost of each type of arrow.

### Example Output:
If the ratio is determined to be 3:2 (for example):
```
Expensive arrows: 588 arrows, 3 arrows per qian
Cheap arrows: 5232 arrows, 2 arrows per qian
Price per expensive arrow: 1/3 qian
Price per cheap arrow: 1/2 qian
```

This code dynamically calculates the results based on the given total money and total arrows.
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 291
Variable 'b' has wrong value. Expected: 5, Actual: 49
Missing variable in output: 'c'
Missing variable in output: 'd'"""
