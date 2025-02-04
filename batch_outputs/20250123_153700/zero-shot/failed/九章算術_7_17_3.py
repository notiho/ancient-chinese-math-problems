"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a斤 ，銀重 b斤 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
gold_count = 9  # number of gold pieces
silver_count = 11  # number of silver pieces

# First condition: gold weighs 3 jin, silver weighs 2 + 5/11 jin
gold_weight_1 = Fraction(3)
silver_weight_1 = Fraction(2) + Fraction(5, 11)
total_weight_1 = gold_count * gold_weight_1 + silver_count * silver_weight_1
difference_1 = total_weight_1 - 49  # difference from 49 jin

# Second condition: gold weighs 2 jin, silver weighs 1 + 7/11 jin
gold_weight_2 = Fraction(2)
silver_weight_2 = Fraction(1) + Fraction(7, 11)
total_weight_2 = gold_count * gold_weight_2 + silver_count * silver_weight_2
difference_2 = total_weight_2 - 49  # difference from 49 jin

# Solve for the weights of gold and silver
numerator_gold = difference_2 * 11 - difference_1 * 11  # Multiply by 11 to clear denominators
denominator = (gold_weight_1 - gold_weight_2) * gold_count * 11
a = numerator_gold / denominator  # Weight of one gold piece

numerator_silver = difference_1 * 11 - difference_2 * 11  # Multiply by 11 to clear denominators
b = numerator_silver / (silver_weight_2 - silver_weight_1) / silver_count

# Results
a = Fraction(a).limit_denominator()  # Weight of one gold piece in jin
b = Fraction(b).limit_denominator()  # Weight of one silver piece in jin

# Output the results
a, b


"""


This code calculates the weights of one gold piece (`a`) and one silver piece (`b`) in `jin` using the given conditions.
"""


"""
Variable 'a' has wrong value. Expected: 143/64, Actual: -2
Variable 'b' has wrong value. Expected: 117/64, Actual: -22"""
