"""
今有出錢六百一十，買羽二千一百翭。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a翭 ， b翭 一錢 其 c翭 ， d翭 一錢
"""

"""
To solve this problem, we need to determine the values of "a", "b", "c", and "d" based on the given information. Here's the Python code to compute the values:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_money = 610  # Total money in units
total_feathers = 2100  # Total feathers in units

# Step 1: Compute the average rate (feathers per unit money)
average_rate = Fraction(total_feathers, total_money)

# Step 2: Determine the rates for the two types of feathers
# Let the rates be "b feathers per 1 unit money" and "d feathers per 1 unit money"
# Assume b > d (more expensive feathers have a higher rate)
b = average_rate.numerator + 1  # One more than the average numerator
d = average_rate.numerator - 1  # One less than the average numerator

# Step 3: Compute the quantities of each type of feather
# Let "a" be the number of feathers at rate "b feathers per 1 unit money"
# Let "c" be the number of feathers at rate "d feathers per 1 unit money"
# Total money spent on each type must sum to total_money
# Total feathers must sum to total_feathers

# Solve for "a" and "c"
a = Fraction(total_money * b - total_feathers, b - d)
c = total_feathers - a

# Output the results
a = int(a)
b = int(b)
c = int(c)
d = int(d)

# Results
print("a =", a, "feathers")
print("b =", b, "feathers per unit money")
print("c =", c, "feathers")
print("d =", d, "feathers per unit money")
#----- content ends here -----


"""


This code calculates the values of "a", "b", "c", and "d" based on the problem's description. The results will be printed as integers.
"""


"""
Variable 'a' has wrong value. Expected: 1140, Actual: 63305
Variable 'b' has wrong value. Expected: 3, Actual: 211
Variable 'c' has wrong value. Expected: 960, Actual: -61205
Variable 'd' has wrong value. Expected: 4, Actual: 209"""
