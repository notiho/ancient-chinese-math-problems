"""
今有出錢一千一百二十，買絲一石二鈞十八斤。欲其貴賤斤率之，問︰各幾何？
其率術曰：各置所買石、鈞、斤、兩以為法，以所率乘錢數為實，實如法而一。不滿法者反以實減法，法賤實貴。
荅曰：其 a鈞 ，斤 b錢 。其 c石 ，斤 d錢 。
"""

"""
To solve this problem, we need to calculate the price per unit weight (斤) for silk, given the total cost and the total weight. The weight is given in a mixed unit system: 石 (shi), 鈞 (jun), and 斤 (jin). Here's how we can compute the values step by step:

1. Convert the total weight into a single unit (斤).
2. Divide the total cost by the total weight to find the price per 斤.
3. Assign the results to the variables `a`, `b`, `c`, and `d` as described in the problem.

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given data
total_cost = 1120  # Total cost in 錢
total_weight_stone = 1  # 石
total_weight_jun = 2  # 鈞
total_weight_jin = 18  # 斤

# Conversion factors
jin_per_jun = 30  # 1 鈞 = 30 斤
jin_per_stone = 300  # 1 石 = 300 斤

# Convert total weight to 斤
total_weight_in_jin = (total_weight_stone * jin_per_stone) + (total_weight_jun * jin_per_jun) + total_weight_jin

# Calculate price per 斤
price_per_jin = Fraction(total_cost, total_weight_in_jin)

# Assign results
a = price_per_jin.numerator  # 鈞 price in 錢
b = price_per_jin.denominator  # 鈞 price denominator
c = price_per_jin.numerator  # 石 price in 錢
d = price_per_jin.denominator  # 石 price denominator

# Results
a, b, c, d


"""


This code calculates the price per unit weight (斤) and assigns the results to the variables `a`, `b`, `c`, and `d`. The use of the `Fraction` class ensures that the results are represented accurately as fractions if needed.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 80
Variable 'b' has wrong value. Expected: 5, Actual: 27
Variable 'c' has wrong value. Expected: 13/12, Actual: 80
Variable 'd' has wrong value. Expected: 6, Actual: 27"""
